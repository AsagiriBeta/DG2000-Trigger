# Build and Release (macOS / Windows)

This document describes how to build and distribute DG2000 Trigger with PyInstaller.

## Platform Scope

- PyInstaller builds are platform-specific.
- Build macOS artifacts on macOS.
- Build Windows artifacts on Windows.
- A single macOS host cannot produce a Windows `.exe`.

## Prerequisites

- Conda environment: `lab-usb-instr`
- Dependencies installed from `requirements.txt`
- Build extras installed via `.[build]`

```bash
conda activate lab-usb-instr
pip install -U pip
pip install -r requirements.txt
pip install ".[build]"
```

## Local Build

### macOS

```bash
./scripts/build_pyinstaller.sh
```

Output:
- `dist/DG2000Trigger/`

### Windows

```powershell
conda activate lab-usb-instr
Set-ExecutionPolicy -Scope Process Bypass
.\scripts\build_pyinstaller.ps1
```

Output:
- `dist\DG2000Trigger\DG2000Trigger.exe`

## CI Build (GitHub Actions)

Use the `PyInstaller build` workflow to generate release artifacts for both platforms:

1. Open **Actions** in GitHub.
2. Run **PyInstaller build**.
3. Download artifacts from the completed run.

## Architecture Notes

- Builds on Apple Silicon produce macOS `arm64` artifacts.
- Intel macOS artifacts must be built on an Intel runner/host.
- Universal2 is not produced by default in this repository.

## Development vs Packaging

For daily development, run from source:

```bash
python -m dg2000_trigger
```

Use PyInstaller only for distribution validation and external delivery.

## Distribution Considerations

- **macOS**: signing and notarization may be required for end users (Gatekeeper).
- **Windows**: unsigned executables may trigger antivirus warnings.
- **Instrument I/O**: target machines still require compatible USB/VISA runtime and drivers.
