#!/usr/bin/env bash
# 默认：PyInstaller + onedir（见 ../dg2000_trigger.spec，已 excludes 常见科学计算大包）。
#
# 若追求更小体积（权衡开发成本与体验）：
# - PySide6/Qt 本体仍占大头；可评估 Nuitka（构建更慢，有时体积更优）或商业裁剪方案。
# - 将界面改为 Tkinter + PyVISA 通常显著小于 Qt，但需重写 UI。
# - 无界面 CLI / TUI（如 Textual）体积更小，适合熟练用户。
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

python3 -m pip install -U pip
python3 -m pip install ".[build]"
python3 -m PyInstaller --noconfirm --clean dg2000_trigger.spec

echo "产物目录: $ROOT/dist/DG2000Trigger"
