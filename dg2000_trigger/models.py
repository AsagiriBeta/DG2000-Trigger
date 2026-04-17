from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class OutputConfig:
    """仪器波形与负载参数（不可变，便于跨线程传递）。"""

    ch1_freq_hz: float
    ch1_vpp: float
    ch1_offset_v: float
    ch1_phase_deg: float
    ch2_pulse_width_s: float
    ch2_after_sine_delay_s: float
    ch2_pulses_per_cycle: int
    ch2_pulse_interval_s: float
    ch2_low_v: float
    ch2_high_v: float
    ch2_idle_level: str
    ch1_output_load: str
    ch2_output_load: str
