from sys import argv, exit
from PySide6.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget
from colorwidget import Color


# noinspection PyTypeChecker
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Grid App")
        self.setGeometry(512, 256, 512, 256)

        self.ui_grid()

    def ui_grid(self):
        layout = QGridLayout()

        layout.addWidget(Color("DarkGreen"), 0, 0)
        layout.addWidget(Color("DarkKhaki"), 1, 0)
        layout.addWidget(Color("DarkMagenta"), 1, 1)
        layout.addWidget(Color("DarkOliveGreen"), 2, 1)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication(argv)

    window = MainWindow()
    window.show()

    exit(app.exec())
