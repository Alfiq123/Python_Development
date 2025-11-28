from sys import argv, exit
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QStackedLayout, QWidget
)
from colorwidget import Color


# noinspection PyTypeChecker
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Stacked Layout")
        self.setGeometry(512, 256, 512, 256)

        self.ui_stack()

    def ui_stack(self):
        layout = QStackedLayout()

        layout.addWidget(Color("DarkSalmon"))
        layout.addWidget(Color("DarkSeaGreen"))
        layout.addWidget(Color("DarkSlateBlue"))
        layout.addWidget(Color("DarkSlateGray"))

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication(argv)

    window = MainWindow()
    window.show()

    exit(app.exec())
