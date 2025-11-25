from sys import argv, exit
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(128, 128, 512, 512)

        self.button = QPushButton("Push Me!", self)
        self.label = QLabel("Hello", self)

        self.init_ui()

    def init_ui(self):
        self.button.setGeometry(150, 200, 200, 100)
        self.button.setStyleSheet("font-size: 30px;")
        self.button.clicked.connect(self.on_click)

        self.label.setGeometry(150, 300, 200, 100)
        self.label.setStyleSheet("font-size: 40px;")

    def on_click(self):
        print("Button Clicked!")

        self.button.setText("Clicked!")
        self.button.setDisabled(True)

        self.label.setText("Goodbye")


if __name__ == "__main__":
    app = QApplication(argv)

    window = MainWindow()
    window.show()

    exit(app.exec_())
