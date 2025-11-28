from sys import argv, exit
## from PySide6.QtCore import Qt
## from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QApplication,
    ## QCheckBox,
    ## QComboBox,
    ## QDoubleSpinBox,
    ## QLabel,
    ## QLineEdit,
    ## QListWidget,
    QMainWindow,
    ## QSlider,
    ## QSpinBox,
    QDial
)


# noinspection PyUnresolvedReferences
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = QDial()
        widget.setRange(-10, 100)
        widget.setSingleStep(1)

        widget.valueChanged.connect(self.value_changed)
        widget.sliderMoved.connect(self.slider_position)
        widget.sliderPressed.connect(self.slider_pressed)
        widget.sliderReleased.connect(self.slider_released)

        self.setCentralWidget(widget)

    @staticmethod
    def value_changed(i): print(i)

    @staticmethod
    def slider_position(p): print("position", p)

    @staticmethod
    def slider_pressed(): print("Pressed!")

    @staticmethod
    def slider_released(): print("Released")


if __name__ == "__main__":
    app = QApplication(argv)

    window = MainWindow()
    window.show()

    exit(app.exec())
