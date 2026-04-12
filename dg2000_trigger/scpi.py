from __future__ import annotations

from typing import Protocol, runtime_checkable

from dg2000_trigger.models import OutputConfig


@runtime_checkable
class ScpiWriter(Protocol):
    """最小 SCPI 写入接口（便于测试与类型检查）。"""

    def write(self, command: str) -> None: ...

    def query(self, command: str) -> str: ...


def try_return_to_local(dev: ScpiWriter) -> None:
    """尝试切回本地面板；不同机型命令略有差异。"""
    for cmd in (":SYST:KLOC OFF", ":SYST:LOC", "SYST:KLOC OFF", "SYST:LOC"):
        try:
            dev.write(cmd)
        except Exception:
            continue


def try_emit_single_pulse(dev: ScpiWriter) -> None:
    """在 CH2 上触发一次单脉冲（设备间同步）。"""
    for cmd in (":SOUR2:BURS:TRIG", "SOUR2:BURS:TRIG", "*TRG"):
        try:
            dev.write(cmd)
            return
        except Exception:
            continue


def configure_outputs(dev: ScpiWriter, cfg: OutputConfig) -> None:
    """按界面配置写入波形与触发模式（不打开输出）。"""
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

    dev.write(":SOUR1:BURS:STAT OFF")
    dev.write(":SOUR2:BURS:STAT ON")
    dev.write(":SOUR2:BURS:MODE TRIG")
    dev.write(":SOUR2:BURS:NCYC 1")
    dev.write(":SOUR2:BURS:TRIG:SOUR BUS")


def format_cycle_start_log(cfg: OutputConfig, on_s: float, off_s: float, syst_err: str) -> str:
    return (
        "循环已开始: "
        f"CH1 {cfg.ch1_freq_hz:.3f}Hz/{cfg.ch1_vpp:.3f}Vpp, "
        f"CH2 {cfg.ch2_pulse_freq_hz:.3f}Hz/{cfg.ch2_pulse_width_s:.6g}s, "
        f"发波 {on_s:.3f}s / 停波 {off_s:.3f}s, "
        f"设备状态 {syst_err}"
    )
