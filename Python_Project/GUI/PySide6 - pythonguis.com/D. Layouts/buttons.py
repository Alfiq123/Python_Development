from sys import argv, exit
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QHBoxLayout,
    QVBoxLayout, QWidget, QPushButton
)
from colorwidget import Color


# noinspection PyTypeChecker
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Layout App")
        self.setGeometry(512, 256, 512, 256)

        ## Nesting layouts
        layout_h = QHBoxLayout()
        layout_v1 = QVBoxLayout()
        layout_v2 = QVBoxLayout()

        # layout_h.setContentsMargins(0, 0, 0, 0)
        # layout_h.setSpacing(20)

        layout_h.setSpacing(10)
        layout_v1.setSpacing(10)
        layout_v2.setSpacing(10)

        layout_v1.addWidget(QPushButton("Click"))
        layout_v1.addWidget(QPushButton("Click"))
        layout_v1.addWidget(QPushButton("Click"))

        layout_h.addLayout(layout_v1)
        layout_h.addWidget(QPushButton("Click"))

        layout_v2.addWidget(QPushButton("Click"))
        layout_v2.addWidget(QPushButton("Click"))

        layout_h.addLayout(layout_v2)

        widget = QWidget()
        widget.setLayout(layout_h)
        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication(argv)

    window = MainWindow()
    window.show()

    exit(app.exec())
