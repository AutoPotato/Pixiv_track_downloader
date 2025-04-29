import importlib.resources
import pathlib

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow, QLabel

import pixiv_track_downloader as sdk


class QMainWindowExt(QMainWindow):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        # self.main_window_model: ui_model.MainWindowModel = ui_model.MainWindowModel()

    def set_up(self) -> None:
        self.setWindowTitle(f"Pixiv Track Downloader {sdk.VERSION}")
        app_icon: pathlib.Path
        with importlib.resources.path(__package__, 'main_window.ico') as app_icon:
            self.setWindowIcon(QIcon(str(app_icon)))

        self.add_link_icon_label: QLabel = getattr(self, 'add_link_icon_label')
