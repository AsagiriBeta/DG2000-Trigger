# 构建与分发（macOS / Windows）

## 重要结论

1. **无法在一台 Mac 上交叉编译出 Windows 的 `.exe`**。PyInstaller 必须在目标操作系统上运行。可行做法：
   - 在 **Windows 电脑或虚拟机** 上运行 `scripts/build_pyinstaller.ps1`；
   - 或使用本仓库 **GitHub Actions**（`PyInstaller build` 工作流）：在 `macos-latest` 与 `windows-latest` 上各打一份包，在 Actions 页面下载 Artifact。
2. **M4 MacBook Pro** 上本地构建得到的是 **macOS arm64** 应用；若需 **Intel macOS**，需在 Intel Mac 或 CI 上指定/配置对应架构（本工作流未单独产出 universal2）。

## 减小体积的依赖选择

- 运行与打包请使用 **`PySide6-Essentials`**（已在 `requirements.txt` / `pyproject.toml` 中配置）。与完整 `PySide6` 相比可明显减小安装与打包体积，本项目仅使用 `QtWidgets`/`QtCore`，无需 WebEngine 等大组件。
- 产物目录名为 **`DG2000Trigger`**（ASCII），避免 Windows 与部分解压工具对中文路径不友好。窗口标题仍为中文「DG2000 控制台」。

## 本地构建（conda：`lab-usb-instr`）

在仓库根目录执行：

```bash
conda activate lab-usb-instr
# 若尚未同步依赖：
pip install -U pip
pip install -r requirements.txt
pip install ".[build]"

# macOS：
./scripts/build_pyinstaller.sh
# 或：python -m PyInstaller --noconfirm --clean dg2000_trigger.spec
```

生成目录：`dist/DG2000Trigger/`（macOS 下运行其中的可执行文件）。

Windows 本机：

```powershell
conda activate lab-usb-instr
Set-ExecutionPolicy -Scope Process Bypass
.\scripts\build_pyinstaller.ps1
```

生成：`dist\DG2000Trigger\DG2000Trigger.exe`。

## 开发时如何调试（不必反复安装打包软件）

日常改代码请**始终用源码 + conda 环境**跑 GUI，用 IDE 断点调试；**只有**在验证「分发形态」或他人机器环境时，才需要打 PyInstaller 包。

1. **激活环境并启动**

   ```bash
   conda activate lab-usb-instr
   cd /path/to/DG2000-Trigger
   python -m dg2000_trigger
   ```

   等价：`python dg2000_gui.py`。

2. **可选：终端里看更细的日志**（VISA/线程排障）

   ```bash
   export DG2000_DEBUG=1   # Windows CMD: set DG2000_DEBUG=1
   python -m dg2000_trigger
   ```

3. **在 Cursor / VS Code 里断点调试**  
   选好解释器为 `lab-usb-instr`，在本机创建 `.vscode/launch.json`（该目录已加入 `.gitignore`，不会提交）。示例：

   ```json
   {
     "version": "0.2.0",
     "configurations": [
       {
         "name": "DG2000 Trigger",
         "type": "debugpy",
         "request": "launch",
         "module": "dg2000_trigger",
         "cwd": "${workspaceFolder}",
         "console": "integratedTerminal",
         "justMyCode": true
       },
       {
         "name": "DG2000 Trigger（详细日志）",
         "type": "debugpy",
         "request": "launch",
         "module": "dg2000_trigger",
         "cwd": "${workspaceFolder}",
         "console": "integratedTerminal",
         "justMyCode": true,
         "env": { "DG2000_DEBUG": "1" }
       }
     ]
   }
   ```

4. **可编辑安装（改代码立刻生效）**

   ```bash
   pip install -e .
   ```

   之后仍用 `python -m dg2000_trigger` 即可，无需每次 `pip install .`。

### 已经打过 PyInstaller 时，如何「更新」而不卸载重装？

当前产物是 **onedir 文件夹** `dist/DG2000Trigger/`，本质是**可拷贝的一整包**，没有系统级「安装程序」时，**不需要卸载**：

- **macOS / Windows**：重新构建后，用新输出的 **`dist/DG2000Trigger` 整个目录覆盖**旧目录即可（先退出正在运行的程序再覆盖）。
- 若你把应用拷到 **「应用程序」** 或固定路径：同样用**新构建的整包覆盖**该目录下的同名内容即可。

若以后做成 **`.dmg` / 安装向导**，更新逻辑仍是「退出应用 → 替换应用包或安装目录」；与「删干净再装」相比，**优先用覆盖同路径**即可。

## GitHub Actions

1. 将本仓库推送到 GitHub。
2. 打开 **Actions** → **PyInstaller build** → **Run workflow**。
3. 完成后在 **Artifacts** 中下载 `DG2000Trigger-macos-arm64` 与 `DG2000Trigger-windows-x64`（zip）。

## 对外分发提示

- **macOS**：若要给他人安装，通常需要 **代码签名 + 公证（Notarization）**，否则 Gatekeeper 可能拦截；签名需 Apple Developer 账号与 `codesign`/`notarytool` 流程（此处不展开）。
- **Windows**：部分杀毒软件可能对 PyInstaller 引导程序误报；可选购代码签名证书对 `exe` 签名以降低误报率。
- **USB / VISA**：打包只解决「不装 Python」；目标机仍需 **USB 驱动 / VISA 或 pyvisa-py 所需运行环境** 才能枚举仪器。
