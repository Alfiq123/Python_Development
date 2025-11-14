import ttkbootstrap as ttk


class LogikaKode:
    def __init__(self, tampilan):
        self.tampilan = tampilan

        self.kalkulasi = ""

    def tambahkan_ke_kalkulasi(self, symbol):
        self.kalkulasi += str(symbol)
        self.tampilan.text_result.delete(index1=1.0, index2="end")
        self.tampilan.text_result.insert(index=1.0, chars=self.kalkulasi)

    def evaluasi_kalkulasi(self):
        try:
            kalkulasi = str(eval(self.kalkulasi))
            self.tampilan.text_result.delete(index1=1.0, index2="end")
            self.tampilan.text_result.insert(index=1.0, chars=kalkulasi)

        except:
            self.bersihkan_text()
            self.tampilan.text_result.insert(index=1.0, chars="Error")

    def backspace(self):
        self.kalkulasi = self.kalkulasi[:-1]
        self.tampilan.text_result.delete(1.0, "end")
        self.tampilan.text_result.insert(1.0, self.kalkulasi)

    def bersihkan_text(self):
        self.kalkulasi = ""
        self.tampilan.text_result.delete(index1=1.0, index2="end")


class Tampilan:
    def __init__(self):
        self.logika = LogikaKode(tampilan=self)

        self.base = ttk.Window(themename="darkly")
        self.base.title("Proyek Kalkulator")
        self.base.resizable(width=False, height=False)

        # ══════════════════════════════════════ #
        # ══════════ Area untuk Frame ══════════ #

        # ===== Frame untuk kotak teks ===== #
        self.frame_1 = ttk.Frame(master=self.base)
        self.frame_1.grid(row=0, column=0, padx=10, pady=10)

        # ===== Frame untuk [Frame 1 dan 2] ===== #
        self.frame_2_3 = ttk.Frame(master=self.base)
        self.frame_2_3.grid(row=1, column=0, padx=5, pady=5)

        # ===== Frame untuk angka ===== #
        self.frame_2 = ttk.Frame(master=self.frame_2_3)
        self.frame_2.grid(row=0, column=0, padx=5, pady=5)

        # ===== Frame untuk operasi ===== #
        self.frame_3 = ttk.Frame(master=self.frame_2_3)
        self.frame_3.grid(row=0, column=1, padx=5, pady=5)

        # ===== Frame untuk bagian bawah 1 ===== #
        self.frame_4 = ttk.Frame(master=self.base)
        self.frame_4.grid(row=2, column=0, padx=5, pady=(5, 0))

        # ===== Frame untuk bagian bawah 2 ===== #
        self.frame_5 = ttk.Frame(master=self.base)
        self.frame_5.grid(row=3, column=0, padx=0, pady=0)

        # ===== Frame untuk bagian bawah 3 ===== #
        self.frame_6 = ttk.Frame(master=self.base)
        self.frame_6.grid(row=4, column=0, padx=0, pady=0)

        # ══════════ Area untuk Frame ══════════ #
        # ══════════════════════════════════════ #

        # ===== Kotak Teks ===== #
        self.text_result = ttk.Text(
            master=self.frame_1,
            height=1,
            width=16,
            font=("Arial", 24)
        )
        self.text_result.grid(row=0, column=0)

        # ===== Tombol Angka Atas ===== #

        self.tombol_1 = ttk.Button(
            master=self.frame_2,
            text="1",
            command=lambda: self.logika.tambahkan_ke_kalkulasi(1),
            width=5
        )
        self.tombol_1.grid(row=2, column=1, padx=2, pady=2)

        self.tombol_2 = ttk.Button(
            master=self.frame_2,
            text="2",
            command=lambda: self.logika.tambahkan_ke_kalkulasi(2),
            width=5
        )
        self.tombol_2.grid(row=2, column=2, padx=2, pady=2)

        self.tombol_3 = ttk.Button(
            master=self.frame_2,
            text="3",
            command=lambda: self.logika.tambahkan_ke_kalkulasi(3),
            width=5
        )
        self.tombol_3.grid(row=2, column=3, padx=2, pady=2)

        # ===== Tombol Angka Tengah ===== #

        self.tombol_4 = ttk.Button(
            master=self.frame_2,
            text="4",
            command=lambda: self.logika.tambahkan_ke_kalkulasi(4),
            width=5
        )
        self.tombol_4.grid(row=3, column=1, padx=2, pady=2)

        self.tombol_5 = ttk.Button(
            master=self.frame_2,
            text="5",
            command=lambda: self.logika.tambahkan_ke_kalkulasi(5),
            width=5
        )
        self.tombol_5.grid(row=3, column=2, padx=2, pady=2)

        self.tombol_6 = ttk.Button(
            master=self.frame_2,
            text="6",
            command=lambda: self.logika.tambahkan_ke_kalkulasi(6),
            width=5
        )
        self.tombol_6.grid(row=3, column=3, padx=2, pady=2)

        # ===== Tombol Angka Bawah ===== #

        self.tombol_7 = ttk.Button(
            master=self.frame_2,
            text="7",
            command=lambda: self.logika.tambahkan_ke_kalkulasi(7),
            width=5
        )
        self.tombol_7.grid(row=4, column=1, padx=2, pady=2)

        self.tombol_8 = ttk.Button(
            master=self.frame_2,
            text="8",
            command=lambda: self.logika.tambahkan_ke_kalkulasi(8),
            width=5
        )
        self.tombol_8.grid(row=4, column=2, padx=2, pady=2)

        self.tombol_9 = ttk.Button(
            master=self.frame_2,
            text="9",
            command=lambda: self.logika.tambahkan_ke_kalkulasi(9),
            width=5
        )
        self.tombol_9.grid(row=4, column=3, padx=2, pady=2)

        # ===== Tombol Angka Nol ===== #

        self.tombol_0 = ttk.Button(
            master=self.frame_2,
            text="0",
            command=lambda: self.logika.tambahkan_ke_kalkulasi(0),
            width=5
        )
        self.tombol_0.grid(row=5, columnspan=4, padx=2, pady=2)

        # ===== Tombol Operasi Angka ===== #

        self.tombol_tambah = ttk.Button(
            master=self.frame_3,
            text="+",
            command=lambda: self.logika.tambahkan_ke_kalkulasi("+"),
            width=5
        )
        self.tombol_tambah.grid(row=0, column=0, padx=2, pady=2)

        self.tombol_kurang = ttk.Button(
            master=self.frame_3,
            text="-",
            command=lambda: self.logika.tambahkan_ke_kalkulasi("-"),
            width=5
        )
        self.tombol_kurang.grid(row=1, column=0, padx=2, pady=2)

        self.tombol_kali = ttk.Button(
            master=self.frame_3,
            text="*",
            command=lambda: self.logika.tambahkan_ke_kalkulasi("*"),
            width=5
        )
        self.tombol_kali.grid(row=2, column=0, padx=2, pady=2)

        self.tombol_bagi = ttk.Button(
            master=self.frame_3,
            text="/",
            command=lambda: self.logika.tambahkan_ke_kalkulasi("/"),
            width=5
        )
        self.tombol_bagi.grid(row=3, column=0, padx=2, pady=2)

        # ===== Tombol Sisa ? ===== #
        # ===== Baris 0 - ( ) . = ===== #

        self.tombol_kurung_buka = ttk.Button(
            master=self.frame_4,
            text="(",
            command=lambda: self.logika.tambahkan_ke_kalkulasi("("),
            width=5
        )
        self.tombol_kurung_buka.grid(row=0, column=0, padx=2, pady=2)

        self.tombol_kurung_tutup = ttk.Button(
            master=self.frame_4,
            text=")",
            command=lambda: self.logika.tambahkan_ke_kalkulasi(")"),
            width=5
        )
        self.tombol_kurung_tutup.grid(row=0, column=1, padx=2, pady=2)

        self.tombol_titik = ttk.Button(
            master=self.frame_4,
            text=".",
            command=lambda: self.logika.tambahkan_ke_kalkulasi("."),
            width=5
        )
        self.tombol_titik.grid(row=0, column=2, padx=2, pady=2)

        self.tombol_sama_dengan = ttk.Button(
            master=self.frame_4,
            text="=",
            command=self.logika.evaluasi_kalkulasi,
            width=6,
            bootstyle="secondary"
        )
        self.tombol_sama_dengan.grid(row=0, column=3, padx=2, pady=2)

        # ===== Tombol untuk Soal 2 ===== #
        # ===== Baris 1 - ^ mod √ ===== #

        self.tombol_pangkat = ttk.Button(
            master=self.frame_5,
            text="^",
            command=lambda: self.logika.tambahkan_ke_kalkulasi("**"),
            width=5
        )
        self.tombol_pangkat.grid(row=1, column=0, padx=2, pady=2)

        self.tombol_modulus = ttk.Button(
            master=self.frame_5,
            text="mod",
            command=lambda: self.logika.tambahkan_ke_kalkulasi("%"),
            width=5
        )
        self.tombol_modulus.grid(row=1, column=1, padx=2, pady=2)

        self.tombol_sqrt = ttk.Button(
            master=self.frame_5,
            text="√",
            command=lambda: self.logika.tambahkan_ke_kalkulasi("**(1/"),
            width=5
        )
        self.tombol_sqrt.grid(row=1, column=2, padx=2, pady=2)

        # ===== Tombol untuk membersihkan ===== #
        # ===== Baris 2 - ⌫ C ===== #

        self.tombol_backspace = ttk.Button(
            master=self.frame_6,
            text="⌫",
            command=self.logika.backspace,
            width=5,
        )
        self.tombol_backspace.grid(row=2, column=0, padx=2, pady=2)

        self.tombol_clear = ttk.Button(
            master=self.frame_6,
            text="C",
            command=self.logika.bersihkan_text,
            width=5,
            bootstyle="danger"
        )
        self.tombol_clear.grid(row=2, column=1, padx=2, pady=2)

        # ===== Bind Enter untuk mengeksekusi ===== #
        self.base.bind("<Return>", lambda event: self.logika.evaluasi_kalkulasi())

    def jalankan(self):
        self.base.mainloop()


if __name__ == '__main__':
    tampilkan = Tampilan()
    tampilkan.jalankan()
