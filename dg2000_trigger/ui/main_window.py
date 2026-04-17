from __future__ import annotations

import logging

from PySide6.QtCore import (
    QEventLoop,
    QMetaObject,
    QSettings,
    QThread,
    QTimer,
    Qt,
    Signal,
    Slot,
)
from PySide6.QtWidgets import (
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
    QSpinBox,
    QVBoxLayout,
    QWidget,
)

from dg2000_trigger import __version__
from dg2000_trigger.models import OutputConfig
from dg2000_trigger.worker import VisaWorker

log = logging.getLogger(__name__)


class MainWindow(QMainWindow):
    """主界面：仅负责控件与线程间信号编排，不直接执行 VISA I/O。"""

    request_scan = Signal()
    request_connect = Signal(str)
    cycle_prepare_requested = Signal(object, int, int)
    cycle_edge_requested = Signal(bool, int, int)

    def __init__(self) -> None:
        super().__init__()
        self._settings = QSettings("dg2000-trigger", "dg2000-trigger")
        self.setWindowTitle(f"DG2000 控制台 v{__version__}")
        self.resize(980, 680)

        self._instrument_connected = False
        self._cycle_running = False
        self._cycle_outputs_on = False
        self._cycle_timer = QTimer(self)
        self._cycle_timer.setSingleShot(True)
        self._cycle_timer.timeout.connect(self._on_cycle_timer)

        self._thread = QThread(self)
        self._worker = VisaWorker()
        self._worker.moveToThread(self._thread)
        # 必须在主线程执行 quit，以便工作线程事件循环退出；使用 Queued 避免跨线程直接调 quit 的边界问题。
        self._worker.shutdown_complete.connect(self._thread.quit, Qt.ConnectionType.QueuedConnection)
        self._wire_worker_signals()
        self.request_scan.connect(
            self._worker.scan_resources, Qt.ConnectionType.QueuedConnection
        )
        self._thread.start()

        root = QWidget()
        self.setCentralWidget(root)
        outer = QVBoxLayout(root)

        outer.addLayout(self._build_header_layout())
        outer.addWidget(self._build_connection_box())
        outer.addWidget(self._build_params_box())
        outer.addWidget(self._build_actions_box())
        outer.addWidget(self._build_log_box(), stretch=1)

        self.request_connect.connect(
            self._worker.connect_instrument, Qt.ConnectionType.QueuedConnection
        )
        self.cycle_prepare_requested.connect(
            self._worker.prepare_start_cycle, Qt.ConnectionType.QueuedConnection
        )
        self.cycle_edge_requested.connect(
            self._worker.apply_cycle_edge, Qt.ConnectionType.QueuedConnection
        )

        self.refresh_btn.clicked.connect(self._request_resource_scan)
        self.disconnect_btn.clicked.connect(self._worker.close_connection)
        self.idn_btn.clicked.connect(self._worker.query_idn)
        self.stop_btn.clicked.connect(self._on_stop_clicked)
        self.test_pulse_btn.clicked.connect(self._on_test_pulse_clicked)
        self.test_square_btn.clicked.connect(self._on_test_square_clicked)
        self.local_btn.clicked.connect(self._worker.return_to_local)

        self.apply_btn.clicked.connect(self.start_cycle)
        self._load_settings()

        QTimer.singleShot(0, self.request_scan.emit)

    def _wire_worker_signals(self) -> None:
        w = self._worker
        w.log_line.connect(self._append_log)
        w.resources_ready.connect(self._on_resources_ready)
        w.scan_failed.connect(self._on_scan_failed)
        w.connection_result.connect(self._on_connection_result)
        w.cycle_prepare_failed.connect(self._on_cycle_prepare_failed)
        w.cycle_started.connect(self._on_cycle_started)
        w.cycle_edge_done.connect(self._on_cycle_edge_done)
        w.cycle_edge_failed.connect(self._on_cycle_edge_failed)
        w.dialog_warning.connect(self._warning)
        w.dialog_critical.connect(self._critical)

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

        self.connect_btn.clicked.connect(self._emit_connect_request)

        layout.addWidget(QLabel("资源:"), 0, 0)
        layout.addWidget(self.resource_combo, 0, 1, 1, 3)
        layout.addWidget(self.refresh_btn, 0, 4)
        layout.addWidget(self.connect_btn, 1, 1)
        layout.addWidget(self.disconnect_btn, 1, 2)
        layout.addWidget(self.idn_btn, 1, 3)
        layout.addWidget(QLabel("状态:"), 2, 0)
        layout.addWidget(self.status_edit, 2, 1, 1, 4)

        return box

    def _build_header_layout(self) -> QHBoxLayout:
        layout = QHBoxLayout()
        layout.addStretch(1)
        version_label = QLabel(f"版本: v{__version__}")
        version_label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        layout.addWidget(version_label)
        return layout

    def _build_params_box(self) -> QGroupBox:
        box = QGroupBox("参数")
        layout = QHBoxLayout(box)

        ch1_group = QGroupBox("CH1 正弦")
        ch1_form = QFormLayout(ch1_group)
        self.ch1_freq = self._double(0.001, 0.000001, 1000.0, 3)
        self.ch1_freq.setSuffix(" MHz")
        self.ch1_vpp = self._double(2.0, 0.001, 20.0, 3)
        self.ch1_offset = self._double(0.0, -10.0, 10.0, 3)
        self.ch1_phase = self._double(0.0, -360.0, 360.0, 3)
        ch1_form.addRow("频率", self.ch1_freq)
        ch1_form.addRow("幅值 Vpp", self.ch1_vpp)
        ch1_form.addRow("偏置 V", self.ch1_offset)
        ch1_form.addRow("相位 deg", self.ch1_phase)

        ch2_group = QGroupBox("CH2 脉冲")
        ch2_form = QFormLayout(ch2_group)
        self.ch2_width = self._double(0.1, 0.000001, 10000.0, 3)
        self.ch2_width.setSuffix(" ms")
        self.ch2_after_sine_delay = self._double(0.0, 0.0, 10000.0, 3)
        self.ch2_after_sine_delay.setSuffix(" ms")
        self.ch2_pulses_per_cycle = QSpinBox()
        self.ch2_pulses_per_cycle.setRange(1, 1000000)
        self.ch2_pulses_per_cycle.setValue(1)
        self.ch2_pulse_interval = self._double(1.0, 0.001, 10000.0, 3)
        self.ch2_pulse_interval.setSuffix(" ms")
        self.ch2_low = self._double(0.0, -10.0, 10.0, 3)
        self.ch2_high = self._double(5.0, -10.0, 10.0, 3)
        self.ch2_idle_combo = QComboBox()
        self.ch2_idle_combo.addItems(["BOTT", "TOP"])
        self.ch2_idle_combo.setCurrentText("BOTT")
        ch2_form.addRow("脉宽", self.ch2_width)
        ch2_form.addRow("正弦结束后延时", self.ch2_after_sine_delay)
        ch2_form.addRow("每周期方波个数", self.ch2_pulses_per_cycle)
        ch2_form.addRow("方波间隔", self.ch2_pulse_interval)
        ch2_form.addRow("低电平 V", self.ch2_low)
        ch2_form.addRow("高电平 V", self.ch2_high)
        ch2_form.addRow("空闲电平", self.ch2_idle_combo)

        common_group = QGroupBox("公共")
        common_form = QFormLayout(common_group)
        self.load_combo = QComboBox()
        self.load_combo.addItems(["INF", "50"])
        self.load_combo.setCurrentText("INF")
        self.cycle_period_s = self._double(2000.0, 1.0, 3600000.0, 3)
        self.cycle_period_s.setSuffix(" ms")
        self.sine_ratio_pct = self._double(50.0, 0.0, 100.0, 1)
        self.sine_ratio_pct.setSuffix(" %")
        common_form.addRow("输出负载", self.load_combo)
        common_form.addRow("周期时长", self.cycle_period_s)
        common_form.addRow("正弦段占比", self.sine_ratio_pct)

        layout.addWidget(ch1_group)
        layout.addWidget(ch2_group)
        layout.addWidget(common_group)

        return box

    def _build_actions_box(self) -> QGroupBox:
        box = QGroupBox("动作")
        layout = QHBoxLayout(box)

        self.apply_btn = QPushButton("开始循环输出")
        self.stop_btn = QPushButton("停止循环并关输出")
        self.test_pulse_btn = QPushButton("CH2 单脉冲测试")
        self.test_square_btn = QPushButton("CH2 连续方波测试")
        self.local_btn = QPushButton("切回本地面板")

        layout.addWidget(self.apply_btn)
        layout.addWidget(self.stop_btn)
        layout.addWidget(self.test_pulse_btn)
        layout.addWidget(self.test_square_btn)
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

    @Slot()
    def _append_log(self, text: str) -> None:
        self.log.appendPlainText(text)

    @Slot()
    def _request_resource_scan(self) -> None:
        self.request_scan.emit()

    @Slot()
    def _emit_connect_request(self) -> None:
        self.request_connect.emit(self.resource_combo.currentText().strip())

    @Slot(list)
    def _on_resources_ready(self, resources: list) -> None:
        current = self.resource_combo.currentText().strip()
        self.resource_combo.clear()
        self.resource_combo.addItems(resources)
        if current:
            self.resource_combo.setEditText(current)

        if resources:
            self._append_log("发现资源:")
            for r in resources:
                self._append_log(f"  {r}")
        else:
            self._append_log("未发现 VISA 资源。")

    @Slot(str)
    def _on_scan_failed(self, message: str) -> None:
        self._append_log(f"扫描失败: {message}")
        QMessageBox.critical(self, "扫描失败", message)

    @Slot(bool, str, str)
    def _on_connection_result(self, ok: bool, resource: str, payload: str) -> None:
        if ok:
            self._instrument_connected = True
            self.status_edit.setText(f"已连接: {resource}")
            self._append_log(f"连接成功: {payload}")
            return

        self._instrument_connected = False
        self._cycle_running = False
        self._cycle_timer.stop()
        self.status_edit.setText("未连接")
        if resource:
            self._append_log(f"连接失败: {payload}")
            QMessageBox.critical(self, "连接失败", payload)

    @Slot(str, str)
    def _warning(self, title: str, message: str) -> None:
        QMessageBox.warning(self, title, message)

    @Slot(str, str)
    def _critical(self, title: str, message: str) -> None:
        QMessageBox.critical(self, title, message)

    def _read_config(self) -> OutputConfig:
        return OutputConfig(
            ch1_freq_hz=self.ch1_freq.value() * 1_000_000.0,
            ch1_vpp=self.ch1_vpp.value(),
            ch1_offset_v=self.ch1_offset.value(),
            ch1_phase_deg=self.ch1_phase.value(),
            ch2_pulse_width_s=self.ch2_width.value() / 1000.0,
            ch2_after_sine_delay_s=self.ch2_after_sine_delay.value() / 1000.0,
            ch2_pulses_per_cycle=self.ch2_pulses_per_cycle.value(),
            ch2_pulse_interval_s=self.ch2_pulse_interval.value() / 1000.0,
            ch2_low_v=self.ch2_low.value(),
            ch2_high_v=self.ch2_high.value(),
            ch2_idle_level=self.ch2_idle_combo.currentText(),
            output_load=self.load_combo.currentText(),
        )

    def _save_settings(self) -> None:
        self._settings.setValue("resource", self.resource_combo.currentText().strip())
        self._settings.setValue("ch1/freq_mhz", self.ch1_freq.value())
        self._settings.setValue("ch1/vpp", self.ch1_vpp.value())
        self._settings.setValue("ch1/offset_v", self.ch1_offset.value())
        self._settings.setValue("ch1/phase_deg", self.ch1_phase.value())
        self._settings.setValue("ch2/width_ms", self.ch2_width.value())
        self._settings.setValue(
            "ch2/after_sine_delay_ms", self.ch2_after_sine_delay.value()
        )
        self._settings.setValue("ch2/pulses_per_cycle", self.ch2_pulses_per_cycle.value())
        self._settings.setValue("ch2/pulse_interval_ms", self.ch2_pulse_interval.value())
        self._settings.setValue("ch2/low_v", self.ch2_low.value())
        self._settings.setValue("ch2/high_v", self.ch2_high.value())
        self._settings.setValue("ch2/idle_level", self.ch2_idle_combo.currentText())
        self._settings.setValue("common/load", self.load_combo.currentText())
        self._settings.setValue("common/cycle_period_ms", self.cycle_period_s.value())
        self._settings.setValue("common/sine_ratio_pct", self.sine_ratio_pct.value())

    def _setting_float(self, key: str, default: float) -> float:
        value = self._settings.value(key, default)
        try:
            return float(value)
        except (TypeError, ValueError):
            return default

    def _setting_int(self, key: str, default: int) -> int:
        value = self._settings.value(key, default)
        try:
            return int(value)
        except (TypeError, ValueError):
            return default

    def _load_settings(self) -> None:
        self.resource_combo.setEditText(str(self._settings.value("resource", "")))
        freq_mhz = self._setting_float("ch1/freq_mhz", -1.0)
        if freq_mhz <= 0:
            freq_hz = self._setting_float("ch1/freq_hz", self.ch1_freq.value() * 1_000_000.0)
            freq_mhz = freq_hz / 1_000_000.0
        self.ch1_freq.setValue(freq_mhz)
        self.ch1_vpp.setValue(self._setting_float("ch1/vpp", self.ch1_vpp.value()))
        self.ch1_offset.setValue(self._setting_float("ch1/offset_v", self.ch1_offset.value()))
        self.ch1_phase.setValue(self._setting_float("ch1/phase_deg", self.ch1_phase.value()))

        width_ms = self._setting_float("ch2/width_ms", -1.0)
        if width_ms < 0:
            width_s = self._setting_float("ch2/width_s", self.ch2_width.value() / 1000.0)
            width_ms = width_s * 1000.0
        self.ch2_width.setValue(width_ms)

        self.ch2_after_sine_delay.setValue(
            self._setting_float("ch2/after_sine_delay_ms", self.ch2_after_sine_delay.value())
        )
        pulses_per_cycle = self._setting_int("ch2/pulses_per_cycle", 1)
        self.ch2_pulses_per_cycle.setValue(max(1, min(1_000_000, pulses_per_cycle)))
        self.ch2_pulse_interval.setValue(
            self._setting_float("ch2/pulse_interval_ms", self.ch2_pulse_interval.value())
        )

        self.ch2_low.setValue(self._setting_float("ch2/low_v", self.ch2_low.value()))
        self.ch2_high.setValue(self._setting_float("ch2/high_v", self.ch2_high.value()))
        self.ch2_idle_combo.setCurrentText(str(self._settings.value("ch2/idle_level", "BOTT")))
        self.load_combo.setCurrentText(str(self._settings.value("common/load", "INF")))
        cycle_period_ms = self._setting_float("common/cycle_period_ms", -1.0)
        if cycle_period_ms < 0:
            cycle_period_s = self._setting_float(
                "common/cycle_period_s", self.cycle_period_s.value() / 1000.0
            )
            cycle_period_ms = cycle_period_s * 1000.0
        self.cycle_period_s.setValue(cycle_period_ms)
        self.sine_ratio_pct.setValue(
            self._setting_float("common/sine_ratio_pct", self.sine_ratio_pct.value())
        )

    @Slot()
    def start_cycle(self) -> None:
        if not self._require_connected():
            return
        cfg = self._read_config()
        on_ms, off_ms = self._calc_cycle_ms()
        self.cycle_prepare_requested.emit(cfg, on_ms, off_ms)

    def _calc_cycle_ms(self) -> tuple[int, int]:
        period_ms = max(1, int(self.cycle_period_s.value()))
        ratio = self.sine_ratio_pct.value() / 100.0
        on_ms = int(period_ms * ratio)
        off_ms = period_ms - on_ms
        # 避免 0ms 定时导致无法观察切换；极端占比时强制最小 1ms。
        if on_ms <= 0:
            on_ms = 1
            off_ms = max(1, period_ms - on_ms)
        elif off_ms <= 0:
            off_ms = 1
            on_ms = max(1, period_ms - off_ms)
        return on_ms, off_ms

    def _require_connected(self) -> bool:
        if not self._instrument_connected:
            QMessageBox.warning(self, "未连接", "请先连接设备。")
            return False
        return True

    @Slot(str)
    def _on_cycle_prepare_failed(self, message: str) -> None:
        self._cycle_running = False
        self._cycle_timer.stop()
        self._append_log(f"启动循环失败: {message}")
        QMessageBox.critical(self, "启动失败", message)

    @Slot(str)
    def _on_cycle_started(self, line: str) -> None:
        self._cycle_running = True
        self._cycle_outputs_on = True
        on_ms, _ = self._calc_cycle_ms()
        self._cycle_timer.start(on_ms)
        self._append_log(line)

    @Slot()
    def _on_cycle_timer(self) -> None:
        if not self._cycle_running:
            return
        on_ms, off_ms = self._calc_cycle_ms()
        self.cycle_edge_requested.emit(self._cycle_outputs_on, on_ms, off_ms)

    @Slot(bool, int, str)
    def _on_cycle_edge_done(self, next_on: bool, delay_ms: int, line: str) -> None:
        self._cycle_outputs_on = bool(next_on)
        self._append_log(line)
        if self._cycle_running:
            self._cycle_timer.start(delay_ms)

    @Slot(str)
    def _on_cycle_edge_failed(self, message: str) -> None:
        self._cycle_running = False
        self._cycle_timer.stop()
        self._append_log(f"周期输出异常，已停止: {message}")
        QMessageBox.critical(self, "运行异常", message)

    @Slot()
    def _on_stop_clicked(self) -> None:
        if not self._require_connected():
            return
        self._cycle_running = False
        self._cycle_timer.stop()
        QMetaObject.invokeMethod(
            self._worker,
            "stop_cycle_outputs",
            Qt.ConnectionType.QueuedConnection,
        )

    @Slot()
    def _on_test_pulse_clicked(self) -> None:
        if not self._require_connected():
            return
        QMetaObject.invokeMethod(
            self._worker,
            "test_ch2_pulse",
            Qt.ConnectionType.QueuedConnection,
        )

    @Slot()
    def _on_test_square_clicked(self) -> None:
        if not self._require_connected():
            return
        QMetaObject.invokeMethod(
            self._worker,
            "test_ch2_square",
            Qt.ConnectionType.QueuedConnection,
        )

    def closeEvent(self, event) -> None:  # type: ignore[override]
        self._save_settings()
        self._cycle_running = False
        self._cycle_timer.stop()

        # 若在这里直接 thread.wait() 阻塞主线程，则排队的 thread.quit()（由 shutdown_complete 触发）
        # 无法被处理，会形成死锁，随后 terminate() 极易导致崩溃。用局部事件循环等待线程结束。
        wait_loop = QEventLoop(self)
        self._thread.finished.connect(wait_loop.quit)

        QMetaObject.invokeMethod(
            self._worker,
            "shutdown",
            Qt.ConnectionType.QueuedConnection,
        )

        safety = QTimer(self)
        safety.setSingleShot(True)
        safety.timeout.connect(wait_loop.quit)
        safety.start(15000)
        wait_loop.exec()
        safety.stop()

        if self._thread.isRunning():
            self._thread.quit()
            if not self._thread.wait(5000):
                log.warning(
                    "工作线程在关闭窗口后仍未退出（可能 VISA 关闭阻塞）。"
                    "请勿对 QThread 使用 terminate，以免崩溃；可检查仪器连接或驱动。"
                )

        super().closeEvent(event)
