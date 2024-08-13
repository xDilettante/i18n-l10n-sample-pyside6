import os
import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QComboBox
from PySide6.QtCore import QTranslator, QCoreApplication

from texts import Texts

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.texts = Texts()

        self.layout = QVBoxLayout()

        self.label = QLabel()
        self.layout.addWidget(self.label)

        self.language_selector = QComboBox()
        self.language_selector.addItem("Русский", "ru_RU")
        self.language_selector.addItem("English", "en_US")
        self.language_selector.addItem("Deutsch", "de_DE")
        self.language_selector.currentIndexChanged.connect(self.change_language_by_index)
        self.layout.addWidget(self.language_selector)

        self.setLayout(self.layout)

        self.translator = QTranslator()
        self.change_language("ru_RU")

    def change_language_by_index(self, index):
        lang_code = self.language_selector.itemData(index)
        self.change_language(lang_code)

    def change_language(self, lang_code):
        qm_file = f"translations/{lang_code}.qm"
        qm_path = os.path.join(os.path.dirname(__file__), qm_file)

        if self.translator.load(qm_path):
            app.installTranslator(self.translator)
            self.update_ui()
        else:
            print(f"Не удалось загрузить перевод: {qm_path}")

    def update_ui(self):
        # Обновляем интерфейс с использованием свойств класса Texts
        self.label.setText(self.texts.label_text)
        self.setWindowTitle(self.texts.main_window_title)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())

