from __future__ import annotations

import logging
from typing import Optional, cast

import pyvisa
from PySide6.QtCore import QObject, Signal, Slot
from pyvisa.resources import MessageBasedResource

from dg2000_trigger.models import OutputConfig
from dg2000_trigger.scpi import (
    configure_outputs,
    format_cycle_start_log,
    try_emit_single_pulse,
    try_return_to_local,
)

log = logging.getLogger(__name__)


class VisaWorker(QObject):
    """在专用 QThread 中执行全部 VISA I/O，避免阻塞 GUI。"""

    log_line = Signal(str)
    resources_ready = Signal(list)
    scan_failed = Signal(str)

    connection_result = Signal(bool, str, str)
    """connected, resource, idn 或错误信息（用于日志/状态栏）。"""

    cycle_prepare_failed = Signal(str)
    cycle_started = Signal(str)
    cycle_edge_done = Signal(bool, int, str)
    """下一段输出是否为 ON、下一次定时毫秒、日志行。"""
    cycle_edge_failed = Signal(str)

    dialog_warning = Signal(str, str)
    dialog_critical = Signal(str, str)

    shutdown_complete = Signal()

    def __init__(self) -> None:
        super().__init__()
        self._rm: Optional[pyvisa.ResourceManager] = None
        self._dev: Optional[MessageBasedResource] = None
        self._cycle_active = False

    @Slot()
    def scan_resources(self) -> None:
        try:
            if self._rm is None:
                self._rm = pyvisa.ResourceManager()
            resources = list(self._rm.list_resources())
            self.resources_ready.emit(resources)
        except Exception as exc:
            log.exception("VISA 扫描失败")
            self.scan_failed.emit(str(exc))

    @Slot(str)
    def connect_instrument(self, resource: str) -> None:
        resource = resource.strip()
        if not resource:
            self.dialog_warning.emit("缺少资源", "请先扫描并选择资源。")
            return
        try:
            if self._dev is not None:
                self.close_connection()

            rm = self._rm or pyvisa.ResourceManager()
            self._rm = rm
            raw = rm.open_resource(resource)
            raw.read_termination = "\n"
            raw.write_termination = "\n"
            raw.timeout = 8000
            dev = cast(MessageBasedResource, raw)
            idn = dev.query("*IDN?").strip()
            self._dev = dev
            self.connection_result.emit(True, resource, idn)
        except Exception as exc:
            self._dev = None
            log.exception("连接失败: %s", resource)
            self.connection_result.emit(False, resource, str(exc))

    @Slot()
    def close_connection(self) -> None:
        if self._dev is None:
            self.connection_result.emit(False, "", "")
            return
        try:
            try_return_to_local(self._dev)
            self._dev.close()
            self.log_line.emit("已断开设备连接。")
        except Exception as exc:
            self.log_line.emit(f"断开连接异常: {exc}")
        finally:
            self._dev = None
            self._cycle_active = False
            self.connection_result.emit(False, "", "")

    @Slot()
    def query_idn(self) -> None:
        if self._dev is None:
            self.dialog_warning.emit("未连接", "请先连接设备。")
            return
        try:
            idn = self._dev.query("*IDN?").strip()
            self.log_line.emit(f"IDN: {idn}")
        except Exception as exc:
            log.exception("读取 IDN 失败")
            self.dialog_critical.emit("读取失败", str(exc))
            self.log_line.emit(f"读取 IDN 失败: {exc}")

    @Slot(object, int, int)
    def prepare_start_cycle(self, cfg_obj: object, on_ms: int, off_ms: int) -> None:
        if self._dev is None:
            self.cycle_prepare_failed.emit("未连接设备。")
            return
        if not isinstance(cfg_obj, OutputConfig):
            self.cycle_prepare_failed.emit("内部错误：参数类型不正确。")
            return
        cfg = cfg_obj
        self._cycle_active = True
        try:
            configure_outputs(self._dev, cfg)
            self._dev.write(":OUTP1 ON")
            self._dev.write(":OUTP2 ON")
            try_emit_single_pulse(self._dev)
            err = self._dev.query(":SYST:ERR?").strip()
            on_s = on_ms / 1000.0
            off_s = off_ms / 1000.0
            self.cycle_started.emit(format_cycle_start_log(cfg, on_s, off_s, err))
        except Exception as exc:
            self._cycle_active = False
            log.exception("启动循环失败")
            self.cycle_prepare_failed.emit(str(exc))

    @Slot(bool, int, int)
    def apply_cycle_edge(self, outputs_on: bool, on_ms: int, off_ms: int) -> None:
        dev = self._dev
        if dev is None or not self._cycle_active:
            return
        try:
            if outputs_on:
                dev.write(":OUTP1 OFF")
                dev.write(":OUTP2 OFF")
                self.cycle_edge_done.emit(False, off_ms, "周期切换: 停波。")
            else:
                dev.write(":OUTP1 ON")
                dev.write(":OUTP2 ON")
                try_emit_single_pulse(dev)
                self.cycle_edge_done.emit(True, on_ms, "周期切换: 发波。")
        except Exception as exc:
            self._cycle_active = False
            log.exception("周期输出异常")
            self.cycle_edge_failed.emit(str(exc))

    @Slot()
    def stop_cycle_outputs(self) -> None:
        self._cycle_active = False
        if self._dev is None:
            self.dialog_warning.emit("未连接", "请先连接设备。")
            return
        try:
            self._dev.write(":OUTP1 OFF")
            self._dev.write(":OUTP2 OFF")
            self.log_line.emit("已停止循环并关闭 CH1/CH2 输出。")
        except Exception as exc:
            log.exception("停止输出失败")
            self.dialog_critical.emit("停止失败", str(exc))

    @Slot()
    def return_to_local(self) -> None:
        if self._dev is None:
            self.dialog_warning.emit("未连接", "请先连接设备。")
            return
        try:
            try_return_to_local(self._dev)
            self.log_line.emit("已尝试切回本地面板控制。")
        except Exception as exc:
            self.dialog_warning.emit("提示", str(exc))

    @Slot()
    def shutdown(self) -> None:
        self._cycle_active = False
        try:
            if self._dev is not None:
                try:
                    try_return_to_local(self._dev)
                    self._dev.close()
                except Exception:
                    log.exception("关闭设备时异常")
                self._dev = None
            if self._rm is not None:
                try:
                    self._rm.close()
                except Exception:
                    log.exception("关闭 ResourceManager 异常")
                self._rm = None
        finally:
            self.shutdown_complete.emit()
