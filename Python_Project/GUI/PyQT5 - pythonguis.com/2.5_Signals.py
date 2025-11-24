# Context Menus

from sys import argv, exit
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QAction, QApplication, QMainWindow, QMenu, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.on_context_menu)

    def contextMenuEvent(self, e):
        context = QMenu(self)
        context.addAction(QAction("test 1", self))
        context.addAction(QAction("test 2", self))
        context.addAction(QAction("test 3", self))
        context.exec(e.globalPos())

    def on_context_menu(self, pos):
        context = QMenu(self)
        context.addAction(QAction("test 1", self))
        context.addAction(QAction("test 2", self))
        context.addAction(QAction("test 3", self))
        context.exec(self.mapToGlobal(pos))

    # Event hierarchy
    ## Python inheritance forwarding
    def mousePressEvent(self, event):
        print("Mouse Pressed!")
        super().mousePressEvent(event)

    ## Layout forwarding
    class CustomButton(QPushButton):
        def mousePressEvent(self, e):
            e.accept()

    class CustomButtonB(QPushButton):
        def event(self, e):
            e.ignore()


if __name__ == "__main__":
    app = QApplication(argv)

    window = MainWindow()
    window.show()

    exit(app.exec())
