# Combo Box

from sys import argv, exit
## from PySide6.QtCore import Qt
## from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QApplication,
    ## QCheckBox,
    QComboBox,
    ## QDoubleSpinBox,
    ## QLabel,
    ## QLineEdit,
    ## QListWidget,
    QMainWindow,
    ## QSlider,
    ## QSpinBox,
)


## Flag                          ## Behavior
# QComboBox.NoInsert             : Performs no insert.
# QComboBox.InsertAtTop          : Inserts as first item.
# QComboBox.InsertAtCurrent      : Replaces the currently selected item.
# QComboBox.InsertAtBottom       : Inserts after the last item.
# QComboBox.InsertAfterCurrent   : Inserts after the current item.
# QComboBox.InsertBeforeCurrent  : Inserts before the current item.
# QComboBox.InsertAlphabetically : Inserts in alphabetical order.


# noinspection PyUnresolvedReferences
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = QComboBox()
        widget.addItems(["One", "Two", "Three", "Boom"])

        ## Sends the current index (position) of the selected item.
        widget.currentIndexChanged.connect(self.index_changed)

        ## There is an alternate signal to send the text.
        widget.currentTextChanged.connect(self.text_changed)

        # widget.setEditable(True)

        ## To use the Flags, apply the flag as follows:
        # widget.setInsertPolicy(QComboBox.InsertAlphabetically)

        ## Limit the number of items allowed in the box
        widget.setMaxCount(10)

        self.setCentralWidget(widget)

    @staticmethod
    def index_changed(i): print(i)

    @staticmethod
    def text_changed(s): print(s)


if __name__ == "__main__":
    app = QApplication(argv)

    window = MainWindow()
    window.show()

    exit(app.exec())
