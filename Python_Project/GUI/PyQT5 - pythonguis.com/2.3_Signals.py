# Connecting widgets together directly

from sys import argv, exit
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Third App")

        self.label = QLabel()

        self.n_input = QLineEdit()
        self.n_input.textChanged.connect(self.label.setText)

        layout = QVBoxLayout()
        layout.addWidget(self.n_input)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(container)


if __name__ == "__main__":
    app = QApplication(argv)

    window = MainWindow()
    window.show()

    exit(app.exec())
