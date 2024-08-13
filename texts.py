from PySide6.QtCore import QCoreApplication

class Texts:
    @property
    def main_window_title(self):
        return QCoreApplication.translate("MainWindow", "main_window_title")

    @property
    def label_text(self):
        return QCoreApplication.translate("MainWindow", "label_text")

