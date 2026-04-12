# PyInstaller：onedir + 排除误收集的大库。
# 产物目录使用 ASCII 名 DG2000Trigger，避免 Windows/解压工具对中文路径不友好。
# macOS 保持 upx=False；Windows 可尝试 upx=True（需本机安装 UPX，未安装则不影响构建）。
# 依赖请使用 PySide6-Essentials（显著小于完整 PySide6）。

block_cipher = None
is_win = sys.platform.startswith("win")

a = Analysis(
    ["dg2000_trigger/__main__.py"],
    pathex=["."],
    binaries=[],
    datas=[],
    hiddenimports=[
        "pyvisa_py",
        "pyvisa_py.highlevel",
        "pyvisa_py.usb",
        "pyvisa_py.protocols",
        "usb.backend.libusb1",
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        "matplotlib",
        "numpy",
        "pandas",
        "scipy",
        "PIL",
        "cv2",
        "torch",
        "IPython",
        "jupyter",
        "PySide6.QtWebEngineCore",
        "PySide6.QtWebEngineWidgets",
        "PySide6.QtWebEngineQuick",
        "PySide6.Qt3DCore",
        "PySide6.Qt3DRender",
        "PySide6.Qt3DInput",
        "PySide6.Qt3DLogic",
        "PySide6.Qt3DAnimation",
        "PySide6.Qt3DExtras",
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="DG2000Trigger",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=is_win,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=is_win,
    upx_exclude=[],
    name="DG2000Trigger",
)
