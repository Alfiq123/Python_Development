from sys import argv, exit
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QButtonGroup


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)

        self.radio_1 = QRadioButton("Visa", self)
        self.radio_2 = QRadioButton("MasterCard", self)
        self.radio_3 = QRadioButton("Gift Card", self)
        self.radio_4 = QRadioButton("In-Store", self)
        self.radio_5 = QRadioButton("Online", self)

        self.btn_group_1 = QButtonGroup(self)
        self.btn_group_2 = QButtonGroup(self)

        self.init_ui()

    def init_ui(self):
        self.radio_1.setGeometry(0, 0, 300, 55)
        self.radio_2.setGeometry(0, 50, 300, 55)
        self.radio_3.setGeometry(0, 100, 300, 55)
        self.radio_4.setGeometry(0, 150, 300, 55)
        self.radio_5.setGeometry(0, 200, 300, 55)

        self.setStyleSheet("""
            QRadioButton {
                font-size: 40px;
                font-family: Helvetica;
                padding: 10px
            }
        """)

        self.btn_group_1.addButton(self.radio_1)
        self.btn_group_1.addButton(self.radio_2)
        self.btn_group_1.addButton(self.radio_3)

        self.btn_group_2.addButton(self.radio_4)
        self.btn_group_2.addButton(self.radio_5)

        self.radio_1.toggled.connect(self.radio_changed)
        self.radio_2.toggled.connect(self.radio_changed)
        self.radio_3.toggled.connect(self.radio_changed)
        self.radio_4.toggled.connect(self.radio_changed)
        self.radio_5.toggled.connect(self.radio_changed)

    def radio_changed(self):
        # radio_buttons = self.sender()
        if self.sender().isChecked():
            print(f"{self.sender().text()} is selected")


if __name__ == "__main__":
    app = QApplication(argv)

    window = MainWindow()
    window.show()

    app.exec_()
