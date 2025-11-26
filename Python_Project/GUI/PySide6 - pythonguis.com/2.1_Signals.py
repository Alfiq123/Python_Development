from sys import argv, exit
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("The Signals")

        self.button_is_checked = True

        self.button = QPushButton("Push Me!", self)
        self.button.setCheckable(True)

        # button.clicked.connect(self.button_clicked)
        # button.clicked.connect(self.button_toggled)

        # self.button.released.connect(self.button_released)
        # self.button.setChecked(self.button_is_checked)

        self.button.clicked.connect(self.button_clicked)

        self.setCentralWidget(self.button)

    def button_clicked(self):
        self.button.setText("You already clicked me.")
        self.button.setEnabled(False)

        self.setWindowTitle("OneShot Signals")
        # print("Clicked!")

    # def button_toggled(self, checked):
    #     self.button_is_checked = checked

    #     print(f"Checked? {self.button_is_checked}")

    # def button_released(self):
    #     self.button_is_checked = self.button.isChecked()
    #
    #     print(self.button_is_checked)


if __name__ == "__main__":
    app = QApplication(argv)

    win = MainWindow()
    win.show()

    exit(app.exec())
