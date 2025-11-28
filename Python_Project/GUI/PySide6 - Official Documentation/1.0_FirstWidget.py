from sys import argv, exit
from PySide6.QtWidgets import QApplication, QLabel

# app = QApplication(argv)

# label = QLabel("Hello World!")
# label.show()

# app.exec()

app = QApplication([])

label = QLabel("<font color=firebrick size=40>Hello World!</font>")
label.show()

app.exec()
