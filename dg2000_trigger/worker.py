from __future__ import annotations

import logging
from typing import Optional, cast

import pyvisa
from PySide6.QtCore import QObject, Signal, Slot
from pyvisa.resources import MessageBasedResource

from dg2000_trigger.models import OutputConfig
from dg2000_trigger.scpi import (
    configure_ch1_burst_cycle,
    configure_outputs,
    format_cycle_start_log,
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
        self._cycle_cfg: Optional[OutputConfig] = None

    def _arm_ch2_single_pulse(self, dev: MessageBasedResource, cfg: OutputConfig) -> None:
        """重申 CH2 burst 配置，等待触发。"""
        dev.write(":OUTP2 ON")
        dev.write(":SOUR2:FUNC PULS")
        dev.write(":SOUR2:FREQ 1000")
        dev.write(f":SOUR2:PULS:WIDT {cfg.ch2_pulse_width_s:.12g}")
        dev.write(f":SOUR2:PULS:DEL {cfg.ch2_delay_s:.12g}")
        dev.write(f":SOUR2:VOLT:LOW {cfg.ch2_low_v:.12g}")
        dev.write(f":SOUR2:VOLT:HIGH {cfg.ch2_high_v:.12g}")
        dev.write(":SOUR2:BURS:STAT ON")
        dev.write(":SOUR2:BURS:MODE TRIG")
        dev.write(":SOUR2:BURS:NCYC 1")
        try:
            dev.write(f":SOUR2:BURS:IDLE {cfg.ch2_idle_level}")
        except Exception:
            pass
        for cmd in (":SOUR2:BURS:TRIG:SOUR MAN",):
            try:
                dev.write(cmd)
                break
            except Exception:
                continue

    def _trigger_cycle_start(self, dev: MessageBasedResource) -> None:
        """显式触发 CH1/CH2 burst，兼容不同固件的全局触发行为差异。"""
        dev.write(":SOUR1:BURS:TRIG")
        dev.write(":SOUR2:BURS:TRIG")

    def _clear_error_queue(self, dev: MessageBasedResource) -> None:
        for _ in range(6):
            err = self._query_safe(dev, ":SYST:ERR?")
            if err.startswith("0,") or err.startswith("+0,"):
                break

    def _query_safe(self, dev: MessageBasedResource, cmd: str) -> str:
        try:
            return dev.query(cmd).strip()
        except Exception as exc:
            return f"<ERR {exc}>"

    def _log_ch2_state(self, dev: MessageBasedResource, prefix: str) -> None:
        parts = [
            f"OUTP2={self._query_safe(dev, ':OUTP2?')}",
            f"FUNC={self._query_safe(dev, ':SOUR2:FUNC?')}",
            f"BURS={self._query_safe(dev, ':SOUR2:BURS:STAT?')}",
            f"MODE={self._query_safe(dev, ':SOUR2:BURS:MODE?')}",
            f"TRIGSRC={self._query_safe(dev, ':SOUR2:BURS:TRIG:SOUR?')}",
            f"LOW={self._query_safe(dev, ':SOUR2:VOLT:LOW?')}",
            f"HIGH={self._query_safe(dev, ':SOUR2:VOLT:HIGH?')}",
            f"ERR={self._query_safe(dev, ':SYST:ERR?')}",
        ]
        self.log_line.emit(f"{prefix}: " + ", ".join(parts))

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
            self._cycle_cfg = None
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
        self._cycle_cfg = cfg
        try:
            configure_outputs(self._dev, cfg)
            on_s = on_ms / 1000.0
            off_s = off_ms / 1000.0
            ncyc, actual_on_s, actual_period_s = configure_ch1_burst_cycle(
                self._dev, cfg, on_s, off_s
            )
            self._dev.write(":OUTP1 ON")
            self._arm_ch2_single_pulse(self._dev, cfg)
            self._trigger_cycle_start(self._dev)
            err = self._dev.query(":SYST:ERR?").strip()
            self.cycle_started.emit(
                format_cycle_start_log(cfg, actual_on_s, max(0.0, actual_period_s - actual_on_s), err)
                + f", CH1 Burst NCYC={ncyc}, PER={actual_period_s:.6g}s, TRIG=SHARED"
            )
        except Exception as exc:
            self._cycle_active = False
            self._cycle_cfg = None
            log.exception("启动循环失败")
            self.cycle_prepare_failed.emit(str(exc))

    @Slot(bool, int, int)
    def apply_cycle_edge(self, outputs_on: bool, on_ms: int, off_ms: int) -> None:
        dev = self._dev
        cfg = self._cycle_cfg
        if dev is None or not self._cycle_active or cfg is None:
            return
        try:
            if outputs_on:
                self.cycle_edge_done.emit(False, off_ms, "周期切换: 停波段（CH1 由 Burst 内部时序控制）。")
            else:
                on_s = on_ms / 1000.0
                off_s = off_ms / 1000.0
                ncyc, actual_on_s, actual_period_s = configure_ch1_burst_cycle(
                    dev, cfg, on_s, off_s
                )
                self._arm_ch2_single_pulse(dev, cfg)
                self._trigger_cycle_start(dev)
                self.cycle_edge_done.emit(
                    True,
                    on_ms,
                    (
                        "周期切换: 发波段（CH2 已触发）。"
                        f"CH1 Burst NCYC={ncyc}, ON={actual_on_s:.6g}s, PER={actual_period_s:.6g}s, TRIG=SHARED"
                    ),
                )
        except Exception as exc:
            self._cycle_active = False
            self._cycle_cfg = None
            log.exception("周期输出异常")
            self.cycle_edge_failed.emit(str(exc))

    @Slot()
    def test_ch2_pulse(self) -> None:
        """手动测试 CH2 是否能立即发出一次脉冲。"""
        dev = self._dev
        if dev is None:
            self.dialog_warning.emit("未连接", "请先连接设备。")
            return
        try:
            self._clear_error_queue(dev)
            if self._cycle_cfg is not None:
                self._arm_ch2_single_pulse(dev, self._cycle_cfg)
            else:
                # 测试按钮在未启动循环时仍使用安全默认值。
                default_cfg = OutputConfig(
                    ch1_freq_hz=1000.0,
                    ch1_vpp=2.0,
                    ch1_offset_v=0.0,
                    ch1_phase_deg=0.0,
                    ch2_pulse_width_s=0.001,
                    ch2_low_v=0.0,
                    ch2_high_v=5.0,
                    ch2_delay_s=0.0,
                    ch2_idle_level="BOTT",
                    output_load="INF",
                )
                self._arm_ch2_single_pulse(dev, default_cfg)
            dev.write(":SOUR2:BURS:TRIG")
            self._log_ch2_state(dev, "CH2 单脉冲测试已触发")
        except Exception as exc:
            self.dialog_critical.emit("测试失败", str(exc))
            self.log_line.emit(f"CH2 单脉冲测试失败: {exc}")

    @Slot()
    def test_ch2_square(self) -> None:
        """输出可见连续方波，快速排查示波器量程/接线问题。"""
        dev = self._dev
        if dev is None:
            self.dialog_warning.emit("未连接", "请先连接设备。")
            return
        try:
            self._clear_error_queue(dev)
            dev.write(":OUTP2 OFF")
            dev.write(":SOUR2:BURS:STAT OFF")
            dev.write(":SOUR2:FUNC SQU")
            dev.write(":SOUR2:FREQ 2")
            dev.write(":SOUR2:VOLT:LOW 0")
            dev.write(":SOUR2:VOLT:HIGH 5")
            dev.write(":OUTP2 ON")
            self._log_ch2_state(dev, "CH2 连续方波测试(2Hz/0-5V)已启动")
        except Exception as exc:
            self.dialog_critical.emit("测试失败", str(exc))
            self.log_line.emit(f"CH2 连续方波测试失败: {exc}")

    @Slot()
    def stop_cycle_outputs(self) -> None:
        self._cycle_active = False
        self._cycle_cfg = None
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
        self._cycle_cfg = None
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
