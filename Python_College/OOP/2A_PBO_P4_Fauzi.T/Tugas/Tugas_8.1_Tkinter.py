import tkinter as tk


class LogikaKode:
    def __init__(self, tampilan):
        self.tampilan = tampilan

        self.kalkulasi = ""

    def tambahkan_ke_kalkulasi(self, simbol):
        self.kalkulasi += str(simbol)
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
        self.tampilan.text_result.delete(index1=1.0, index2="end")
        self.tampilan.text_result.insert(index=1.0, chars=self.kalkulasi)

    def bersihkan_text(self):
        self.kalkulasi = ""
        self.tampilan.text_result.delete(index1=1.0, index2="end")


class Tampilan:
    def __init__(self):
        self.logika = LogikaKode(tampilan=self)

        self.base = tk.Tk()
        self.base.title("Kalkulator Sederhana")
        self.base.resizable(width=False, height=False)

        # ══════════ Area untuk Frame ══════════ #

        # Frame 1
        # ===== Frame untuk kotak teks ===== #
        self.frame_1 = tk.Frame(master=self.base)
        self.frame_1.grid(row=0, column=0, padx=10, pady=10)

        # Frame 2
        # ===== Frame untuk [Frame 1 dan 2] ===== #
        self.frame_2_3 = tk.Frame(master=self.base)
        self.frame_2_3.grid(row=1, column=0, padx=5, pady=5)

        # Frame 3
        # ===== Frame untuk angka ===== #
        self.frame_2 = tk.Frame(master=self.frame_2_3)
        self.frame_2.grid(row=0, column=0, padx=5, pady=5)

        # Frame 4
        # ===== Frame untuk operasi ===== #
        self.frame_3 = tk.Frame(master=self.frame_2_3)
        self.frame_3.grid(row=0, column=1, padx=5, pady=5)

        # Frame 5
        # ===== Frame untuk bagian bawah 1 ===== #
        self.frame_4 = tk.Frame(master=self.base)
        self.frame_4.grid(row=2, column=0, padx=5, pady=(5, 0))

        # Frame 6
        # ===== Frame untuk bagian bawah 2 ===== #
        self.frame_5 = tk.Frame(master=self.base)
        self.frame_5.grid(row=3, column=0, padx=0, pady=0)

        # Frame 7
        # ===== Frame untuk bagian bawah 3 ===== #
        self.frame_6 = tk.Frame(master=self.base)
        self.frame_6.grid(row=4, column=0, padx=0, pady=0)

        # ══════════════════════════════════════ #

        # ===== Kotak Teks ===== #
        self.text_result = tk.Text(
            master=self.frame_1,
            height=1,
            width=16,
            font=("Arial", 24)
        )
        self.text_result.grid(row=0, column=0)

        self.tombol = [("1", "2", "3"), ("4", "5", "6"), ("7", "8", "9"), ("0",)]
        self.operasi = ["+", "-", "*", "/"]
        self.sisa = ["(", ")", "."]
        self.soal_12 = ["**", "%", "**(1/"]

        # Frame 2 = Angka
        for i, item_2 in enumerate(self.tombol):
            for j, angka in enumerate(item_2):
                tk.Button(
                    master=self.frame_2,
                    text=angka,
                    command=lambda ang=angka: self.logika.tambahkan_ke_kalkulasi(ang),
                    width=5
                ).grid(row=i, column=j, columnspan=3 if angka == "0" else 1, padx=2, pady=2)

        # Frame 3 = Operasi Aritmatika
        for i, item_3 in enumerate(self.operasi):
            tk.Button(
                master=self.frame_3,
                text=item_3,
                command=lambda i3=item_3: self.logika.tambahkan_ke_kalkulasi(i3),
                width=5
            ).grid(row=i, column=0, padx=2, pady=2)

        # Frame 4 = Simbol lainnya
        for i, item_4 in enumerate(self.sisa):
            tk.Button(
                master=self.frame_4,
                text=item_4,
                command=lambda i4=item_4: self.logika.tambahkan_ke_kalkulasi(i4),
                width=5
            ).grid(row=0, column=i, padx=2, pady=2)

        # Frame 5 = Soal 1.2
        for i, item_5 in enumerate(self.soal_12):
            tk.Button(
                master=self.frame_5,
                text="^" if item_5 == "**" else (
                    "mod" if item_5 == "%" else (
                        "√" if item_5 == "**(1/" else item_5
                    )),
                command=lambda i5=item_5: self.logika.tambahkan_ke_kalkulasi(i5),
                width=5
            ).grid(row=0, column=i, padx=2, pady=2)

        self.tombol_sama_dengan = tk.Button(
            master=self.frame_4,
            text="=",
            command=self.logika.evaluasi_kalkulasi,
            width=6
        )
        self.tombol_sama_dengan.grid(row=0, column=3, padx=2, pady=2)

        self.tombol_backspace = tk.Button(
            master=self.frame_6,
            text="⌫",
            command=self.logika.backspace,
            width=5,
        )
        self.tombol_backspace.grid(row=2, column=0, padx=2, pady=2)

        self.tombol_clear = tk.Button(
            master=self.frame_6,
            text="C",
            command=self.logika.bersihkan_text,
            width=5
        )
        self.tombol_clear.grid(row=2, column=1, padx=2, pady=2)

        # ===== Bind Enter untuk mengeksekusi ===== #
        self.base.bind(
            "<Return>", lambda event: self.logika.evaluasi_kalkulasi()
        )

    def jalankan(self):
        self.base.mainloop()


if __name__ == "__main__":
    tampilkan = Tampilan()
    tampilkan.jalankan()
