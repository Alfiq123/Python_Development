import tkinter as tk
from tkinter import ttk


class Perhitungan:
    def __init__(self, aplikasi):
        self.aplikasi = aplikasi

class Aplikasi:
    def __init__(self):
        self.base = tk.Tk()
        self.base.title("Kafe Nusa")
        self.base.resizable(width=False, height=False)

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

        self.frame_1 = tk.Frame(master=self.base)
        self.frame_1.grid(row=0, column=0, padx=10, pady=10)

        self.frame_2 = tk.LabelFrame(
            master=self.base,
            text=" Tombol Menu ",
            labelanchor="n",
            borderwidth=2,
            padx=5,
            pady=5,
            relief="sunken"
        )
        self.frame_2.grid(row=1, column=0, padx=10, pady=10)

        self.frame_3 = tk.Frame(master=self.base)
        self.frame_3.grid(row=2, column=0, padx=10, pady=10)

        self.tabel_kolom = ["no", "menu", "harga"]
        self.tabel = ttk.Treeview(
            master=self.frame_1,
            columns=self.tabel_kolom,
            show="headings"
        )

        self.tabel.heading(column="no", text="No")
        self.tabel.heading(column="menu", text="Menu")
        self.tabel.heading(column="harga", text="Harga")

        self.tabel.column(column="no", width=80)
        self.tabel.column(column="menu", width=80)
        self.tabel.column(column="harga", width=80)

        self.tabel.insert(
            parent="",
            index="end",
            values=(1, "Tea", "Rp 5,000")
        )
        self.tabel.insert(
            parent="",
            index="end",
            values=(2, "Coffee", "Rp 8,000")
        )
        self.tabel.insert(
            parent="",
            index="end",
            values=(3, "Sandwich", "Rp 15,000")
        )
        self.tabel.insert(
            parent="",
            index="end",
            values=(4, "Cake", "Rp 22,000")
        )
        self.tabel.insert(
            parent="",
            index="end",
            values=(5, "Burger", "Rp 22,000")
        )
        self.tabel.insert(
            parent="",
            index="end",
            values=(6, "Pizza", "Rp 35,000")
        )
        self.tabel.insert(
            parent="",
            index="end",
            values=(7, "Fanta", "Rp 8,000")
        )
        self.tabel.insert(
            parent="",
            index="end",
            values=(8, "Sprite", "Rp 8,000")
        )

        self.tabel.grid(row=0, column=0, padx=10, pady=10)

        self.tabel_pesanan = ttk.Treeview(
            master=self.frame_1,
            columns=["nama", "harga"],
            show="headings"
        )

        self.tabel_pesanan.heading("nama", text="Menu")
        self.tabel_pesanan.heading("harga", text="Harga")

        self.tabel_pesanan.column("nama", width=120)
        self.tabel_pesanan.column("harga", width=80)

        self.tabel_pesanan.grid(row=0, column=1, padx=10, pady=10)

        # Tea
        self.tombol_tea = tk.Button(
            master=self.frame_2,
            text="Tea",
            width=8,
            command=lambda: self.tambah_pesanan("Tea")

        )
        self.tombol_tea.grid(row=0, column=0, padx=2, pady=2)

        # Coffee
        self.tombol_coffee = tk.Button(
            master=self.frame_2,
            text="Coffee",
            width=8,
            command=lambda: self.tambah_pesanan("Coffee")
        )
        self.tombol_coffee.grid(row=0, column=1, padx=2, pady=2)

        # Sandwich
        self.tombol_sandwich = tk.Button(
            master=self.frame_2,
            text="Sandwich",
            width=8,
            command=lambda: self.tambah_pesanan("Sandwich")
        )
        self.tombol_sandwich.grid(row=0, column=2, padx=2, pady=2)

        # Cake
        self.tombol_cake = tk.Button(
            master=self.frame_2,
            text="Cake",
            width=8,
            command = lambda: self.tambah_pesanan("Cake")
        )
        self.tombol_cake.grid(row=0, column=3, padx=2, pady=2)

        # Burger
        self.tombol_burger = tk.Button(
            master=self.frame_2,
            text="Burger",
            width=8,
            command=lambda: self.tambah_pesanan("Burger")
        )
        self.tombol_burger.grid(row=1, column=0, padx=2, pady=2)

        # Pizza
        self.tombol_pizza = tk.Button(
            master=self.frame_2,
            text="Pizza",
            width=8,
            command=lambda: self.tambah_pesanan("Pizza")
        )
        self.tombol_pizza.grid(row=1, column=1, padx=2, pady=2)

        # Fanta
        self.tombol_fanta = tk.Button(
            master=self.frame_2,
            text="Fanta",
            width=8,
            command=lambda: self.tambah_pesanan("Fanta")
        )
        self.tombol_fanta.grid(row=1, column=2, padx=2, pady=2)

        # Sprite
        self.tombol_sprite = tk.Button(
            master=self.frame_2,
            text="Sprite",
            width=8,
            command=lambda: self.tambah_pesanan("Sprite")
        )
        self.tombol_sprite.grid(row=1, column=3, padx=2, pady=2)

        # Label Total Harga
        self.label_total = tk.Label(
            master=self.frame_3,
            text="Total: Rp 0",
            font=("Arial", 12, "bold")
        )
        self.label_total.grid(row=0, column=0, pady=10)

    def tambah_pesanan(self, nama_menu):
        for item in self.menu:
            if item["nama"] == nama_menu:
                self.keranjang.append({
                    "nama": item["nama"],
                    "harga": item["harga"]
                })
                break

        self.perbarui_tabel_pesanan()

    def perbarui_tabel_pesanan(self):
        for row in self.tabel_pesanan.get_children():
            self.tabel_pesanan.delete(row)

        for item in self.keranjang:
            self.tabel_pesanan.insert(
                parent="", index="end",
                values=(item["nama"], f"Rp {item['harga']:,.0f}")
            )

        total = sum(item["harga"] for item in self.keranjang)
        total_harga = total + (total * 0.10) + 1000

        self.label_total.config(text=f"Total: Rp {total_harga:,.0f}")

    def jalankan(self):
        self.base.mainloop()

if __name__ == "__main__":
    apk = Aplikasi()
    apk.jalankan()
