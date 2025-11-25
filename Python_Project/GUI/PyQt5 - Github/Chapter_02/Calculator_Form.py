from sys import argv, exit
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QLCDNumber, QLineEdit,
    QGridLayout, QPushButton, QSizePolicy
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        central = QWidget()
        layout = QVBoxLayout()
        central.setLayout(layout)
        self.setCentralWidget(central)

        lcd = QLCDNumber()
        layout.addWidget(lcd)

        history = QLineEdit()
        layout.addWidget(history)

        button_texts = [
            "Clear", "BackSpace", "Mem", "Mem Clear",
            "1", "2", "3", "+",
            "4", "5", "6", "-",
            "7", "8", "9", "×",
            ".", "0", "=", "÷"
        ]

        button_layout = QGridLayout()
        layout.addLayout(button_layout)

        for num, button_text in enumerate(button_texts):
            button = QPushButton(button_text, self)
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

            row = num // 4
            column = num % 4

            button_layout.addWidget(button, row, column)


if __name__ == "__main__":
    app = QApplication(argv)

    win = MainWindow()
    win.show()

    exit(app.exec_())
