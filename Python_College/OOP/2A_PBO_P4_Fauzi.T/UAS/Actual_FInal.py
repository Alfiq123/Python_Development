from sys import argv, exit
from datetime import date, datetime, timedelta

from MainWindow_Page import Ui_MainWindow

from PySide6.QtCore import QDate, QDateTime, QObject, Signal
from PySide6.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QHeaderView, QMessageBox, QStyledItemDelegate)


class Database:
    """Menghubungkan database"""

    def __init__(self):
        self.db = QSqlDatabase.addDatabase("QMYSQL")
        self.db.setHostName("localhost")
        self.db.setUserName("root")
        self.db.setPassword("apache_123")
        self.db.setDatabaseName("Kedaluwarsa")

        if not self.db.open():
            print("User gagal membuat koneksi ke database")
            QMessageBox.warning(
                QMainWindow(),
                "Peringatan",
                "Gagal Menghubungkan Database")
            exit()
            return


# noinspection PyUnresolvedReferences
class GantiTanggal(QStyledItemDelegate):
    """Mengubah Format tanggal Amerika ke Standar Internasional, F**K USA"""

    def displayText(self, value, locale):
        if isinstance(value, (QDate, QDateTime)):
            return value.toString("yyyy/MM/dd")

        elif isinstance(value, (datetime.date, datetime.datetime)):
            return value.strftime("%Y/%m/%d")

        else:
            return super().displayText(value, locale)


class ExpireDelegate(QStyledItemDelegate):
    def displayText(self, value, locale):
        if not value:
            return ""
        today = date.today()
        selisih = (value.toPyDate() - today).days
        if selisih > 0:
            return f"{selisih} hari lagi"
        elif selisih == 0:
            return "Hari ini kadaluarsa"
        else:
            return f"Sudah {abs(selisih)} hari"


class InputUser(QObject):
    sinyal = Signal()

    def __init__(self, ui):
        super().__init__()
        self.ui = ui
        self.ui.tombol_simpan.clicked.connect(self.simpan_data)

    def simpan_data(self):
        __nama = self.ui.p13_02_inputnama.text()
        __jumlah = self.ui.p14_02_inputjumlah.text()
        __satuan = self.ui.p14_04_combosatuan.currentText()
        __tglbeli = self.ui.p14_06_datetanggal.date().toString("yyyy-MM-dd")
        __tglexpire = self.ui.p14_08_dateexpire.date().toString("yyyy-MM-dd")
        __kategori = ""

        if self.ui.p15_02_radiodaging.isChecked():
            __kategori = "Daging"
        elif self.ui.p15_03_radiosayuran.isChecked():
            __kategori = "Sayuran"
        elif self.ui.p15_04_radiobuah.isChecked():
            __kategori = "Buah"
        elif self.ui.p15_05_radiosusu.isChecked():
            __kategori = "Susu"
        elif self.ui.p15_06_radioroti.isChecked():
            __kategori = "Roti"
        else:
            __kategori = "Lainnya"

        query = QSqlQuery()
        query.prepare("""
            INSERT INTO `Input User` (
                `Nama`, `Jumlah`, `Satuan`, 
                `Tanggal Pembelian`, `Tanggal Kedaluwarsa`, `Kategori`
            )
            VALUES (?, ?, ?, ?, ?, ?)
        """)
        query.addBindValue(__nama)
        query.addBindValue(__jumlah)
        query.addBindValue(__satuan)
        query.addBindValue(__tglbeli)
        query.addBindValue(__tglexpire)
        query.addBindValue(__kategori)

        if query.exec():
            QMessageBox.information(
                QMainWindow(),
                "Info",
                "Data berhasil disimpan")
            self.sinyal.emit()

        else:
            QMessageBox.critical(
                QMainWindow(),
                "Peringatan",
                f"Gagal menyimpan: {query.lastError().text()}")


# noinspection PyUnresolvedReferences
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.inputuser = InputUser(self.ui)
        self.inputuser.sinyal.connect(self.reload_data)

        self.model = None

        self.tabel_sql()  # 1
        self.redirect()  # 2
        self.p2_iterasi_nama()
        self.p3_filter_set()

    def tabel_sql(self):
        """Mengisi tabel dengan data dari Database"""
        db = Database().db
        self.model = QSqlTableModel(self, db)
        self.model.setTable("Input User")

        self.ui.p32_07_tabelhasil.setItemDelegateForColumn(3, GantiTanggal())
        self.ui.p32_07_tabelhasil.setItemDelegateForColumn(4, GantiTanggal())

        self.ui.p32_07_tabelhasil.setItemDelegateForColumn(6, ExpireDelegate())

        self.model.select()

        self.ui.p32_07_tabelhasil.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeToContents)
        self.ui.p32_07_tabelhasil.setModel(self.model)

    def p2_iterasi_nama(self):
        """Memasukkan nama makanan ke dalam Combo Box"""
        query = QSqlQuery("SELECT `Nama` FROM `Input User`;")

        while query.next():
            self.ui.p22_02_combonama.addItem(query.value(0))

    def p3_filter(self):
        hari_ini = date(year=2025, month=1, day=25)
        kategori = self.ui.p32_02_combokategori.currentText()
        lst_query = []

        # Memfilter tabel berdasarkan kategori dari Combo Box
        if kategori != "Semua":
            lst_query.append(f"`Kategori` = '{kategori}'")

        # Memfilter tabel berdasarkan tenggat dari Radio Button
        if self.ui.p32_04_radiominggu.isChecked():
            awal_minggu = hari_ini - timedelta(days=hari_ini.weekday())
            akhir_minggu = awal_minggu + timedelta(days=6)

            lst_query.append(
                f"`Tanggal Kedaluwarsa` BETWEEN '{awal_minggu}'"
                f" AND '{akhir_minggu}'")

        elif self.ui.p32_05_radiobulan.isChecked():
            awal_bulan = hari_ini.replace(day=1)

            if hari_ini.month == 12:
                akhir_bulan = hari_ini.replace(
                    year=hari_ini.year + 1, month=1, day=1) - timedelta(days=1)

            else:
                akhir_bulan = hari_ini.replace(
                    month=hari_ini.month + 1, day=1) - timedelta(days=1)

            lst_query.append(
                f"`Tanggal Kedaluwarsa` BETWEEN '{awal_bulan}'"
                f" AND '{akhir_bulan}'")

        else:
            pass

        self.model.setFilter(" AND ".join(lst_query))
        self.model.select()

    def p3_filter_set(self):
        self.ui.p32_02_combokategori.currentTextChanged.connect(
            self.p3_filter)
        self.ui.p32_04_radiominggu.toggled.connect(self.p3_filter)
        self.ui.p32_05_radiobulan.toggled.connect(self.p3_filter)
        self.ui.p32_06_radiosemua.toggled.connect(self.p3_filter)

    def redirect(self):
        """Mengganti halaman berdasarkan tombol sidebar"""
        self.ui.side_input.clicked.connect(
            lambda: self.ui.pages.setCurrentIndex(0))
        self.ui.side_transaksi.clicked.connect(
            lambda: self.ui.pages.setCurrentIndex(1))
        self.ui.side_laporan.clicked.connect(
            lambda: self.ui.pages.setCurrentIndex(2))

        self.redirect_tombol(0)
        self.ui.pages.currentChanged.connect(self.redirect_tombol)

    def redirect_tombol(self, index):
        """Mengganti warna tombol sidebar"""
        on = """
            QPushButton {
                background-color: hsl(33, 29%, 90%);
                border: 1px solid;
                border-radius: 5px;
                font-family: Helvetica, Inter, Sans-serif;
                font-size: 12pt;
                margin: 5px;
                padding: 10px;
            } 
            QPushButton:hover {
                background-color: hsl(27, 19%, 82%);
            }
        """
        off = """
            QPushButton {
                background-color: hsl(33, 29%, 70%);
                border: 1px solid;
                border-radius: 5px;
                font-family: Helvetica, Inter, Sans-serif;
                font-size: 12pt;
                margin: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: hsl(27, 19%, 82%);
            }
        """

        self.ui.side_input.setStyleSheet(on if index == 0 else off)
        self.ui.side_transaksi.setStyleSheet(on if index == 1 else off)
        self.ui.side_laporan.setStyleSheet(on if index == 2 else off)

    def reload_data(self):
        if self.model:
            self.model.select()
            self.ui.p22_02_combonama.clear()
            self.p2_iterasi_nama()
            self.p3_filter()

        else:
            pass


if __name__ == "__main__":
    app = QApplication(argv)

    window = MainWindow()
    window.show()

    exit(app.exec())
