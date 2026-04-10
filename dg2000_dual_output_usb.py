"""
DG2000 USB 双通道输出示例（Python + PyVISA）

功能:
1) CH1 输出可调正弦波
2) CH2 同时输出 0~5V 方波脉冲（用于与采集器通信）

使用前准备:
- 安装 Python 3
- 安装 pyvisa: pip install pyvisa
- 安装 VISA 运行库（例如 NI-VISA）
- 通过 USB 连接波形发生器
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from typing import Optional

import pyvisa


@dataclass
class Config:
    # 连接参数
    resource_name: str = ""  # 留空自动选择第一个 USB 设备
    do_reset: bool = False    # True: 连接后执行 *RST

    # CH1: 正弦波参数
    ch1_freq_hz: float = 1000.0
    ch1_vpp: float = 2.0
    ch1_offset_v: float = 0.0
    ch1_phase_deg: float = 0.0

    # CH2: 脉冲参数（0~5V）
    ch2_pulse_freq_hz: float = 1000.0
    ch2_pulse_width_s: float = 100e-6
    ch2_low_v: float = 0.0
    ch2_high_v: float = 5.0

    # 输出负载设置: "INF"(高阻) 或 "50"
    output_load: str = "INF"

    # VISA 超时（毫秒）
    timeout_ms: int = 8000


def choose_resource(rm: pyvisa.ResourceManager, resource_name: str) -> str:
    """自动选择资源：优先 USB，其次任意 INSTR。"""
    if resource_name.strip():
        return resource_name.strip()

    resources = rm.list_resources()
    if not resources:
        raise RuntimeError("未发现 VISA 设备。请确认已安装 VISA 运行库并连接仪器。")

    usb_candidates = [r for r in resources if "USB" in r.upper() and r.upper().endswith("INSTR")]
    if usb_candidates:
        selected = usb_candidates[0]
        print(f"自动选择资源(USB): {selected}")
        return selected

    instr_candidates = [r for r in resources if r.upper().endswith("INSTR")]
    if instr_candidates:
        selected = instr_candidates[0]
        print(f"自动选择资源(INSTR): {selected}")
        return selected

    selected = resources[0]
    print(f"自动选择资源(首个): {selected}")
    return selected


def print_visa_resources(rm: pyvisa.ResourceManager) -> tuple[str, ...]:
    """打印当前可见的 VISA 资源，便于排查连接问题。"""
    resources = rm.list_resources()
    print("VISA 资源列表:")
    if not resources:
        print("  (空)")
    else:
        for idx, res in enumerate(resources, start=1):
            print(f"  {idx}. {res}")
    return resources


def print_pyusb_devices() -> None:
    """打印系统可见的 USB 设备摘要（需要 pyusb）。"""
    try:
        import usb.core  # type: ignore
    except Exception:
        print("USB 设备摘要: 未安装 pyusb，跳过。")
        return

    devices = list(usb.core.find(find_all=True))
    print("USB 设备摘要:")
    if not devices:
        print("  (未发现可枚举 USB 设备)")
        return

    for dev in devices:
        vid = f"0x{dev.idVendor:04x}"
        pid = f"0x{dev.idProduct:04x}"
        print(f"  VID={vid}, PID={pid}")


def query_idn(dev) -> str:
    return dev.query("*IDN?").strip()


def setup_outputs(dev, cfg: Config) -> None:
    # 先关输出，避免参数切换时误触发
    dev.write(":OUTP1 OFF")
    dev.write(":OUTP2 OFF")

    # 通道负载模式
    dev.write(f":OUTP1:LOAD {cfg.output_load}")
    dev.write(f":OUTP2:LOAD {cfg.output_load}")

    # CH1: 正弦波
    dev.write(
        f":SOUR1:APPL:SIN {cfg.ch1_freq_hz:.12g},{cfg.ch1_vpp:.12g},{cfg.ch1_offset_v:.12g}"
    )
    dev.write(f":SOUR1:PHAS {cfg.ch1_phase_deg:.12g}")

    # CH2: 脉冲波（0~5V）
    dev.write(":SOUR2:FUNC PULS")
    dev.write(f":SOUR2:FREQ {cfg.ch2_pulse_freq_hz:.12g}")
    dev.write(f":SOUR2:PULS:WIDT {cfg.ch2_pulse_width_s:.12g}")
    dev.write(f":SOUR2:VOLT:LOW {cfg.ch2_low_v:.12g}")
    dev.write(f":SOUR2:VOLT:HIGH {cfg.ch2_high_v:.12g}")

    # 连续输出模式
    dev.write(":SOUR1:BURS:STAT OFF")
    dev.write(":SOUR2:BURS:STAT OFF")

    # 开启两个通道
    dev.write(":OUTP1 ON")
    dev.write(":OUTP2 ON")


def stop_outputs(dev) -> None:
    """关闭两个通道输出。"""
    dev.write(":OUTP1 OFF")
    dev.write(":OUTP2 OFF")


def start_outputs(dev) -> None:
    """开启两个通道输出。"""
    dev.write(":OUTP1 ON")
    dev.write(":OUTP2 ON")


def try_return_to_local(dev) -> None:
    """尝试释放远程控制，恢复面板可操作状态。"""
    # 不同型号命令兼容性有差异，逐个尝试，失败不影响主流程。
    for cmd in (":SYST:KLOC OFF", ":SYST:LOC", "SYST:KLOC OFF", "SYST:LOC"):
        try:
            dev.write(cmd)
        except Exception:
            continue


def run(cfg: Optional[Config] = None, stop_only: bool = False) -> None:
    cfg = cfg or Config()

    rm = pyvisa.ResourceManager()
    print_visa_resources(rm)
    resource = choose_resource(rm, cfg.resource_name)

    dev = rm.open_resource(resource)
    try:
        # 和 MATLAB 配置一致：LF 结尾 + 8 秒超时
        dev.read_termination = "\n"
        dev.write_termination = "\n"
        dev.timeout = cfg.timeout_ms

        idn = query_idn(dev)
        print(f"已连接设备: {idn}")

        dev.write("*CLS")
        if cfg.do_reset:
            dev.write("*RST")

        if stop_only:
            stop_outputs(dev)
            print("已停止 CH1/CH2 输出。")
        else:
            setup_outputs(dev, cfg)
            print(
                f"CH1 正弦波已开启: f={cfg.ch1_freq_hz:.3f} Hz, "
                f"Vpp={cfg.ch1_vpp:.3f} V, Offset={cfg.ch1_offset_v:.3f} V"
            )
            print(
                f"CH2 脉冲已开启: f={cfg.ch2_pulse_freq_hz:.3f} Hz, "
                f"Width={cfg.ch2_pulse_width_s:.6g} s, "
                f"Low={cfg.ch2_low_v:.3f} V, High={cfg.ch2_high_v:.3f} V"
            )

        err = dev.query(":SYST:ERR?").strip()
        print(f"设备状态: {err}")

    finally:
        try_return_to_local(dev)
        # 始终释放资源，避免 VISA 占用
        dev.close()
        rm.close()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="DG2000 双通道输出控制脚本")
    parser.add_argument(
        "--list",
        action="store_true",
        help="仅打印可发现的 VISA 资源和 USB 设备摘要，不下发 SCPI 命令。",
    )
    parser.add_argument(
        "--stop",
        action="store_true",
        help="停止 CH1/CH2 输出（用户手动停止）。",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    try:
        if args.list:
            rm = pyvisa.ResourceManager()
            try:
                print_visa_resources(rm)
            finally:
                rm.close()
            print_pyusb_devices()
            raise SystemExit(0)

        run(Config(), stop_only=args.stop)
    except Exception as exc:
        print(f"执行失败: {exc}")
        print("以下为诊断信息:")
        try:
            rm_diag = pyvisa.ResourceManager()
            try:
                print_visa_resources(rm_diag)
            finally:
                rm_diag.close()
        except Exception as diag_exc:
            print(f"VISA 资源诊断失败: {diag_exc}")

        print_pyusb_devices()
        print("建议检查: Python 依赖、VISA 运行库、USB 连接、resource_name 是否正确。")
