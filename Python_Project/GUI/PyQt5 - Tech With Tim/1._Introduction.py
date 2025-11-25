from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()

        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("First PyQT5 Program")
        self.init_ui()

    def init_ui(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("First PyQT5 Program")
        self.label.move(50, 50)

        self.btn_1 = QtWidgets.QPushButton(self)
        self.btn_1.setText("Click Me")
        self.btn_1.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText("You pressed the button")
        self.update()

    def update(self):
        self.label.adjustSize()


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


window()
