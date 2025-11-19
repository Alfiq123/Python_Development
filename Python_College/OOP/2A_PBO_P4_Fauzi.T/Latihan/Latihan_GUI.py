from tkinter import messagebox
import mysql.connector
import ttkbootstrap as ttk


class App:
    def __init__(self):
        self.base = ttk.Window(themename="darkly")
        self.base.title("Biodata Sederhana")
        self.base.resizable(width=False, height=False)

        # Menghubungkan Database
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="apache_123",
            database="Biodata"
        )
        self.dbcursor = self.db.cursor()

        ## ==================== FRAME ==================== ##

        # === Frame 1 -- Tabel ===
        self.frame_1 = ttk.Frame(master=self.base)
        self.frame_1.grid(row=0, column=0, padx=20, pady=20)

        # === Frame 2 -- Entry + Update ===
        self.frame_tengah = ttk.Frame(master=self.frame_1)
        self.frame_tengah.grid(row=1, column=0)

        # === Frame 3 -- Label & Entry ===
        self.frame_2 = ttk.Frame(master=self.frame_tengah)
        self.frame_2.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        # === Frame 4 -- Edit Data ===
        self.frame_4 = ttk.Frame(master=self.frame_tengah)
        self.frame_4.grid_forget()

        # === Frame 5 -- Tombol ===
        self.frame_3 = ttk.Frame(master=self.frame_1)
        self.frame_3.grid(row=2, column=0, padx=10, pady=10)

        ## ==================== WIDGET-WIDGET ==================== ##

        # === Tabel ===
        self.tabel_kolom = ["ID", "Nama", "Alamat"]
        self.tabel = ttk.Treeview(
            master=self.frame_1,
            columns=self.tabel_kolom,
            show="headings",
            bootstyle="info",
        )

        for kol in self.tabel_kolom:
            self.tabel.heading(column=kol, text=kol)
            self.tabel.column(column=kol, width=150)

        self.refresh_data()

        self.tabel.grid(row=0, column=0)
        self.tabel.bind(sequence="<ButtonRelease-1>", func=self.klik_tabel)

        # === Nama ===
        ttk.Label(
            master=self.frame_2,
            text="Nama"
        ).grid(row=0, column=0, padx=10, sticky="w")

        self.entry_nama = ttk.Entry(
            master=self.frame_2,
            width=30
        )
        self.entry_nama.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        # === Alamat ===
        ttk.Label(
            master=self.frame_2,
            text="Alamat"
        ).grid(row=2, column=0, padx=10, sticky="w")

        self.entry_alamat = ttk.Entry(
            master=self.frame_2,
            width=30
        )
        self.entry_alamat.grid(row=3, column=0, padx=10, pady=10, sticky="w")

        ## ==================== TOMBOL-TOMBOL ==================== ##

        # === Tombol -- Tambah ===
        self.btn_tambah_data = ttk.Button(
            master=self.frame_3,
            text="Tambah Data",
            command=self.tambah_data,
            width=14,
        )
        self.btn_tambah_data.grid(row=0, column=0, padx=5, pady=5)

        # === Tombol -- Edit ===
        self.btn_edit_data = ttk.Button(
            master=self.frame_3,
            text="Edit Data",
            width=14,
            command=self.edit_data
        )
        self.btn_edit_data.grid(row=0, column=1, padx=5, pady=5)

        # === Tombol -- Hapus ===
        self.btn_hapus_data = ttk.Button(
            master=self.frame_3,
            text="Hapus Data",
            width=14,
            command=self.hapus_data,
            bootstyle="warning"
        )
        self.btn_hapus_data.grid(row=0, column=2, padx=5, pady=5)

        # === Tombol -- Cari ===
        self.btn_cari_data = ttk.Button(
            master=self.frame_3,
            text="Cari Data",
            width=14,
            state="disabled",
            bootstyle="disabled"
        )
        self.btn_cari_data.grid(row=1, column=1, padx=5, pady=5)

        # # === Tombol -- Kosongkan Tabel ===
        # self.btn_kosongkan_data = ttk.Button(
        #     master=self.frame_3,
        #     text="Kosongkan Tabel",
        #     command=self.kosongkan_tabel,
        #     width=14,
        #     bootstyle="danger",
        #     state="disabled"
        # )
        # self.btn_kosongkan_data.grid(row=2, column=1, padx=5, pady=5)

        # ===== EDIT ===== #

        # === Edit Nama ===
        ttk.Label(
            master=self.frame_4,
            text="Update Nama"
        ).grid(row=1, columnspan=2, padx=10, sticky="w")

        self.entry_edit_nama = ttk.Entry(
            master=self.frame_4,
            width=30
        )
        self.entry_edit_nama.grid(row=2, columnspan=2, padx=10, pady=10)

        # === Edit Alamat ===
        ttk.Label(
            master=self.frame_4,
            text="Update Alamat"
        ).grid(row=3, columnspan=2, padx=10, sticky="w")

        self.entry_edit_alamat = ttk.Entry(
            master=self.frame_4,
            width=30
        )
        self.entry_edit_alamat.grid(row=4, columnspan=2, padx=10, pady=10)

        # === Tombol -- Confirm === #
        self.btn_confirm = ttk.Button(
            master=self.frame_3,
            text="Konfirmasi",
            width=14,
            command=self.edit_data_confirm
        )

        # === Tombol -- Cancel === #
        self.btn_cancel = ttk.Button(
            master=self.frame_3,
            text="Cancel",
            width=14,
            command=self.edit_data_cancel
        )

    ## ==================== FUNGSI-FUNGSI ==================== ##

    def tambah_data(self):
        nama = self.entry_nama.get()
        alamat = self.entry_alamat.get()

        if nama or alamat:
            self.dbcursor.execute(f"""
                INSERT INTO `Bio` (`nama`, `alamat`)
                VALUES ("{nama}", "{alamat}");
            """)
            messagebox.showinfo(
                title="Informasi",
                message="Data Berhasil Ditambahkan"
            )

        else:
            messagebox.showwarning(
                title="Peringatan",
                message="Nama atau Alamat Tidak Boleh Kosong"
            )
            raise ValueError("Nama atau Alamat Kosong")

        self.db.commit()
        self.refresh_data()

    def edit_data(self):
        """Mengedit Data"""
        self.btn_confirm.grid(row=1, column=0, padx=10, pady=10)
        self.btn_cancel.grid(row=1, column=2, padx=10, pady=10)
        self.frame_4.grid(row=0, column=1, padx=10, pady=10, sticky="w")
        self.btn_tambah_data.configure(state="disabled")
        self.btn_edit_data.configure(state="disabled")
        self.btn_hapus_data.configure(state="disabled")

    def edit_data_confirm(self):
        """Konfirmasi Edit Data"""
        nama = self.entry_nama.get()
        alamat = self.entry_alamat.get()
        n_nama = self.entry_edit_nama.get()
        n_alamat = self.entry_edit_alamat.get()

        if n_nama or n_alamat:
            self.dbcursor.execute(f"""
                UPDATE `Bio`
                SET `nama` = "{n_nama}", `alamat` = "{n_alamat}"
                WHERE `nama` = "{nama}" OR `alamat` = "{alamat}";         
            """)
            messagebox.showinfo(title="Informasi", message="Data Berhasil Diubah")
        else:
            messagebox.showwarning(title="Peringatan", message="Data Baru Tidak Boleh Kosong")
            raise ValueError("Data Baru Kosong")

        self.db.commit()
        self.refresh_data()

        self.btn_confirm.grid_forget()
        self.btn_cancel.grid_forget()
        self.frame_4.grid_forget()

        self.btn_tambah_data.configure(state="enabled")
        self.btn_edit_data.configure(state="enabled")
        self.btn_hapus_data.configure(state="enabled")

    def edit_data_cancel(self):
        self.btn_confirm.grid_forget()
        self.btn_cancel.grid_forget()
        self.frame_4.grid_forget()

        self.btn_tambah_data.configure(state="enabled")
        self.btn_edit_data.configure(state="enabled")
        self.btn_hapus_data.configure(state="enabled")

    def hapus_data(self):
        """Menghapus Data Dari Tabel"""
        nama = self.entry_nama.get()
        alamat = self.entry_alamat.get()

        if nama or alamat:
            self.dbcursor.execute(f"""
                DELETE FROM `Bio` 
                WHERE `nama` = "{nama}" OR `alamat` = "{alamat}";
            """)
            messagebox.showinfo(
                title="Informasi",
                message="Data Berhasil Dihapus"
            )

        else:
            messagebox.showwarning(
                title="Peringatan",
                message="Data Tidak Ada Yang Dipilih!"
            )
            raise ValueError("Data TIdak Terpilih!")

        self.entry_nama.delete(first=0, last="end")
        self.entry_alamat.delete(first=0, last="end")

        self.db.commit()
        self.refresh_data()

    def refresh_data(self):
        """Mengupdate Data Tabel"""
        self.dbcursor.execute("SELECT `id`, `nama`, `alamat` FROM `Bio`;")

        for item in self.tabel.get_children():
            self.tabel.delete(item)

        for row in self.dbcursor.fetchall():
            self.tabel.insert(parent="", index="end", values=row)

    def klik_tabel(self, event):
        """Mengisi entry ketika tabel di-klik"""
        baris = self.tabel.focus()
        if not baris: return

        data = self.tabel.item(item=baris)["values"]
        if not data: return

        self.entry_nama.delete(first=0, last="end")
        self.entry_alamat.delete(first=0, last="end")

        self.entry_nama.insert(index=0, string=data[1])
        self.entry_alamat.insert(index=0, string=data[2])

    # def kosongkan_tabel(self):
    #     self.dbcursor.execute("TRUNCATE TABLE `Bio`;")
    #     self.refresh_data()

    def jalankan(self):
        self.base.mainloop()


if __name__ == "__main__":
    app = App()
    app.jalankan()
