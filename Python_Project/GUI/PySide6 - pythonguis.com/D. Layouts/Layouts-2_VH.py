from sys import argv, exit
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout
)
from colorwidget import Color


# noinspection PyTypeChecker
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Layout App")
        self.setGeometry(512, 256, 512, 256)

        ## Add Layout - Vertical
        layout = QVBoxLayout()
        layout.addWidget(Color("Brown"))
        layout.addWidget(Color("Aquamarine"))
        layout.addWidget(Color("AntiqueWhite"))

        ## Add Layout - Horizontal
        layout = QHBoxLayout()
        layout.addWidget(Color("Brown"))
        layout.addWidget(Color("Aquamarine"))
        layout.addWidget(Color("AntiqueWhite"))

        widget = QWidget()  # widget = Color("Red")
        widget.setLayout(layout)
        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication(argv)

    window = MainWindow()
    window.show()

    exit(app.exec())
