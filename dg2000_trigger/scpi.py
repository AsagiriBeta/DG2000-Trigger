from __future__ import annotations

import math
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
    for cmd in (":SOUR2:BURS:TRIG", "*TRG"):
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
    # 单次触发 N=1 时频率不决定触发次数，这里固定为安全值，避免界面暴露误导参数。
    dev.write(":SOUR2:FREQ 1000")
    dev.write(f":SOUR2:PULS:WIDT {cfg.ch2_pulse_width_s:.12g}")
    dev.write(f":SOUR2:PULS:DEL {cfg.ch2_delay_s:.12g}")
    dev.write(f":SOUR2:VOLT:LOW {cfg.ch2_low_v:.12g}")
    dev.write(f":SOUR2:VOLT:HIGH {cfg.ch2_high_v:.12g}")

    dev.write(":SOUR1:BURS:STAT OFF")
    dev.write(":SOUR2:BURS:STAT ON")
    dev.write(":SOUR2:BURS:MODE TRIG")
    dev.write(":SOUR2:BURS:NCYC 1")
    # DG2000 手册定义触发源为 INT/EXT/MAN，不支持 BUS。
    for cmd in (":SOUR2:BURS:TRIG:SOUR MAN",):
        try:
            dev.write(cmd)
            break
        except Exception:
            continue
    # 机型支持时，设置触发间隙空闲电平（BOTT/TOP），减少空闲态跳变。
    try:
        dev.write(f":SOUR2:BURS:IDLE {cfg.ch2_idle_level}")
    except Exception:
        pass


def configure_ch1_burst_cycle(
    dev: ScpiWriter, cfg: OutputConfig, on_s: float, off_s: float
) -> tuple[int, float, float]:
    """将 CH1 配置为手动触发 Burst；每次触发输出一段正弦。"""
    req_period_s = max(1e-6, on_s + off_s)
    freq = max(1e-9, cfg.ch1_freq_hz)
    req_cycles = max(1.0, on_s * freq)
    ncyc = max(1, int(math.floor(req_cycles + 0.5)))
    burst_on_s = ncyc / freq

    dev.write(":SOUR1:BURS:MODE TRIG")
    dev.write(":SOUR1:BURS:TRIG:SOUR MAN")
    dev.write(f":SOUR1:BURS:NCYC {ncyc}")
    dev.write(":SOUR1:BURS:TDEL 0")
    dev.write(":SOUR1:BURS:STAT ON")
    return ncyc, burst_on_s, req_period_s


def format_cycle_start_log(cfg: OutputConfig, on_s: float, off_s: float, syst_err: str) -> str:
    return (
        "循环已开始: "
        f"CH1 {cfg.ch1_freq_hz:.3f}Hz/{cfg.ch1_vpp:.3f}Vpp, "
        f"CH2 脉宽 {cfg.ch2_pulse_width_s:.6g}s,"
        f"延时 {cfg.ch2_delay_s:.6g}s,空闲 {cfg.ch2_idle_level}, "
        f"发波 {on_s:.3f}s / 停波 {off_s:.3f}s, "
        f"设备状态 {syst_err}"
    )
