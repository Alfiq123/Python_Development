# Line Edit

from sys import argv, exit
## from PyQt5.QtCore import Qt
## from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QApplication,
    ## QCheckBox,
    ## QComboBox,
    ## QDoubleSpinBox,
    ## QLabel,
    QLineEdit,
    ## QListWidget,
    QMainWindow,
    ## QSlider,
    ## QSpinBox,
)


# noinspection PyUnresolvedReferences
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = QLineEdit()
        widget.setMaxLength(10)
        widget.setPlaceholderText("Enter your text")

        ## Set Text Read Only
        # widget.setReadOnly(True) # uncomment this to make it read-only

        widget.returnPressed.connect(self.return_pressed)
        widget.selectionChanged.connect(self.selection_changed)
        widget.textChanged.connect(self.text_changed)
        widget.textEdited.connect(self.text_edited)

        ## Input Mask
        # widget.setInputMask("000.000.000.000;_")

        self.setCentralWidget(widget)

    def return_pressed(self):
        print("Return pressed!")
        self.centralWidget().setText("BOOM!")

    def selection_changed(self):
        print("Selection changed")
        print(self.centralWidget().selectedText())

    @staticmethod
    def text_changed(s):
        print("Text changed...")
        print(s)

    @staticmethod
    def text_edited(s):
        print("Text edited...")
        print(s)


if __name__ == "__main__":
    app = QApplication(argv)

    window = MainWindow()
    window.show()

    exit(app.exec())
