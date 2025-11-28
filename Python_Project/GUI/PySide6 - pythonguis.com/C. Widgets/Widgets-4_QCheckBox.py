# QCheckBox

from sys import argv, exit
from PySide6.QtCore import Qt
## from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    ## QComboBox,
    ## QDoubleSpinBox,
    ## QLabel,
    ## QLineEdit,
    ## QListWidget,
    QMainWindow,
    ## QSlider,
    ## QSpinBox,
)


## Flag 	          | ## Behavior
# Qt.Unchecked        | Item is unchecked
# Qt.PartiallyChecked | Item is partially checked
# Qt.Checked          | Item is checked


# noinspection PyUnresolvedReferences
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = QCheckBox("This is a Checkbox")
        widget.setCheckState(Qt.Checked)

        # For tristate: widget.setCheckState(Qt.PartiallyChecked)
        # Or: widget.setTriState(True)
        widget.stateChanged.connect(self.show_state)

        self.setCentralWidget(widget)

    @staticmethod
    def show_state(s):
        print(s == Qt.Checked)
        print(s)


if __name__ == "__main__":
    app = QApplication(argv)

    window = MainWindow()
    window.show()

    exit(app.exec())
