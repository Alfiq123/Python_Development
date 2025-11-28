from sys import argv, exit
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Third App")

        self.setMouseTracking(True)  # Added
        self.label = QLabel("Click in this window")
        self.label.setMouseTracking(True)  # Added
        self.setCentralWidget(self.label)

    def mouseMoveEvent(self, event):
        self.label.setText("mouseMoveEvent")

    def mousePressEvent(self, event):
        self.label.setText("mousePressEvent")

    def mouseReleaseEvent(self, event):
        self.label.setText("mouseReleaseEvent")

    def mouseDoubleClickEvent(self, event):
        self.label.setText("mouseDoubleClickEvent")


if __name__ == "__main__":
    app = QApplication(argv)

    window = MainWindow()
    window.show()

    exit(app.exec())
