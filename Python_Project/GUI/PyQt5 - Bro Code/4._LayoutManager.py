from sys import argv, exit
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QWidget,
    QVBoxLayout, QHBoxLayout, QGridLayout
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(128, 128, 512, 512)
        self.init_ui()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        label_1 = QLabel("Number 1", self)
        label_2 = QLabel("Number 2", self)
        label_3 = QLabel("Number 3", self)
        label_4 = QLabel("Number 4", self)
        label_5 = QLabel("Number 5", self)

        label_1.setStyleSheet("background-color: red;")
        label_2.setStyleSheet("background-color: green;")
        label_3.setStyleSheet("background-color: yellow;")
        label_4.setStyleSheet("background-color: cyan;")
        label_5.setStyleSheet("background-color: magenta;")

        # var = Q__Layout()
        # var.addWidget(var, row, column, rowspan, columnspan)

        # vbox = QVBoxLayout()
        # vbox.addWidget(label_1)
        # vbox.addWidget(label_2)
        # vbox.addWidget(label_3)
        # vbox.addWidget(label_4)
        # vbox.addWidget(label_5)

        # hbox = QHBoxLayout()
        # hbox.addWidget(label_1)
        # hbox.addWidget(label_2)
        # hbox.addWidget(label_3)
        # hbox.addWidget(label_4)
        # hbox.addWidget(label_5)

        grid = QGridLayout()
        grid.addWidget(label_1, 0, 0)
        grid.addWidget(label_2, 0, 1)
        grid.addWidget(label_3, 1, 0)
        grid.addWidget(label_4, 1, 1)
        grid.addWidget(label_5, 2, 0, 1, 2)

        central_widget.setLayout(grid)


if __name__ == "__main__":
    app = QApplication(argv)

    window = MainWindow()
    window.show()

    exit(app.exec_())
