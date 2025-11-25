from sys import argv, exit
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)

        self.line_edit = QLineEdit(self)
        self.button = QPushButton("Submit", self)

        self.init_ui()

    def init_ui(self):
        self.line_edit.setGeometry(10, 10, 200, 50)
        self.line_edit.setStyleSheet("""
            font-size: 25px;
            font-family: Helvetica;
        """)
        self.line_edit.setPlaceholderText("Enter your name")

        self.button.setGeometry(10, 70, 100, 50)
        self.button.setStyleSheet("""
            font-size: 25px;
            font-family: Helvetica;
        """)

        self.button.clicked.connect(self.submit)

    def submit(self):
        text = self.line_edit.text()
        print(f"Hello {text}")


if __name__ == "__main__":
    app = QApplication(argv)

    window = MainWindow()
    window.show()

    app.exec_()
