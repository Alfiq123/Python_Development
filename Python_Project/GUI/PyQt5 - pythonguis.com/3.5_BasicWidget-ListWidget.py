# QListWidget

from sys import argv, exit
## from PyQt5.QtCore import Qt
## from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QApplication,
    ## QCheckBox,
    ## QComboBox,
    ## QDoubleSpinBox,
    ## QLabel,
    ## QLineEdit,
    QListWidget,
    QMainWindow,
    ## QSlider,
    ## QSpinBox,
)


# noinspection PyUnresolvedReferences
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = QListWidget()
        widget.addItems(["One", "Two", "Three", "Four", "Five"])

        widget.currentItemChanged.connect(self.index_changed)
        widget.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(widget)

    @staticmethod
    def index_changed(i):  # Not an index, "i" is a QListWidgetItem
        print(i.text())

    @staticmethod
    def text_changed(s):  # s is a str
        print(s)


if __name__ == "__main__":
    app = QApplication(argv)

    window = MainWindow()
    window.show()

    exit(app.exec())
