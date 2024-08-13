from PySide6.QtCore import QCoreApplication

# Если текст не будет совпадать с текстом из файлов .ts тега <source> то локализация работать не будет.
class Texts:
    @property
    def main_window_title(self):
        return QCoreApplication.translate("MainWindow", "Default. Имя Моего Окна")

    @property
    def label_text(self):
        return QCoreApplication.translate("MainWindow", "Default. Это пример текста, который нужно перевести.")

