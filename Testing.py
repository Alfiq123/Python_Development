import sys
from PySide6.QtWidgets import QApplication, QTableView, QMessageBox
from PySide6.QtSql import QSqlDatabase, QSqlTableModel
from PySide6.QtCore import Qt, QDate


class CustomExpiryModel(QSqlTableModel):
    def __init__(self, db=None):
        super().__init__(db=db)

    def columnCount(self, parent=None):
        # Tambahkan 1 kolom ekstra untuk "Sisa Hari"
        # super().columnCount() adalah jumlah kolom asli di MySQL
        return super().columnCount(parent) + 1

    def data(self, index, role=Qt.DisplayRole):
        # Hitung index kolom terakhir (kolom baru kita)
        last_col_index = self.columnCount() - 1

        # Logika untuk Kolom Tambahan ("Sisa Hari")
        if index.column() == last_col_index:
            if role == Qt.DisplayRole:
                # Ambil data dari kolom 'tanggal_kedaluwarsa' (misal nama kolom di DB)
                # Pastikan nama kolom sesuai dengan di database Anda
                record = self.record(index.row())
                tgl_expired = record.value(
                    "tanggal_kedaluwarsa")  # Return QDate atau str

                # Konversi ke QDate jika masih string (tergantung driver SQL)
                if isinstance(tgl_expired, str):
                    tgl_expired = QDate.fromString(tgl_expired, "yyyy-MM-dd")

                if tgl_expired and tgl_expired.isValid():
                    hari_ini = QDate.currentDate()
                    sisa_hari = hari_ini.daysTo(tgl_expired)

                    if sisa_hari < 0:
                        return f"Kadaluwarsa ({abs(sisa_hari)} hari lalu)"
                    elif sisa_hari == 0:
                        return "HARI INI!"
                    else:
                        return f"{sisa_hari} hari lagi"
                return "-"

            # Opsional: Beri warna merah jika sudah kadaluwarsa (ForegroundRole)
            if role == Qt.ForegroundRole:
                record = self.record(index.row())
                tgl_expired = record.value("tanggal_kedaluwarsa")
                if tgl_expired:
                    # Handle konversi str ke QDate lagi jika perlu di sini
                    if isinstance(tgl_expired, str):
                        tgl_expired = QDate.fromString(tgl_expired,
                                                       "yyyy-MM-dd")

                    if QDate.currentDate().daysTo(tgl_expired) < 0:
                        return Qt.red  # Text warna merah

        # Untuk kolom asli database, gunakan perilaku standar
        return super().data(index, role)

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        # Beri nama header untuk kolom tambahan
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            if section == self.columnCount() - 1:
                return "Sisa Hari (Status)"

        return super().headerData(section, orientation, role)


# --- SETUP APLIKASI UTAMA ---
def main():
    app = QApplication(sys.argv)

    # 1. Koneksi Database
    db = QSqlDatabase.addDatabase("QMYSQL")
    db.setHostName("localhost")
    db.setUserName("root")  # Ganti user
    db.setPassword("apache_123")  # Ganti password
    db.setDatabaseName("Perpustakaan_0083")  # Ganti nama DB

    if not db.open():
        QMessageBox.critical(None, "Error", "Gagal koneksi database")
        return

    # 2. Setup Model Custom
    model = CustomExpiryModel(db=db)
    model.setTable("bahan_makanan")  # Ganti nama tabel
    model.select()  # Load data

    # Atur Header Kolom Asli (Opsional)
    model.setHeaderData(0, Qt.Horizontal, "ID")
    model.setHeaderData(1, Qt.Horizontal, "Nama Bahan")
    model.setHeaderData(2, Qt.Horizontal, "Tgl Expired")

    # 3. Setup View
    view = QTableView()
    view.setModel(model)
    view.resize(600, 400)
    view.setWindowTitle("Pemantauan Kedaluwarsa")
    view.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()