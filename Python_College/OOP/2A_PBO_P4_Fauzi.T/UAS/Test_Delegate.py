import sys
from PySide6.QtWidgets import QApplication, QMessageBox, QWidget, QVBoxLayout, QLabel
from PySide6.QtSql import QSqlDatabase, QSqlQuery


class DatabaseManager:
    def __init__(self):
        # 1. Menentukan Driver Database (QMYSQL)
        self.db = QSqlDatabase.addDatabase("QMYSQL")

        # 2. Mengatur Kredensial Koneksi
        self.db.setHostName("localhost")  # Host (biasanya localhost)
        self.db.setPort(3306)  # Port default MySQL
        self.db.setUserName("root")  # Username database
        self.db.setPassword("apache_123")  # Password database
        self.db.setDatabaseName("DatabaseBank")  # Ganti dengan nama database Anda

    def connect(self):
        # 3. Membuka Koneksi
        if not self.db.open():
            print("Koneksi Gagal: ", self.db.lastError().text())
            return False
        print("Koneksi Berhasil terhubung ke MySQL!")
        return True

    def check_drivers(self):
        # Mengecek apakah driver MySQL tersedia di PySide6 Anda
        print("Driver yang tersedia:", QSqlDatabase.drivers())


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tes Koneksi MySQL")
        self.resize(300, 100)

        layout = QVBoxLayout()
        self.label = QLabel("Mencoba menghubungkan...", self)
        layout.addWidget(self.label)
        self.setLayout(layout)

        # Inisialisasi Database
        self.db_manager = DatabaseManager()
        self.db_manager.check_drivers()

        if self.db_manager.connect():
            self.label.setText("Status: Terhubung ke Database ✅")
            self.run_query()
        else:
            self.label.setText("Status: Gagal Terhubung ❌")

    def run_query(self):
        # Contoh menjalankan query sederhana
        query = QSqlQuery()
        if query.exec("SELECT VERSION()"):
            if query.next():
                version = query.value(0)
                print(f"Versi MySQL: {version}")
        else:
            print("Query Error:", query.lastError().text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())