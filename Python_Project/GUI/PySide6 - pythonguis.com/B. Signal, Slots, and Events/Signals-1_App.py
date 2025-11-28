from sys import argv, exit
from PySide6.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Signal, Slots, and Events")


if __name__ == "__main__":
    app = QApplication(argv)

    window = MainWindow()
    window.show()

    exit(app.exec())
