from sys import argv, exit
from datetime import date, datetime, timedelta

from MainWindow_Page import Ui_MainWindow

from PySide6.QtCore import QDate, QDateTime, QObject, Signal
from PySide6.QtGui import QBrush, QColor
from PySide6.QtSql import (
    QSqlDatabase, QSqlQuery, QSqlQueryModel, QSqlTableModel
)
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QHeaderView, QMessageBox, QStyledItemDelegate,
    QTableView, QDialog, QPushButton, QHBoxLayout, QVBoxLayout
)


class Database:
    """Menghubungkan database"""

    def __init__(self):
        if QSqlDatabase.contains("qt_sql_default_connection"):
            self.db = QSqlDatabase.database("qt_sql_default_connection")

        else:
            self.db = QSqlDatabase.addDatabase("QMYSQL")
            self.db.setConnectOptions(f"SSL_CA={'ca.pem'}")
            self.db.setDatabaseName("Kedaluwarsa")
            self.db.setHostName("mysql-universal-izuaf-2003.c.aivencloud.com")
            self.db.setPassword("AVNS_BP73ypcHbhYc9olJhSX")
            self.db.setPort(23688)
            self.db.setUserName("avnadmin")
            self.db.open()

        if not self.db.open():
            print("User gagal membuat koneksi ke database")
            QMessageBox.warning(
                None,
                "Peringatan",
                "Gagal Menghubungkan Database"
            )
            exit()
            return

        else:
            pass


# noinspection PyUnresolvedReferences
class EditTabel(QDialog):
    """Membuat Edit Tabel karena kode sebelumnya kacau"""

    def __init__(self, parent=None, table_name="Bahan Makanan"):
        super().__init__(parent)

        self.setWindowTitle(f"Edit Mode - {table_name}")
        self.resize(900, 500)

        # --- MODEL --- #
        self.model = QSqlTableModel(self)
        self.model.setTable(table_name)
        self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.model.select()

        # --- TABLE VIEW --- #
        self.tb = QTableView()
        self.tb.setModel(self.model)
        self.tb.resizeColumnsToContents()
        self.tb.verticalHeader().setVisible(False)
        self.tb.hideColumn(0)
        self.tb.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeToContents
        )
        self.tb.setSortingEnabled(True)

        # --- BUTTONS --- #
        self.btnsimpan = QPushButton("Save")
        self.btncancel = QPushButton("Cancel")

        self.btnsimpan.clicked.connect(self.save_changes)
        self.btncancel.clicked.connect(self.cancel_changes)

        # --- STYLING --- #
        self.setStyleSheet("""
            QHeaderView { 
                background-color: hsl(210, 13%, 65%); 
                border: 1px solid; 
                border-radius: 5px;
                font-family: Helvetica, Inter, Sans-serif; 
                font-size: 12pt; 
            }
            QTableView {
                font-family: Helvetica, Inter, Sans-serif; 
                font-size: 12pt; 
            }
            QPushButton { 
                background-color: hsl(210, 31%, 80%); 
                border: 1px solid hsl(210, 13%, 65%); 
                border-radius: 5px; 
                font-family: Helvetica, Inter, Sans-serif; 
                font-size: 12pt; 
                margin: 10px; 
                padding: 10px; 
            } 
            QPushButton:hover { 
                background-color: hsl(210, 31%, 90%); 
            }
        """)

        # Layout button horizontal
        btnly = QHBoxLayout()
        btnly.addWidget(self.btnsimpan)
        btnly.addWidget(self.btncancel)

        # Layout utama
        layout = QVBoxLayout(self)
        layout.addWidget(self.tb)
        layout.addLayout(btnly)

    def save_changes(self):
        if not self.model.submitAll():
            QMessageBox.warning(
                self, "Error", self.model.lastError().text()
            )
        else:
            QMessageBox.information(
                self, "Sukses", "Perubahan Berhasil Disimpan!"
            )
            self.accept()

    def cancel_changes(self):
        self.model.revertAll()
        self.reject()


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


class WarnaSisaHari(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super().initStyleOption(option, index)

        # Kolom ke-? sesuaikan dengan posisinya di tabelmu
        # misal sisa hari ada di kolom 3 (index mulai 0 → 0,1,2,3)
        if index.column() == 6:
            sisa = index.data()

            if sisa is not None:
                try:
                    sisa = int(sisa)

                    if sisa > 7:
                        option.backgroundBrush = QBrush(
                            QColor("#B3FFB3"))  # hijau

                    elif 1 <= sisa <= 7:
                        option.backgroundBrush = QBrush(
                            QColor("#FFF9A6"))  # kuning

                    elif sisa <= 0:
                        option.backgroundBrush = QBrush(
                            QColor("#FFB3B3"))  # merah

                except ValueError:
                    pass


class InputUser(QObject):
    sinyal = Signal()

    def __init__(self, ui):
        super().__init__()
        self.ui = ui
        self.ui.btnsimpan.clicked.connect(self.simpan_data)

    def simpan_data(self):
        __nama = self.ui.p13b_lenama.text()
        __jumlah = self.ui.p14b_spjumlah.value()
        __satuan = self.ui.p14d_cbsatuan.currentText()
        __tglbeli = self.ui.p14f_detanggal.date().toString("yyyy-MM-dd")
        __tglexpire = self.ui.p14h_deeexpire.date().toString("yyyy-MM-dd")
        __kategori = ""

        # Kondisi Pertama: Cek Kekosongan Data
        if not __nama or not __jumlah or not __satuan:
            QMessageBox.warning(
                None,
                "Input Kosong",
                "Pastikan semua data telah diisi sebelum menyimpan."
            )
            return

        else:
            pass

        # Kondisi Kedua: Cek Duplikasi Nama
        dup = QSqlQuery()
        dup.prepare('SELECT COUNT(*) FROM "Bahan Makanan" WHERE "Nama" = ?')
        dup.addBindValue(__nama)
        dup.exec()
        dup.next()

        if dup.value(0) > 0:
            QMessageBox.warning(
                None,
                "Nama Duplikat",
                f"Nama [{__nama}] sudah tersedia!"
            )
            return

        else:
            pass

        # Kondisi Ketiga: Cek RadioButton
        if self.ui.p15b_rbdaging.isChecked():
            __kategori = "Daging"
        elif self.ui.p15c_rbsayuran.isChecked():
            __kategori = "Sayuran"
        elif self.ui.p15d_rbbuah.isChecked():
            __kategori = "Buah"
        elif self.ui.p15e_rbsusu.isChecked():
            __kategori = "Susu"
        elif self.ui.p15f_rbroti.isChecked():
            __kategori = "Roti"
        else:
            __kategori = "Lainnya"

        # Jika lolos semua, Masukkan data
        query = QSqlQuery()
        query.prepare("""
            INSERT INTO "Bahan Makanan" (
                "Nama", "Jumlah", "Satuan",
                "Tanggal Pembelian", "Tanggal Kedaluwarsa", "Kategori"
            ) VALUES
            (:nama, :jumlah, :satuan, :tglbeli, :tglexpire, :kategori)
        """)
        query.bindValue(":nama", __nama)
        query.bindValue(":jumlah", __jumlah)
        query.bindValue(":satuan", __satuan)
        query.bindValue(":tglbeli", __tglbeli)
        query.bindValue(":tglexpire", __tglexpire)
        query.bindValue(":kategori", __kategori)

        if query.exec():
            QMessageBox.information(
                None,
                "Info",
                "Data berhasil disimpan"
            )
            self.sinyal.emit()

        else:
            QMessageBox.critical(
                None,
                "Peringatan",
                f"Gagal menyimpan: {query.lastError().text()}"
            )


class Transaksi(QObject):
    sinyal = Signal()

    def __init__(self, ui):
        super().__init__()
        self.ui = ui
        self.ui.p22db_btnproses.clicked.connect(self.proses_transaksi)

    def proses_transaksi(self):
        if self.ui.p22bc_rbmasuk.isChecked():
            self.tambah_barang()

        elif self.ui.p22bb_rbkeluar.isChecked():
            self.kurangi_barang()

        else:
            QMessageBox.information(
                None,
                "Peringatan",
                "Silakan Masukkan Data!"
            )
            pass

    def tambah_barang(self):
        db = QSqlDatabase.database()
        nama = self.ui.p22ab_cbnama.currentText()
        jumlah = self.ui.p22cb_spjumlah.value()

        if jumlah < 1:
            QMessageBox.warning(
                None,
                "Peringatan",
                "Jumlah tidak boleh kosong atau negatif"
            )
            return

        else:
            pass

        query = QSqlQuery(db)
        query.prepare("""
            UPDATE `Bahan Makanan`
            SET `Jumlah` = `Jumlah` + :jumlah
            WHERE `Nama` = :nama
        """)
        query.bindValue(":nama", nama)
        query.bindValue(":jumlah", jumlah)

        if query.exec():
            QMessageBox.information(
                None,
                "Sukses",
                f"Stok [{nama}] berhasil ditambah"
            )
            self.sinyal.emit()

        else:
            QMessageBox.critical(
                None,
                "Error",
                query.lastError().text()
            )

    def kurangi_barang(self):
        db = QSqlDatabase.database()
        nama = self.ui.p22ab_cbnama.currentText()
        jumlah = self.ui.p22cb_spjumlah.value()

        if jumlah < 1:
            QMessageBox.warning(
                None,
                "Peringatan",
                "Jumlah tidak boleh kosong atau negatif"
            )
            return

        else:
            pass

        # Verif 1: Cek persediaan
        cek = QSqlQuery(db)
        cek.prepare(
            "SELECT `Jumlah` FROM `Bahan Makanan` WHERE `Nama` = :nama"
        )
        cek.bindValue(":nama", nama)
        cek.exec()
        cek.next()

        if cek.value(0) < jumlah:
            QMessageBox.warning(
                None,
                "Stok Tidak Cukup",
                f"Stok tersisa {cek.value(0)}, Permintaan melebihi batas."
            )
            return

        else:
            pass

        query = QSqlQuery(db)
        query.prepare("""
            UPDATE `Bahan Makanan`
            SET `Jumlah` = `Jumlah` - :jumlah
            WHERE `Nama` = :nama
        """)
        query.bindValue(":nama", nama)
        query.bindValue(":jumlah", jumlah)

        if query.exec():
            QMessageBox.information(
                None,
                "Sukses",
                f"Stok [{nama}] berhasil dikurangi"
            )
            self.sinyal.emit()

        else:
            QMessageBox.critical(
                None,
                "Error",
                query.lastError().text()
            )


class Filter:
    def __init__(self, ui, model):
        self.ui = ui
        self.model = model

        self.p3_filter_set()

    def p3_filter(self):
        # hari_ini = date(year=2023, month=10, day=30)
        hari_ini = date.today()
        kategori = self.ui.p32b_cbkategori.currentText()
        lst_where = []

        # Memfilter tabel berdasarkan kategori dari Combo Box
        if kategori != "Semua":
            lst_where.append(f"`Kategori` = '{kategori}'")

        else:
            pass

        # Memfilter tabel berdasarkan tenggat dari Radio Button
        if self.ui.p32e_rbminggu.isChecked():
            awal_minggu = hari_ini - timedelta(days=hari_ini.weekday())
            akhir_minggu = awal_minggu + timedelta(days=6)

            lst_where.append(
                f"`Tanggal Kedaluwarsa` "
                f"BETWEEN '{awal_minggu}' AND '{akhir_minggu}'"
            )

        elif self.ui.p32f_rbbulan.isChecked():
            awal_bulan = hari_ini.replace(day=1)

            if hari_ini.month == 12:
                akhir_bulan = hari_ini.replace(
                    year=hari_ini.year + 1, month=1, day=1
                ) - timedelta(days=1)

            else:
                akhir_bulan = hari_ini.replace(
                    month=hari_ini.month + 1, day=1
                ) - timedelta(days=1)

            lst_where.append(
                f"`Tanggal Kedaluwarsa` "
                f"BETWEEN '{awal_bulan}' AND '{akhir_bulan}'"
            )

        else:
            pass

        sql_where = f"WHERE {' AND '.join(lst_where)}" if lst_where else ""
        sql_query = f"""
            SELECT
                `Nama`, `Jumlah`, `Satuan`, 
                `Tanggal Pembelian`, `Tanggal Kedaluwarsa`, `Kategori`,
                DATEDIFF(`Tanggal Kedaluwarsa`, CURDATE()) AS `Sisa Hari`
            FROM `Bahan Makanan`
            {sql_where}
        """
        self.model.setQuery(sql_query)

        # self.model.setFilter(" AND ".join(lst_where))
        # self.model.select()

    def p3_filter_set(self):
        self.ui.p32b_cbkategori.currentTextChanged.connect(self.p3_filter)
        self.ui.p32e_rbminggu.toggled.connect(self.p3_filter)
        self.ui.p32f_rbbulan.toggled.connect(self.p3_filter)
        self.ui.p32g_rbsemua.toggled.connect(self.p3_filter)


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
        self.inputuser = InputUser(self.ui)
        self.inputuser.sinyal.connect(self.reload_data)
        self.transaksi = Transaksi(self.ui)
        self.transaksi.sinyal.connect(self.reload_data)
        self.filter = Filter(self.ui, self.model)

        self.tabel_sql()  # 1
        self.redirect()  # 2
        self.iterasi_nama()
        self.modif_ui()

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
                background-color: hsl(210, 31%, 60%);
                border: 1px solid;
                border-color: hsl(210, 31%, 60%);
                border-radius: 5px;
                font-family: Helvetica, Inter, Sans-serif;
                font-size: 12pt;
                margin: 5px;
                padding: 10px;
            } 
            QPushButton:hover {
                background-color: hsl(210, 31%, 70%);
            }
        """
        off = """
            QPushButton {
                background-color: hsl(210, 31%, 80%);
                border: 1px solid;
                border-color: hsl(210, 31%, 80%);
                border-radius: 5px;
                font-family: Helvetica, Inter, Sans-serif;
                font-size: 12pt;
                margin: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: hsl(210, 31%, 90%);
            }
        """

        self.ui.side_input.setStyleSheet(on if index == 0 else off)
        self.ui.side_transaksi.setStyleSheet(on if index == 1 else off)
        self.ui.side_laporan.setStyleSheet(on if index == 2 else off)

        # Gak guna
        if index == 2:
            self.setFixedSize(1024, 719)

        else:
            self.setFixedSize(704, 719)

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

        delegate = WarnaSisaHari()
        self.ui.p32h_tbhasil.setItemDelegate(delegate)

        self.ui.p32h_tbhasil.setItemDelegateForColumn(3, GantiTanggal())
        self.ui.p32h_tbhasil.setItemDelegateForColumn(4, GantiTanggal())

        self.ui.p32h_tbhasil.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeToContents
        )


if __name__ == "__main__":
    app = QApplication(argv)

    window = MainWindow()
    window.show()

    exit(app.exec())
