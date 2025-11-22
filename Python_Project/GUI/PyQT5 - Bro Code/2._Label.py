from sys import argv, exit
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(128, 128, 512, 512)

        label = QLabel("Hello", self)
        label.setFont(QFont("Helvetica", 24))
        label.setGeometry(0, 0, 256, 64)
        label.setStyleSheet("""
            color: #D8C4B6;
            background-color: #3E5879;
            font-weight: bold;
            font-style: italic;
            text-decoration: underline;
        """)

        ## Vertical Alignment
        # label.setAlignment(Qt.AlignTop)  # Vertical Top
        # label.setAlignment(Qt.AlignBottom)  # Vertical Bottom
        # label.setAlignment(Qt.AlignVCenter)  # Vertical Center

        ## Horizontal Alignment
        # label.setAlignment(Qt.AlignRight)  # Horizontal Right
        # label.setAlignment(Qt.AlignHCenter)  # Horizontal Center
        # label.setAlignment(Qt.AlignLeft)  # Horizontal Left

        ## Combine Alignment
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)  # Center & Top
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)  # Center & Bottom
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # Center & Center

        ## Shortcut for Center & Center
        label.setAlignment(Qt.AlignCenter)


if __name__ == "__main__":
    app = QApplication(argv)

    window = MainWindow()
    window.show()

    exit(app.exec_())
