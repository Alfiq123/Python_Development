import sys
# Kita import widget-widget yang dibutuhkan
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QHBoxLayout, QFormLayout,
    QRadioButton, QComboBox, QMessageBox
)


class FormulirPendaftaran(QWidget):
    def __init__(self):
        super().__init__()
        self.inisialisasi_ui()

    def inisialisasi_ui(self):
        """Fungsi untuk mengatur tampilan antarmuka (UI)"""

        # 1. Pengaturan Jendela Utama
        self.setWindowTitle('Formulir Pendaftaran Mahasiswa')
        self.setGeometry(100, 100, 400, 300)  # x, y, lebar, tinggi

        # 2. Membuat Widget Input

        # --- Input Nama (Text Field) ---
        self.input_nama = QLineEdit()
        self.input_nama.setPlaceholderText("Masukkan nama lengkap Anda")

        # --- Input Jurusan (Dropdown / ComboBox) ---
        self.input_jurusan = QComboBox()
        # Menambahkan pilihan ke dalam dropdown
        self.input_jurusan.addItems(["Teknik Informatika", "Sistem Informasi", "Ilmu Komputer", "Desain Grafis"])

        # --- Input Jenis Kelamin (Radio Button) ---
        # Kita butuh 2 tombol radio
        self.radio_pria = QRadioButton("Laki-laki")
        self.radio_wanita = QRadioButton("Perempuan")
        self.radio_pria.setChecked(True)  # Set default terpilih ke Laki-laki

        # Kita butuh wadah (layout) horizontal agar radio button berjejer ke samping
        layout_gender = QHBoxLayout()
        layout_gender.addWidget(self.radio_pria)
        layout_gender.addWidget(self.radio_wanita)

        # --- Tombol Submit ---
        self.tombol_daftar = QPushButton("Daftar Sekarang")
        # Menghubungkan tombol dengan fungsi logika (event handler)
        self.tombol_daftar.clicked.connect(self.proses_pendaftaran)

        # 3. Mengatur Tata Letak (Layout)

        # QFormLayout sangat bagus untuk form karena otomatis merapikan: "Label: Input"
        form_layout = QFormLayout()

        # Menambahkan baris ke form layout (Label, Widget Inputnya)
        form_layout.addRow("Nama Lengkap:", self.input_nama)
        form_layout.addRow("Jurusan:", self.input_jurusan)
        form_layout.addRow("Jenis Kelamin:", layout_gender)  # Masukkan layout horizontal tadi ke sini

        # 4. Menggabungkan ke Layout Utama
        layout_utama = QVBoxLayout()
        layout_utama.addLayout(form_layout)  # Masukkan form di bagian atas
        layout_utama.addWidget(self.tombol_daftar)  # Tombol di bagian bawah

        # Terapkan layout ke jendela aplikasi
        self.setLayout(layout_utama)

    def proses_pendaftaran(self):
        """Fungsi ini dipanggil saat tombol diklik"""

        # Ambil teks dari input nama
        nama = self.input_nama.text()

        # Ambil teks dari jurusan yang dipilih
        jurusan = self.input_jurusan.currentText()

        # Cek radio button mana yang aktif
        gender = "Tidak Diketahui"
        if self.radio_pria.isChecked():
            gender = "Laki-laki"
        elif self.radio_wanita.isChecked():
            gender = "Perempuan"

        # Validasi sederhana: Jika nama kosong, tampilkan peringatan
        if not nama:
            QMessageBox.warning(self, "Peringatan", "Nama wajib diisi!")
            return

        # Tampilkan hasil input menggunakan Pop-up (MessageBox)
        pesan = f"Data Berhasil Diterima!\n\nNama: {nama}\nJurusan: {jurusan}\nGender: {gender}"
        QMessageBox.information(self, "Sukses", pesan)


# --- Blok Utama untuk Menjalankan Aplikasi ---
if __name__ == '__main__':
    # 1. Buat objek aplikasi
    app = QApplication(sys.argv)

    # 2. Buat instance dari class formulir kita
    window = FormulirPendaftaran()

    # 3. Tampilkan jendela
    window.show()

    # 4. Loop utama agar aplikasi tetap berjalan
    sys.exit(app.exec_())