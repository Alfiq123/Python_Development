import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLineEdit, QPushButton,
    QVBoxLayout, QGridLayout, QMessageBox
)
from PyQt5.QtCore import Qt


class Kalkulator(QWidget):
    def __init__(self):
        super().__init__()
        self.inisialisasi_ui()

    def inisialisasi_ui(self):
        self.setWindowTitle('Kalkulator PyQt5')
        self.setGeometry(100, 100, 300, 400)

        # --- 1. Layar Tampilan (Display) ---
        # Menggunakan QLineEdit agar terlihat seperti layar angka
        self.layar = QLineEdit()

        # Mengatur font agar besar dan tebal
        self.layar.setStyleSheet("font-size: 25px; height: 50px;")

        # Mengatur teks agar rata kanan (seperti kalkulator asli)
        self.layar.setAlignment(Qt.AlignRight)

        # Membuat layar "Read Only" agar user tidak bisa ketik huruf sembarangan lewat keyboard
        self.layar.setReadOnly(True)

        # --- 2. Membuat Tombol dengan Grid Layout ---
        # Kita gunakan QGridLayout untuk menyusun tombol rapi (baris x kolom)
        grid_layout = QGridLayout()

        # Daftar tombol dan posisinya
        # Format list: ['Teks Tombol', baris, kolom]
        # Kita buat susunan 4 baris x 4 kolom
        tombol_config = [
            ['7', 0, 0], ['8', 0, 1], ['9', 0, 2], ['/', 0, 3],
            ['4', 1, 0], ['5', 1, 1], ['6', 1, 2], ['*', 1, 3],
            ['1', 2, 0], ['2', 2, 1], ['3', 2, 2], ['-', 2, 3],
            ['C', 3, 0], ['0', 3, 1], ['=', 3, 2], ['+', 3, 3],
        ]

        # Loop untuk membuat tombol secara otomatis
        for teks, baris, kolom in tombol_config:
            tombol = QPushButton(teks)
            tombol.setStyleSheet("font-size: 20px; height: 40px;")

            # Hubungkan setiap tombol ke fungsi 'aksi_tombol'
            tombol.clicked.connect(self.aksi_tombol)

            # Masukkan tombol ke dalam grid layout sesuai posisi (row, col)
            grid_layout.addWidget(tombol, baris, kolom)

        # --- 3. Menyusun Layout Utama ---
        layout_utama = QVBoxLayout()
        layout_utama.addWidget(self.layar)  # Layar di atas
        layout_utama.addLayout(grid_layout)  # Tombol-tombol di bawahnya

        self.setLayout(layout_utama)

    def aksi_tombol(self):
        # Mengetahui tombol mana yang sedang diklik user
        tombol = self.sender()
        teks_tombol = tombol.text()

        # Ambil teks yang saat ini ada di layar
        teks_layar = self.layar.text()

        if teks_tombol == 'C':
            # Jika tombol C, hapus semua isi layar
            self.layar.clear()

        elif teks_tombol == '=':
            # Jika tombol =, hitung hasilnya
            try:
                # Fungsi eval() di Python sangat sakti, dia menghitung string matematika
                # Contoh: eval("2 + 2") akan menjadi 4
                hasil = str(eval(teks_layar))
                self.layar.setText(hasil)
            except ZeroDivisionError:
                self.layar.setText("Error")  # Menangani pembagian dengan nol
            except Exception:
                self.layar.setText("Error")  # Menangani error sintaks lain

        else:
            # Jika tombol angka atau operator (+ - * /), tambahkan ke layar
            # Contoh: Layar "1", tekan "2" -> Layar jadi "12"
            self.layar.setText(teks_layar + teks_tombol)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    kalkulator = Kalkulator()
    kalkulator.show()
    sys.exit(app.exec_())