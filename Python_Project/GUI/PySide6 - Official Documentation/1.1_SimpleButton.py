from sys import argv, exit
from PySide6.QtWidgets import QApplication, QPushButton
from PySide6.QtCore import Slot


@Slot()
def say_hello():
    print("Button Clicked, Hello!")


app = QApplication(argv)

button = QPushButton("Push Me!")
button.clicked.connect(say_hello)
button.show()

exit(app.exec())
