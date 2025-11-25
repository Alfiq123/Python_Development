from sys import argv, exit
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)

        self.check_1 = QCheckBox("Do you like food?", self)

        self.init_ui()

    def init_ui(self):
        self.check_1.setGeometry(10, 0, 500, 100)
        self.check_1.setStyleSheet("""
            font-size: 30px;
            font-family: Helvetica;
        """)
        self.check_1.setChecked(False)  # Make Checkbutton Checked
        self.check_1.stateChanged.connect(self.on_check)

    def on_check(self, state):
        if state == Qt.Checked:
            print("You Like Food!")
        else:
            print("You Don't Like Food!")


if __name__ == "__main__":
    app = QApplication(argv)

    window = MainWindow()
    window.show()

    app.exec_()
