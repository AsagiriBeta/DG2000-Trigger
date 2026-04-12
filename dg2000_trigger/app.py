from __future__ import annotations

import logging
import os
import sys

from PySide6.QtWidgets import QApplication

from dg2000_trigger.ui.main_window import MainWindow


def main() -> int:
    debug = bool(os.environ.get("DG2000_DEBUG", "").strip())
    level = logging.DEBUG if debug else logging.INFO
    logging.basicConfig(level=level, format="%(levelname)s %(name)s: %(message)s")
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = MainWindow()
    window.show()
    return app.exec()
