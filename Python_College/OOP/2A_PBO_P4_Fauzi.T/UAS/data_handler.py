from datetime import date, timedelta

from PySide6.QtCore import QObject, Signal
from PySide6.QtSql import QSqlDatabase, QSqlQuery
from PySide6.QtWidgets import QMessageBox


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


class InputUser(QObject):
    sinyal = Signal()

    def __init__(self, ui):
        super().__init__()
        self.ui = ui
        # Menghubungkan signal clicked dengan method simpan_data
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

        # Kondisi Kedua: Cek Duplikasi Nama
        dup = QSqlQuery()
        dup.prepare(
            "SELECT COUNT(*) FROM `Bahan Makanan` WHERE `Nama` = ?"
        )
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
                "Tanggal Pembelian",
                "Tanggal Kedaluwarsa",
                "Kategori"
            )
            VALUES (
                :nama, :jumlah, :satuan, 
                :tglbeli, :tglexpire, :kategori
            )
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
