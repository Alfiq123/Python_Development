from sys import argv, exit
# from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,  # QLabel,
    QMainWindow,  # QPushButton,
    QTabWidget,  # QWidget,
)
from colorwidget import Color


# noinspection PyTypeChecker,PyUnresolvedReferences
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Tab Widget")
        self.setGeometry(512, 256, 512, 256)

        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.West)
        tabs.setMovable(True)
        tabs.setDocumentMode(True)

        for color in ["FireBrick", "FloralWhite", "ForestGreen", "Fuchsia"]:
            tabs.addTab(Color(color), color)

        self.setCentralWidget(tabs)


if __name__ == "__main__":
    app = QApplication(argv)

    window = MainWindow()
    window.show()

    exit(app.exec())
