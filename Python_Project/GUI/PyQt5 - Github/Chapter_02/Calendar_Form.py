from sys import argv, exit
from PyQt5.QtWidgets import (
    QApplication, QCalendarWidget, QCheckBox, QComboBox,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QMainWindow, QPushButton,
    QSizePolicy, QTextEdit, QTimeEdit, QVBoxLayout,
    QWidget
)
from PyQt5.QtCore import QTime


class MainWIndow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Not My Calendar App")
        self.resize(800, 600)

        # Create a central widget to hold layouts
        central = QWidget()
        self.setCentralWidget(central)

        # --- The Widgets ---
        self.calendar = QCalendarWidget()
        self.event_list = QListWidget()
        self.event_title = QLineEdit()
        self.event_category = QComboBox()
        self.event_time = QTimeEdit(QTime(8, 0))
        self.allday_check = QCheckBox("All Day")
        self.event_detail = QTextEdit()
        self.add_button = QPushButton("Add/Update")
        self.del_button = QPushButton("Delete")

        self.event_category.addItems([
            "Select category…", "New…", "Work",
            "Meeting", "Doctor", "Family"
        ])
        self.event_category.model().item(0).setEnabled(False)

        # --- Layouts ---
        main_layout = QHBoxLayout()
        central.setLayout(main_layout)

        main_layout.addWidget(self.calendar)
        self.calendar.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Expanding
        )

        right_layout = QVBoxLayout()
        main_layout.addLayout(right_layout)

        right_layout.addWidget(QLabel("Events on Date"))
        right_layout.addWidget(self.event_list)
        self.event_list.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Expanding
        )

        event_form = QGroupBox("Event")
        right_layout.addWidget(event_form)

        event_form_layout = QGridLayout()
        event_form.setLayout(event_form_layout)

        event_form_layout.addWidget(self.event_title, 1, 1, 1, 3)
        event_form_layout.addWidget(self.event_category, 2, 1)
        event_form_layout.addWidget(self.event_time, 2, 2)
        event_form_layout.addWidget(self.allday_check, 2, 3)
        event_form_layout.addWidget(self.event_detail, 3, 1, 1, 3)
        event_form_layout.addWidget(self.add_button, 4, 2)
        event_form_layout.addWidget(self.del_button, 4, 3)


if __name__ == "__main__":
    app = QApplication(argv)
    win = MainWIndow()
    win.show()
    exit(app.exec_())
