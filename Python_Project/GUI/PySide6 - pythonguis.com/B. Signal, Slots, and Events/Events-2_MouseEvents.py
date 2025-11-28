from sys import argv, exit
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow


## Method      | ## Returns
# .button()    | Specific button that triggered this event
# .buttons()   | State of all mouse buttons (OR'ed flags)
# .globalPos() | Application-global position as a QPoint
# .globalX()   | Application-global horizontal X position
# .globalY()   | Application-global vertical Y position
# .pos()       | Widget-relative position as a QPoint integer
# .posF()      | Widget-relative position as a QPointF float


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Events: Mouse Events")

        self.label = QLabel("Click in this window")
        self.setCentralWidget(self.label)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            # handle the left-button press in here
            self.label.setText("mousePressEvent LEFT")

        elif event.button() == Qt.MouseButton.MiddleButton:
            # handle the middle-button press in here.
            self.label.setText("mousePressEvent MIDDLE")

        elif event.button() == Qt.MouseButton.RightButton:
            # handle the right-button press in here.
            self.label.setText("mousePressEvent RIGHT")

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.label.setText("mouseReleaseEvent LEFT")

        elif event.button() == Qt.MouseButton.MiddleButton:
            self.label.setText("mouseReleaseEvent MIDDLE")

        elif event.button() == Qt.MouseButton.RightButton:
            self.label.setText("mouseReleaseEvent RIGHT")

    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.label.setText("mouseDoubleClickEvent LEFT")

        elif event.button() == Qt.MouseButton.MiddleButton:
            self.label.setText("mouseDoubleClickEvent MIDDLE")

        elif event.button() == Qt.MouseButton.RightButton:
            self.label.setText("mouseDoubleClickEvent RIGHT")


if __name__ == "__main__":
    app = QApplication(argv)

    window = MainWindow()
    window.show()

    exit(app.exec())

## Identifier                 | ## Value (binary) | ## Represents
# Qt.MouseButton.NoButton     | 0 (000)           | No button pressed, or the event is not related to a button press.
# Qt.MouseButton.LeftButton   | 1 (001)           | The left button is pressed
# Qt.MouseButton.RightButton  | 2 (010)           | The right button is pressed.
# Qt.MouseButton.MiddleButton | 4 (100)           | The middle button is pressed.
