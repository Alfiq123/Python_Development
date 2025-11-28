from sys import argv, exit
# noinspection PyUnusedImports
from PySide6.QtCore import Qt
# noinspection PyUnusedImports
from PySide6.QtGui import QPixmap
# noinspection PyUnusedImports
from PySide6.QtWidgets import (
    QApplication, QCheckBox, QComboBox, QDoubleSpinBox, QLabel,
    QLineEdit, QListWidget, QMainWindow, QSlider, QSpinBox,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")


if __name__ == "__main__":
    app = QApplication(argv)

    window = MainWindow()
    window.show()

    exit(app.exec())
