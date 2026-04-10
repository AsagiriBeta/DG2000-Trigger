from __future__ import annotations

import sys
from dataclasses import dataclass
from typing import Optional

import pyvisa
from PySide6.QtCore import QTimer, Qt
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QDoubleSpinBox,
    QFormLayout,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QPlainTextEdit,
    QVBoxLayout,
    QWidget,
)


@dataclass
class OutputConfig:
    ch1_freq_hz: float
    ch1_vpp: float
    ch1_offset_v: float
    ch1_phase_deg: float
    ch2_pulse_freq_hz: float
    ch2_pulse_width_s: float
    ch2_low_v: float
    ch2_high_v: float
    output_load: str


def try_return_to_local(dev) -> None:
    # Model compatibility differs; try multiple commands safely.
    for cmd in (":SYST:KLOC OFF", ":SYST:LOC", "SYST:KLOC OFF", "SYST:LOC"):
        try:
            dev.write(cmd)
        except Exception:
            continue


def try_emit_single_pulse(dev) -> None:
    """在 CH2 上触发一次单脉冲（用于设备间同步通信）。"""
    # 不同固件命令兼容性存在差异，按常见写法依次尝试。
    for cmd in (":SOUR2:BURS:TRIG", "SOUR2:BURS:TRIG", "*TRG"):
        try:
            dev.write(cmd)
            return
        except Exception:
            continue


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("DG2000 控制台")
        self.resize(980, 680)

        self.rm: Optional[pyvisa.ResourceManager] = None
        self.dev = None
        self.cycle_timer = QTimer(self)
        self.cycle_timer.setSingleShot(True)
        self.cycle_timer.timeout.connect(self._on_cycle_timer)
        self.cycle_running = False
        self.cycle_state_on = False

        root = QWidget()
        self.setCentralWidget(root)
        outer = QVBoxLayout(root)

        outer.addWidget(self._build_connection_box())
        outer.addWidget(self._build_params_box())
        outer.addWidget(self._build_actions_box())
        outer.addWidget(self._build_log_box(), stretch=1)

        self.refresh_resources()

    def _build_connection_box(self) -> QGroupBox:
        box = QGroupBox("连接")
        layout = QGridLayout(box)

        self.resource_combo = QComboBox()
        self.resource_combo.setEditable(True)
        self.resource_combo.setMinimumWidth(460)

        self.refresh_btn = QPushButton("扫描设备")
        self.connect_btn = QPushButton("连接")
        self.disconnect_btn = QPushButton("断开")
        self.idn_btn = QPushButton("读取 IDN")

        self.status_edit = QLineEdit("未连接")
        self.status_edit.setReadOnly(True)

        self.refresh_btn.clicked.connect(self.refresh_resources)
        self.connect_btn.clicked.connect(self.connect_device)
        self.disconnect_btn.clicked.connect(self.disconnect_device)
        self.idn_btn.clicked.connect(self.query_idn)

        layout.addWidget(QLabel("资源:"), 0, 0)
        layout.addWidget(self.resource_combo, 0, 1, 1, 3)
        layout.addWidget(self.refresh_btn, 0, 4)
        layout.addWidget(self.connect_btn, 1, 1)
        layout.addWidget(self.disconnect_btn, 1, 2)
        layout.addWidget(self.idn_btn, 1, 3)
        layout.addWidget(QLabel("状态:"), 2, 0)
        layout.addWidget(self.status_edit, 2, 1, 1, 4)

        return box

    def _build_params_box(self) -> QGroupBox:
        box = QGroupBox("参数")
        layout = QHBoxLayout(box)

        ch1_group = QGroupBox("CH1 正弦")
        ch1_form = QFormLayout(ch1_group)
        self.ch1_freq = self._double(1000.0, 0.001, 1e9, 3)
        self.ch1_vpp = self._double(2.0, 0.001, 20.0, 3)
        self.ch1_offset = self._double(0.0, -10.0, 10.0, 3)
        self.ch1_phase = self._double(0.0, -360.0, 360.0, 3)
        ch1_form.addRow("频率 Hz", self.ch1_freq)
        ch1_form.addRow("幅值 Vpp", self.ch1_vpp)
        ch1_form.addRow("偏置 V", self.ch1_offset)
        ch1_form.addRow("相位 deg", self.ch1_phase)

        ch2_group = QGroupBox("CH2 脉冲")
        ch2_form = QFormLayout(ch2_group)
        self.ch2_freq = self._double(1000.0, 0.001, 1e9, 3)
        self.ch2_width = self._double(100e-6, 1e-9, 10.0, 9)
        self.ch2_low = self._double(0.0, -10.0, 10.0, 3)
        self.ch2_high = self._double(5.0, -10.0, 10.0, 3)
        ch2_form.addRow("频率 Hz", self.ch2_freq)
        ch2_form.addRow("脉宽 s", self.ch2_width)
        ch2_form.addRow("低电平 V", self.ch2_low)
        ch2_form.addRow("高电平 V", self.ch2_high)

        common_group = QGroupBox("公共")
        common_form = QFormLayout(common_group)
        self.load_combo = QComboBox()
        self.load_combo.addItems(["INF", "50"])
        self.load_combo.setCurrentText("INF")
        self.on_time_s = self._double(1.0, 0.001, 3600.0, 3)
        self.off_time_s = self._double(1.0, 0.001, 3600.0, 3)
        common_form.addRow("输出负载", self.load_combo)
        common_form.addRow("发波时长 s", self.on_time_s)
        common_form.addRow("停波时长 s", self.off_time_s)

        layout.addWidget(ch1_group)
        layout.addWidget(ch2_group)
        layout.addWidget(common_group)

        return box

    def _build_actions_box(self) -> QGroupBox:
        box = QGroupBox("动作")
        layout = QHBoxLayout(box)

        self.apply_btn = QPushButton("开始循环输出")
        self.stop_btn = QPushButton("停止循环并关输出")
        self.local_btn = QPushButton("切回本地面板")

        self.apply_btn.clicked.connect(self.start_cycle)
        self.stop_btn.clicked.connect(self.stop_outputs)
        self.local_btn.clicked.connect(self.return_local)

        layout.addWidget(self.apply_btn)
        layout.addWidget(self.stop_btn)
        layout.addWidget(self.local_btn)
        return box

    def _build_log_box(self) -> QGroupBox:
        box = QGroupBox("日志")
        layout = QVBoxLayout(box)
        self.log = QPlainTextEdit()
        self.log.setReadOnly(True)
        layout.addWidget(self.log)
        return box

    @staticmethod
    def _double(default: float, minimum: float, maximum: float, decimals: int) -> QDoubleSpinBox:
        w = QDoubleSpinBox()
        w.setDecimals(decimals)
        w.setRange(minimum, maximum)
        w.setValue(default)
        w.setSingleStep(max(10 ** (-decimals), 0.001))
        return w

    def _append_log(self, text: str) -> None:
        self.log.appendPlainText(text)

    def _ensure_rm(self) -> pyvisa.ResourceManager:
        if self.rm is None:
            self.rm = pyvisa.ResourceManager()
        return self.rm

    def _require_connected(self) -> bool:
        if self.dev is None:
            QMessageBox.warning(self, "未连接", "请先连接设备。")
            return False
        return True

    def refresh_resources(self) -> None:
        try:
            rm = self._ensure_rm()
            resources = rm.list_resources()
        except Exception as exc:
            self._append_log(f"扫描失败: {exc}")
            QMessageBox.critical(self, "扫描失败", str(exc))
            return

        current = self.resource_combo.currentText().strip()
        self.resource_combo.clear()
        self.resource_combo.addItems(list(resources))
        if current:
            self.resource_combo.setEditText(current)

        if resources:
            self._append_log("发现资源:")
            for r in resources:
                self._append_log(f"  {r}")
        else:
            self._append_log("未发现 VISA 资源。")

    def connect_device(self) -> None:
        resource = self.resource_combo.currentText().strip()
        if not resource:
            QMessageBox.warning(self, "缺少资源", "请先扫描并选择资源。")
            return

        try:
            if self.dev is not None:
                self.disconnect_device()

            rm = self._ensure_rm()
            dev = rm.open_resource(resource)
            dev.read_termination = "\n"
            dev.write_termination = "\n"
            dev.timeout = 8000
            idn = dev.query("*IDN?").strip()

            self.dev = dev
            self.status_edit.setText(f"已连接: {resource}")
            self._append_log(f"连接成功: {idn}")
        except Exception as exc:
            self.status_edit.setText("未连接")
            self._append_log(f"连接失败: {exc}")
            QMessageBox.critical(self, "连接失败", str(exc))

    def disconnect_device(self) -> None:
        if self.dev is None:
            return

        try:
            try_return_to_local(self.dev)
            self.dev.close()
            self._append_log("已断开设备连接。")
        except Exception as exc:
            self._append_log(f"断开连接异常: {exc}")
        finally:
            self.dev = None
            self.status_edit.setText("未连接")

    def query_idn(self) -> None:
        if not self._require_connected():
            return
        try:
            idn = self.dev.query("*IDN?").strip()
            self._append_log(f"IDN: {idn}")
        except Exception as exc:
            self._append_log(f"读取 IDN 失败: {exc}")
            QMessageBox.critical(self, "读取失败", str(exc))

    def _read_config(self) -> OutputConfig:
        return OutputConfig(
            ch1_freq_hz=self.ch1_freq.value(),
            ch1_vpp=self.ch1_vpp.value(),
            ch1_offset_v=self.ch1_offset.value(),
            ch1_phase_deg=self.ch1_phase.value(),
            ch2_pulse_freq_hz=self.ch2_freq.value(),
            ch2_pulse_width_s=self.ch2_width.value(),
            ch2_low_v=self.ch2_low.value(),
            ch2_high_v=self.ch2_high.value(),
            output_load=self.load_combo.currentText(),
        )

    def _configure_waveforms(self, cfg: OutputConfig) -> None:
        dev = self.dev
        dev.write(":OUTP1 OFF")
        dev.write(":OUTP2 OFF")

        dev.write(f":OUTP1:LOAD {cfg.output_load}")
        dev.write(f":OUTP2:LOAD {cfg.output_load}")

        dev.write(
            f":SOUR1:APPL:SIN {cfg.ch1_freq_hz:.12g},{cfg.ch1_vpp:.12g},{cfg.ch1_offset_v:.12g}"
        )
        dev.write(f":SOUR1:PHAS {cfg.ch1_phase_deg:.12g}")

        dev.write(":SOUR2:FUNC PULS")
        dev.write(f":SOUR2:FREQ {cfg.ch2_pulse_freq_hz:.12g}")
        dev.write(f":SOUR2:PULS:WIDT {cfg.ch2_pulse_width_s:.12g}")
        dev.write(f":SOUR2:VOLT:LOW {cfg.ch2_low_v:.12g}")
        dev.write(f":SOUR2:VOLT:HIGH {cfg.ch2_high_v:.12g}")

        # CH1 连续输出；CH2 配为触发单次脉冲，周期开始时只发一次。
        dev.write(":SOUR1:BURS:STAT OFF")
        dev.write(":SOUR2:BURS:STAT ON")
        dev.write(":SOUR2:BURS:MODE TRIG")
        dev.write(":SOUR2:BURS:NCYC 1")
        dev.write(":SOUR2:BURS:TRIG:SOUR BUS")

    def start_cycle(self) -> None:
        if not self._require_connected():
            return

        cfg = self._read_config()
        try:
            self._configure_waveforms(cfg)
            self.cycle_running = True
            self.cycle_state_on = True
            self.dev.write(":OUTP1 ON")
            self.dev.write(":OUTP2 ON")
            try_emit_single_pulse(self.dev)

            on_ms = max(1, int(self.on_time_s.value() * 1000))
            self.cycle_timer.start(on_ms)

            err = self.dev.query(":SYST:ERR?").strip()
            self._append_log(
                "循环已开始: "
                f"CH1 {cfg.ch1_freq_hz:.3f}Hz/{cfg.ch1_vpp:.3f}Vpp, "
                f"CH2 {cfg.ch2_pulse_freq_hz:.3f}Hz/{cfg.ch2_pulse_width_s:.6g}s, "
                f"发波 {self.on_time_s.value():.3f}s / 停波 {self.off_time_s.value():.3f}s, "
                f"设备状态 {err}"
            )
        except Exception as exc:
            self.cycle_running = False
            self.cycle_timer.stop()
            self._append_log(f"启动循环失败: {exc}")
            QMessageBox.critical(self, "启动失败", str(exc))

    def _on_cycle_timer(self) -> None:
        if not self.cycle_running or self.dev is None:
            return

        try:
            if self.cycle_state_on:
                self.dev.write(":OUTP1 OFF")
                self.dev.write(":OUTP2 OFF")
                self.cycle_state_on = False
                off_ms = max(1, int(self.off_time_s.value() * 1000))
                self.cycle_timer.start(off_ms)
                self._append_log("周期切换: 停波。")
            else:
                self.dev.write(":OUTP1 ON")
                self.dev.write(":OUTP2 ON")
                try_emit_single_pulse(self.dev)
                self.cycle_state_on = True
                on_ms = max(1, int(self.on_time_s.value() * 1000))
                self.cycle_timer.start(on_ms)
                self._append_log("周期切换: 发波。")
        except Exception as exc:
            self.cycle_running = False
            self.cycle_timer.stop()
            self._append_log(f"周期输出异常，已停止: {exc}")
            QMessageBox.critical(self, "运行异常", str(exc))

    def stop_outputs(self) -> None:
        if not self._require_connected():
            return
        try:
            self.cycle_running = False
            self.cycle_timer.stop()
            self.dev.write(":OUTP1 OFF")
            self.dev.write(":OUTP2 OFF")
            self._append_log("已停止循环并关闭 CH1/CH2 输出。")
        except Exception as exc:
            self._append_log(f"停止输出失败: {exc}")
            QMessageBox.critical(self, "停止失败", str(exc))

    def return_local(self) -> None:
        if not self._require_connected():
            return
        try:
            try_return_to_local(self.dev)
            self._append_log("已尝试切回本地面板控制。")
        except Exception as exc:
            self._append_log(f"切回本地失败: {exc}")
            QMessageBox.warning(self, "提示", str(exc))

    def closeEvent(self, event) -> None:  # type: ignore[override]
        self.cycle_running = False
        self.cycle_timer.stop()
        self.disconnect_device()
        if self.rm is not None:
            try:
                self.rm.close()
            except Exception:
                pass
            self.rm = None
        super().closeEvent(event)


def main() -> int:
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    w = MainWindow()
    w.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
