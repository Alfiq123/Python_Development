from sys import argv, exit
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QGridLayout, QVBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")

        self.keypad()

    def keypad(self):
        central = QWidget()
        layout = QGridLayout()

        btn_1 = QPushButton("Text")
        layout.addWidget(btn_1)

        central.setLayout(layout)
        self.setCentralWidget(central)



if __name__ == "__main__":
    app = QApplication(argv)

    window = MainWindow()
    window.show()

    exit(app.exec())
