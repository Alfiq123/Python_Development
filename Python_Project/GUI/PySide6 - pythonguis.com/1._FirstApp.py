from sys import argv, exit
from PyQt5.QtCore import  QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My First App")
        self.button = QPushButton("Press Me")

        self.setFixedSize(QSize(400, 300))

        # Set the central widget of the Window.
        self.setCentralWidget(self.button)

if __name__ == "__main__":
    app = QApplication(argv)

    window = MainWindow()
    window.show()

    exit(app.exec())
