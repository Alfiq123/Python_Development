from sys import argv, exit
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QHBoxLayout, QGraphicsOpacityEffect


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button_1 = QPushButton("Num #1")
        self.button_2 = QPushButton("Num #2")
        self.button_3 = QPushButton("Num #3")

        self.init_ui()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        h_box = QHBoxLayout()
        h_box.addWidget(self.button_1)
        h_box.addWidget(self.button_2)
        h_box.addWidget(self.button_3)

        central_widget.setLayout(h_box)

        self.button_1.setObjectName("btn_1")
        self.button_2.setObjectName("btn_2")
        self.button_3.setObjectName("btn_3")

        self.setStyleSheet("""
            QPushButton {
                font-size: 40px;
                font-family: Helvetica;
                padding: 15px 75px;
                margin: 25px;
                border: 3px solid;
                border-radius: 15px;
            }
            
            QPushButton#btn_1 {
                background-color: Chocolate;
            }
            
            QPushButton#btn_2 {
                background-color: DarkSalmon;
            }
            
            QPushButton#btn_3 {
                background-color: Firebrick;
            }
            
            
            QPushButton#btn_1:hover {
                background-color: LightGrey;
            }
            
            QPushButton#btn_2:hover {
                background-color: LightGrey;
            }
            
            QPushButton#btn_3:hover {
                background-color: LightGrey;
            }
        """)


if __name__ == "__main__":
    app = QApplication(argv)

    window = MainWindow()
    window.show()

    exit(app.exec_())
