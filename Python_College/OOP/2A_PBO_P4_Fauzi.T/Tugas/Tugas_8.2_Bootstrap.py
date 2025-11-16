import ttkbootstrap as ttk


class Perhitungan:
    """Kelas untuk melakukan perhitungan pesanan"""

    def __init__(self, aplikasi):
        self.aplikasi = aplikasi

    def tambah_pesanan(self, nama_menu):
        """Memasukkan pesanan ke tabel baru"""
        for item in self.aplikasi.menu:
            if item["nama"] == nama_menu:
                self.aplikasi.keranjang.append({
                    "nama": item["nama"],
                    "harga": item["harga"]
                })
                break

        self.perbarui_tabel_pesanan()

    def perbarui_tabel_pesanan(self):
        """Memperbarui pesanan dari tabel & melakukan perhitungan"""
        for row in self.aplikasi.tabel_pesanan.get_children():
            self.aplikasi.tabel_pesanan.delete(row)

        for item in self.aplikasi.keranjang:
            self.aplikasi.tabel_pesanan.insert(
                parent="", index="end",
                values=(item["nama"], f"Rp {item['harga']:,.0f}")
            )

        total = sum(item["harga"] for item in self.aplikasi.keranjang)
        total_harga = total + (total * 0.10) + 1000

        self.aplikasi.label_total.config(
            text=f"Total: Rp {total_harga:,.0f}"
        )


class Aplikasi:
    """Kelas untuk tampilan program (GUI)"""

    def __init__(self):
        self.base = ttk.Window(themename="cosmo")
        self.base.title("Kafe Nusa")
        self.base.resizable(width=False, height=False)

        self.perhitungan = Perhitungan(aplikasi=self)

        self.keranjang = []

        self.menu = [
            {"no": 1, "nama": "Tea", "harga": 5000},
            {"no": 2, "nama": "Coffee", "harga": 8000},
            {"no": 3, "nama": "Sandwich", "harga": 15000},
            {"no": 4, "nama": "Cake", "harga": 22000},
            {"no": 5, "nama": "Burger", "harga": 22000},
            {"no": 6, "nama": "Pizza", "harga": 35000},
            {"no": 7, "nama": "Fanta", "harga": 8000},
            {"no": 8, "nama": "Sprite", "harga": 8000}
        ]
        self.nama_menu = [
            ("Tea", "Coffee", "Sandwich", "Cake"),
            ("Burger", "Pizza", "Fanta", "Sprite")
        ]

        # Frame 1
        self.frame_1 = ttk.Frame(master=self.base)
        self.frame_1.grid(row=0, column=0, padx=10, pady=10)

        # Frame 2
        self.frame_2 = ttk.Frame(master=self.base)
        self.frame_2.grid(row=1, column=0, padx=10, pady=10)

        # Frame 3
        self.frame_3 = ttk.Frame(master=self.base)
        self.frame_3.grid(row=2, column=0, padx=10, pady=10)

        self.label_judul = ttk.Label(
            master=self.frame_1,
            text="Cafe Nusa",
            font=("Helvetica", 24, "bold")
        )
        self.label_judul.grid(row=0, columnspan=2)

        self.tabel_kolom = ["no", "menu", "harga"]
        self.tabel = ttk.Treeview(
            master=self.frame_1,
            columns=self.tabel_kolom,
            show="headings",
            bootstyle="info"
        )

        self.tabel.heading(column="no", text="No")
        self.tabel.heading(column="menu", text="Menu")
        self.tabel.heading(column="harga", text="Harga")

        self.tabel.column(column="no", width=80)
        self.tabel.column(column="menu", width=80)
        self.tabel.column(column="harga", width=80)

        for menu in self.menu:
            harga = f"Rp {menu['harga']:,}"
            self.tabel.insert(
                parent="",
                index="end",
                values=(menu["no"], menu["nama"], harga)
            )

        self.tabel.grid(row=1, column=0, padx=10, pady=10)

        self.tabel_pesanan = ttk.Treeview(
            master=self.frame_1,
            columns=["nama", "harga"],
            show="headings",
            bootstyle="success",
        )

        self.tabel_pesanan.heading("nama", text="Menu")
        self.tabel_pesanan.heading("harga", text="Harga")

        self.tabel_pesanan.column("nama", width=120)
        self.tabel_pesanan.column("harga", width=80)

        self.tabel_pesanan.grid(row=1, column=1, padx=10, pady=10)

        for i, baris in enumerate(self.nama_menu):
            for j, nama in enumerate(baris):
                ttk.Button(
                    master=self.frame_2,
                    text=nama,
                    width=8,
                    command=lambda nm=nama: self.perhitungan.tambah_pesanan(nm)
                ).grid(row=i, column=j, padx=2, pady=2)

        # Label Total Harga
        self.label_total = ttk.Label(
            master=self.frame_3,
            text="Total: Rp 0",
            font=("Arial", 12, "bold")
        )
        self.label_total.grid(row=0, column=0, pady=10)

    def jalankan(self):
        self.base.mainloop()


if __name__ == "__main__":
    apk = Aplikasi()
    apk.jalankan()
