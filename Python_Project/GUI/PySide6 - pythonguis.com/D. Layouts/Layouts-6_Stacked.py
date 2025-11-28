from sys import argv, exit
from PySide6.QtWidgets import (
    QApplication, QMainWindow,
    QHBoxLayout, # QLabel,
    QPushButton, QStackedLayout,
    QVBoxLayout, QWidget,
)
from colorwidget import Color


# noinspection PyTypeChecker
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Stacked Layout")
        self.setGeometry(512, 256, 512, 256)

        self.stacklayout = QStackedLayout()

        self.ui_stack()

    def ui_stack(self):
        pagelayout = QVBoxLayout()
        button_layout = QHBoxLayout()
        # self.stacklayout = QStackedLayout()

        pagelayout.addLayout(button_layout)
        pagelayout.addLayout(self.stacklayout)

        # Tab 1
        button = QPushButton("Cornsilk")
        button.setFixedSize(128, 50)
        button.pressed.connect(self.activate_tab_1)
        button_layout.addWidget(button)

        self.stacklayout.addWidget(Color("Cornsilk"))

        # Tab 2
        button = QPushButton("CornflowerBlue")
        button.setFixedSize(150, 50)
        button.pressed.connect(self.activate_tab_2)
        button_layout.addWidget(button)

        self.stacklayout.addWidget(Color("CornflowerBlue"))

        # Tab 3
        button = QPushButton("Coral")
        button.setFixedSize(128, 50)
        button.pressed.connect(self.activate_tab_3)
        button_layout.addWidget(button)

        self.stacklayout.addWidget(Color("Coral"))

        # Tab 4
        button = QPushButton("Chocolate")
        button.setFixedSize(128, 50)
        button.pressed.connect(self.activate_tab_4)
        button_layout.addWidget(button)

        self.stacklayout.addWidget(Color("Chocolate"))

        # Tab 5
        button = QPushButton("Chartreuse")
        button.setFixedSize(128, 50)
        button.pressed.connect(self.activate_tab_5)
        button_layout.addWidget(button)

        self.stacklayout.addWidget(Color("Chartreuse"))

        widget = QWidget()
        widget.setLayout(pagelayout)

        self.setCentralWidget(widget)

    def activate_tab_1(self):
        self.stacklayout.setCurrentIndex(0)

    def activate_tab_2(self):
        self.stacklayout.setCurrentIndex(1)

    def activate_tab_3(self):
        self.stacklayout.setCurrentIndex(2)

    def activate_tab_4(self):
        self.stacklayout.setCurrentIndex(3)

    def activate_tab_5(self):
        self.stacklayout.setCurrentIndex(4)


if __name__ == "__main__":
    app = QApplication(argv)

    window = MainWindow()
    window.show()

    exit(app.exec())
