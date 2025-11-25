# QSpinBox and QDoubleSpinBox

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
    ## QListWidget,
    QMainWindow,
    ## QSlider,
    QSpinBox,
    QDoubleSpinBox
)


# noinspection PyUnresolvedReferences
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = QSpinBox()
        # widget = QDoubleSpinBox()

        widget.setMinimum(-10)
        widget.setMaximum(3)
        # widget.setRange(-10, 3)

        widget.setPrefix("$")
        widget.setSuffix("c")
        widget.setSingleStep(3)
        # widget.setSingleStep(0.5)

        widget.valueChanged.connect(self.value_changed)
        widget.textChanged.connect(self.value_changed_str)

        widget.lineEdit().setReadOnly(True)

        self.setCentralWidget(widget)

    @staticmethod
    def value_changed(i): print(i)

    @staticmethod
    def value_changed_str(s): print(s)


if __name__ == "__main__":
    app = QApplication(argv)

    window = MainWindow()
    window.show()

    exit(app.exec())
