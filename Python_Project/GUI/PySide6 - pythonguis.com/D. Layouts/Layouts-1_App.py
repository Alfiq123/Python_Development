# Layouts

## Layout        ## Behaviour
# QHBoxLayout    : Linear horizontal layout
# QVBoxLayout    : Linear vertical layout
# QGridLayout    : In indexable grid XxY
# QStackedLayout : Stacked (z) in front of one another

from sys import argv, exit
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtGui import QPalette, QColor


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Fourth App")


if __name__ == "__main__":
    app = QApplication(argv)

    window = MainWindow()
    window.show()

    exit(app.exec())
