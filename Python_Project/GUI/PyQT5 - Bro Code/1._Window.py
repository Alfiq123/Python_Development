from sys import argv, exit
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bro Code First GUI")
        self.setGeometry(128, 128, 512, 512)
        self.setWindowIcon(QIcon("mansion.png"))


if __name__ == "__main__":
    app = QApplication(argv)

    window = MainWindow()
    window.show()

    exit(app.exec_())
