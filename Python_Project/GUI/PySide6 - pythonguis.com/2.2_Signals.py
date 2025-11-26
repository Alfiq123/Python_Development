# Changing the interface

from sys import argv, exit
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from random import choice

window_titles = [
    "My App",
    "My App",
    "Still My App",
    "Still My App",
    "What on earth",
    "What on earth",
    "This is surprising",
    "This is surprising",
    "Something went wrong"
]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Second App")

        self.n_times_clicked = 0

        self.button = QPushButton("Press Me!")
        self.button.clicked.connect(self.button_clicked)

        self.windowTitleChanged.connect(self.window_changed)

        self.setCentralWidget(self.button)

    def button_clicked(self):
        print("\nClicked!")

        self.n_times_clicked += 1
        print(self.n_times_clicked)

        new_window_title = choice(window_titles)
        print(f"Setting title: {new_window_title}")
        self.setWindowTitle(new_window_title)

    def window_changed(self, window_title):
        print(f"Window title changed: {window_title}")

        if window_title == "Something went wrong":
            self.button.setDisabled(True)
            exit()


if __name__ == "__main__":
    app = QApplication(argv)

    win = MainWindow()
    win.show()

    exit(app.exec())
