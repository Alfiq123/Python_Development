from sys import argv, exit
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(128, 128, 512, 512)

        label = QLabel(self)
        label.setGeometry(0, 0, 256, 256)

        # pixmap = QPixmap("mansion.png")
        # label.setPixmap(pixmap)

        label.setPixmap(QPixmap("mansion.png"))
        label.setScaledContents(True)

        label.setGeometry(
            (self.width() - label.width()) // 2,
            (self.height() - label.height()) // 2,
            label.width(),
            label.height()
        )


if __name__ == "__main__":
    app = QApplication(argv)

    window = MainWindow()
    window.show()

    exit(app.exec_())
