from sys import argv, exit
from MainWindow_Page import Ui_MainWindow
from PySide6.QtCore import QPropertyAnimation, QEasingCurve
from PySide6.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(argv)
    
    window = MainWindow()
    window.show()

    exit(app.exec())

