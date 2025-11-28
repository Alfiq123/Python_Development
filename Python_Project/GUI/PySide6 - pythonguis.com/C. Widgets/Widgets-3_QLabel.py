# QLabel

from sys import argv, exit
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QApplication,
    ## QCheckBox,
    ## QComboBox,
    ## QDoubleSpinBox,
    QLabel,
    ## QLineEdit,
    ## QListWidget,
    QMainWindow,
    ## QSlider,
    ## QSpinBox,
)


### Horizontal Alignment
## Flag           | ## Behavior
# Qt.AlignLeft    | Aligns with the left edge.
# Qt.AlignRight   | Aligns with the right edge.
# Qt.AlignHCenter | Centers horizontally in the available space.
# Qt.AlignJustify | Justifies the text in the available space.

### Vertical Alignment
## Flag           | ## Behavior
# Qt.AlignTop     | Aligns with the top.
# Qt.AlignBottom  | Aligns with the bottom.
# Qt.AlignVCenter | Centers vertically in the available space.

### Center Alignment
## Flag           | ## Behavior
# Qt.AlignCenter  | Centers horizontally and vertically.

# You can combine flags together using pipes (`|`).
# However, note that you can only use vertical or horizontal alignment
#   flags at a time:


# noinspection PyUnresolvedReferences
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Third App")

        # w_label = QLabel("Hello", self)

        # w_label = QLabel("1", self)
        # w_label.setText("2")

        w_label = QLabel("Hello")

        font = w_label.font()
        font.setPointSize(30)

        w_label.setFont(font)
        w_label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        ## Add Images
        w_label.setPixmap(QPixmap("cat.png"))
        w_label.setScaledContents(True)

        self.setCentralWidget(w_label)


if __name__ == "__main__":
    app = QApplication(argv)

    window = MainWindow()
    window.show()

    exit(app.exec())
