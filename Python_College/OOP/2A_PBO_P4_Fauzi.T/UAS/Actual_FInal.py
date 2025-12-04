from sys import argv, exit
from MainWindow_Page import Ui_MainWindow
from PySide6.QtSql import QSqlDatabase, QSqlTableModel
from PySide6.QtWidgets import QApplication, QMainWindow, QHeaderView


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.data_base()
        self.redirect()

    def data_base(self):
        db = QSqlDatabase.addDatabase("QMYSQL")
        db.setHostName("localhost")
        db.setUserName("root")
        db.setPassword("apache_123")
        db.setDatabaseName("Kedaluwarsa")

        if not db.open():
            print("Gagal koneksi database")
            return

        self.model = QSqlTableModel(self, db)
        self.model.setTable("Input User")
        self.model.select()

        self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.ui.tableView.setModel(self.model)

    def redirect(self):
        self.ui.side_input.clicked.connect(
            lambda: self.ui.pages.setCurrentIndex(0)
        )
        self.ui.side_transaksi.clicked.connect(
            lambda: self.ui.pages.setCurrentIndex(1)
        )
        self.ui.side_laporan.clicked.connect(
            lambda: self.ui.pages.setCurrentIndex(2)
        )

        self.redirect_tombol(0)
        self.ui.pages.currentChanged.connect(self.redirect_tombol)

    def redirect_tombol(self, index):
        focus = "background-color: CornflowerBlue;"
        no_focus = "background-color: none;"

        self.ui.side_input.setStyleSheet(focus if index == 0 else no_focus)
        self.ui.side_transaksi.setStyleSheet(focus if index == 1 else no_focus)
        self.ui.side_laporan.setStyleSheet(focus if index == 2 else no_focus)


if __name__ == "__main__":
    app = QApplication(argv)

    window = MainWindow()
    window.show()

    exit(app.exec())
