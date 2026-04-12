# Windows 本机打包（需在 Windows 上安装 Python/conda 与项目依赖）
$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
Set-Location $Root

python -m pip install -U pip
python -m pip install ".[build]"
python -m PyInstaller --noconfirm --clean dg2000_trigger.spec

Write-Host "输出目录: $Root\dist\DG2000Trigger"
Write-Host "运行: dist\DG2000Trigger\DG2000Trigger.exe"
