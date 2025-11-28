from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QWidget


class Color(QWidget):
    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)

        pallete = self.palette()
        pallete.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(pallete)
