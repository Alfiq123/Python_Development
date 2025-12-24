from sys import argv, exit

from data_handler import Database, InputUser, Transaksi, Filter
from dialog import EditTabel
from main_window import Ui_MainWindow
from style import Redesign
from style_table import GantiTanggal, WarnaSisaHari

from PySide6.QtCore import QDate
from PySide6.QtSql import QSqlQuery, QSqlQueryModel
from PySide6.QtWidgets import QApplication, QMainWindow, QHeaderView


# noinspection PyUnresolvedReferences
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Pemantauan Kedaluwarsa Bahan Makanan")

        # Database
        self.db = Database().db
        self.model = QSqlQueryModel(self)
        # self.model = QSqlTableModel(self, self.db)

        # Composition
        self.filter = Filter(self.ui, self.model)
        self.inputuser = InputUser(self.ui)
        self.inputuser.sinyal.connect(self.reload_data)
        self.redesign = Redesign(self.ui)
        self.transaksi = Transaksi(self.ui)
        self.transaksi.sinyal.connect(self.reload_data)

        # Expanding Code
        self.tabel_sql()  # 1
        self.iterasi_nama()
        self.modif_ui()
        self.redirect()

        # Edit Mode: Fitur Dadakan
        self.ui.p32i_chkedit.toggled.connect(self.open_edit_window)

    def iterasi_nama(self):
        """Memasukkan nama makanan ke dalam Combo Box"""
        query = QSqlQuery("SELECT `Nama` FROM `Bahan Makanan`;")

        while query.next():
            self.ui.p22ab_cbnama.addItem(query.value(0))

    def modif_ui(self):
        self.ui.p14f_detanggal.setDate(QDate.currentDate())
        self.ui.p14h_deeexpire.setDate(QDate.currentDate())
        self.ui.p22cd_detanggal.setDate(QDate.currentDate())

    def open_edit_window(self, state):
        if state:
            dialog = EditTabel(self)
            result = dialog.exec()
            print("Edit Mode Diaktifkan!")

            # Setelah edit window ditutup → refresh tabel utama
            self.tabel_sql()

            # Matikan checkbox
            self.ui.p32i_chkedit.setChecked(False)

    def redirect(self):
        """Mengganti halaman berdasarkan tombol sidebar"""
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
        """Mengganti warna tombol sidebar"""
        on = """
            QPushButton {
                background-color: #456882;
                border: 1px solid;
                border-color: #456882;
                border-radius: 5px;
                font-family: Helvetica, Inter, Sans-serif;
                font-size: 12pt;
                margin: 5px;
                padding: 10px;
            } 
            QPushButton:hover {
                background-color: #234C6A;
            }
        """
        off = """
            QPushButton {
                background-color: #234C6A;
                border: 1px solid;
                border-color: #234C6A;
                border-radius: 5px;
                font-family: Helvetica, Inter, Sans-serif;
                font-size: 12pt;
                margin: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #456882;
            }
        """

        self.ui.side_input.setStyleSheet(on if index == 0 else off)
        self.ui.side_transaksi.setStyleSheet(on if index == 1 else off)
        self.ui.side_laporan.setStyleSheet(on if index == 2 else off)

    def reload_data(self):
        if self.model:
            self.model.setQuery(self.model.query().lastQuery())
            self.ui.p22ab_cbnama.clear()
            self.iterasi_nama()
            self.filter.p3_filter()

        else:
            pass

    def tabel_sql(self):
        """Mengisi tabel dengan data dari Database"""
        self.model.setQuery("""
            SELECT 
                `Nama`,
                `Jumlah`,
                `Satuan`,
                `Tanggal Pembelian`,
                `Tanggal Kedaluwarsa`,
                `Kategori`,
                DATEDIFF(`Tanggal Kedaluwarsa`, CURDATE()) AS `Sisa Hari`
            FROM `Bahan Makanan`
            ORDER BY `Nama`
        """)

        self.ui.p32h_tbhasil.setModel(self.model)

        self.ui.p32h_tbhasil.setItemDelegate(WarnaSisaHari())
        self.ui.p32h_tbhasil.setItemDelegateForColumn(3, GantiTanggal())
        self.ui.p32h_tbhasil.setItemDelegateForColumn(4, GantiTanggal())

        self.ui.p32h_tbhasil.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )


if __name__ == "__main__":
    app = QApplication(argv)

    with open("styling.qss") as f:
        app.setStyleSheet(f.read())

    window = MainWindow()
    window.show()

    exit(app.exec())
