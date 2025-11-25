from tkinter import messagebox
import mysql.connector
import ttkbootstrap as ttk


class App:
    def __init__(self):
        self.base = ttk.Window(themename="darkly")
        self.base.title("Biodata Sederhana")
        self.base.resizable(width=False, height=False)

        # Menghubungkan Database
        try:
            self.db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="apache_123",
                database="Biodata"
            )
            self.dbcursor = self.db.cursor()
        except mysql.connector.Error as e:
            messagebox.showerror(
                title="Error Database",
                message=f"Gagal terhubung ke database:\n{e}"
            )
            self.base.destroy()
            return

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
        self.frame_tombol = ttk.Frame(master=self.frame_1)
        self.frame_tombol.grid(row=2, column=0, padx=10, pady=10)

        # === Frame 6 -- Cari ===
        self.frame_cari = ttk.Frame(master=self.frame_1)
        self.frame_cari.grid_forget()

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
        self.entry_nama = ttk.Entry(master=self.frame_2, width=30)
        self.entry_nama.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        # === Alamat ===
        ttk.Label(
            master=self.frame_2,
            text="Alamat"
        ).grid(row=2, column=0, padx=10, sticky="w")
        self.entry_alamat = ttk.Entry(master=self.frame_2, width=30)
        self.entry_alamat.grid(row=3, column=0, padx=10, pady=10, sticky="w")

        ## ==================== TOMBOL-TOMBOL UTAMA ==================== ##

        self.btn_tambah_data = ttk.Button(
            master=self.frame_tombol,
            text="Tambah Data",
            command=self.tambah_data, width=14
        )
        self.btn_tambah_data.grid(row=0, column=0, padx=5, pady=5)

        self.btn_edit_data = ttk.Button(
            master=self.frame_tombol,
            text="Edit Data",
            width=14,
            command=self.edit_data
        )
        self.btn_edit_data.grid(row=0, column=1, padx=5, pady=5)

        self.btn_hapus_data = ttk.Button(
            master=self.frame_tombol,
            text="Hapus Data",
            width=14,
            command=self.hapus_data,
            bootstyle="warning"
        )
        self.btn_hapus_data.grid(row=0, column=2, padx=5, pady=5)

        self.btn_cari_data = ttk.Button(
            master=self.frame_tombol,
            text="Cari Data",
            width=14,
            command=self.show_cari_ui
        )
        self.btn_cari_data.grid(row=1, column=1, padx=5, pady=5)

        # ===== EDIT UI ===== #
        ttk.Label(
            master=self.frame_4,
            text="Update Nama"
        ).grid(row=1, columnspan=2, padx=10, sticky="w")
        self.entry_edit_nama = ttk.Entry(master=self.frame_4, width=30)
        self.entry_edit_nama.grid(row=2, columnspan=2, padx=10, pady=10)

        ttk.Label(
            master=self.frame_4,
            text="Update Alamat"
        ).grid(row=3, columnspan=2, padx=10, sticky="w")
        self.entry_edit_alamat = ttk.Entry(master=self.frame_4, width=30)
        self.entry_edit_alamat.grid(row=4, columnspan=2, padx=10, pady=10)

        self.btn_confirm = ttk.Button(
            master=self.frame_tombol,
            text="Konfirmasi",
            width=14,
            command=self.edit_data_confirm
        )
        self.btn_cancel = ttk.Button(
            master=self.frame_tombol,
            text="Cancel",
            width=14,
            command=self.edit_data_cancel
        )

        # ===== CARI UI ===== #

        ttk.Label(
            master=self.frame_cari,
            text="Cari Berdasarkan Nama:"
        ).grid(row=0, column=0, columnspan=3, sticky="w", padx=10)
        self.entry_cari = ttk.Entry(master=self.frame_cari, width=30)
        self.entry_cari.grid(row=1, column=0, padx=10, pady=10)

        # Bind tombol Enter
        self.entry_cari.bind(
            "<Return>", lambda event: self.lakukan_pencarian()
        )

        # Tombol Eksekusi Cari
        self.btn_eksekusi_cari = ttk.Button(
            master=self.frame_cari,
            text="Cari",
            bootstyle="success",
            command=self.lakukan_pencarian
        )
        self.btn_eksekusi_cari.grid(row=1, column=1, padx=5)

        # Tombol Tutup Cari (Reset)
        self.btn_tutup_cari = ttk.Button(
            master=self.frame_cari,
            text="X",
            bootstyle="danger-outline",
            command=self.tutup_cari
        )
        self.btn_tutup_cari.grid(row=1, column=2, padx=5)

    ## ==================== FUNGSI-FUNGSI ==================== ##

    def tambah_data(self):
        nama = self.entry_nama.get()
        alamat = self.entry_alamat.get()
        if nama or alamat:
            sql = """
                INSERT INTO `Bio` (`nama`, `alamat`) 
                VALUES (%s, %s)
            """
            val = (nama, alamat)

            self.dbcursor.execute(sql, val)
            messagebox.showinfo(
                title="Informasi",
                message="Data Berhasil Ditambahkan"
            )
        else:
            messagebox.showwarning(
                title="Peringatan",
                message="Nama atau Alamat Tidak Boleh Kosong"
            )
            return

        self.db.commit()
        self.refresh_data()

    def edit_data(self):
        self.btn_confirm.grid(row=1, column=0, padx=10, pady=10)
        self.btn_cancel.grid(row=1, column=2, padx=10, pady=10)
        self.frame_4.grid(row=0, column=1, padx=10, pady=10, sticky="w")
        self.toggle_tombol_utama("disabled")

    def edit_data_confirm(self):
        nama = self.entry_nama.get()
        n_nama = self.entry_edit_nama.get()
        n_alamat = self.entry_edit_alamat.get()

        if n_nama or n_alamat:
            sql = """
                UPDATE `Bio` 
                SET `nama` = %s, `alamat` = %s 
                WHERE `nama` = %s
            """
            val = (n_nama, n_alamat, nama)

            self.dbcursor.execute(sql, val)
            messagebox.showinfo(
                title="Informasi",
                message="Data Berhasil Diubah"
            )
        else:
            messagebox.showwarning(
                title="Peringatan",
                message="Data Baru Tidak Boleh Kosong"
            )
            return

        self.db.commit()
        self.refresh_data()
        self.edit_data_cancel()

    def edit_data_cancel(self):
        self.btn_confirm.grid_forget()
        self.btn_cancel.grid_forget()
        self.frame_4.grid_forget()
        self.toggle_tombol_utama("enabled")

    def hapus_data(self):
        nama = self.entry_nama.get()
        if nama:
            confirm = messagebox.askyesno(
                title="Konfirmasi",
                message=f"Yakin ingin menghapus data {nama}?"
            )
            if confirm:
                sql = """
                    DELETE FROM `Bio` 
                    WHERE `nama` = %s
                """
                val = (nama,)

                self.dbcursor.execute(sql, val)
                messagebox.showinfo(
                    title="Informasi",
                    message="Data Berhasil Dihapus"
                )
                self.entry_nama.delete(first=0, last="end")
                self.entry_alamat.delete(first=0, last="end")
        else:
            messagebox.showwarning(
                title="Peringatan",
                message="Pilih data dari tabel terlebih dahulu!"
            )
            return

        self.db.commit()
        self.refresh_data()

    # === FUNGSI CARI DATA ===
    def show_cari_ui(self):
        self.frame_cari.grid(row=3, column=0, padx=10, pady=10)
        self.entry_cari.focus()  # Langsung fokus ke kolom ketik
        self.toggle_tombol_utama("disabled")

    def lakukan_pencarian(self):
        keyword = self.entry_cari.get()

        # Bersihkan tabel saat ini
        for item in self.tabel.get_children():
            self.tabel.delete(item)

        sql = """
            SELECT `id`, `nama`, `alamat` 
            FROM `Bio` 
            WHERE `nama` LIKE %s OR `alamat` LIKE %s
        """
        val = (f"%{keyword}%", f"%{keyword}%")

        self.dbcursor.execute(sql, val)
        results = self.dbcursor.fetchall()

        if results:
            for row in results:
                self.tabel.insert(parent="", index="end", values=row)
        else:
            messagebox.showinfo(
                title="Info",
                message="Data tidak ditemukan."
            )

    def tutup_cari(self):
        self.entry_cari.delete(first=0, last="end")
        self.frame_cari.grid_forget()
        self.refresh_data()  # Kembalikan semua data
        self.toggle_tombol_utama("enabled")

    def refresh_data(self):
        self.dbcursor.execute("SELECT `id`, `nama`, `alamat` FROM `Bio`")

        for item in self.tabel.get_children():
            self.tabel.delete(item)
        for row in self.dbcursor.fetchall():
            self.tabel.insert(parent="", index="end", values=row)

    def klik_tabel(self, event):
        baris = self.tabel.focus()

        if not baris: return
        data = self.tabel.item(item=baris)["values"]
        if not data: return

        self.entry_nama.delete(first=0, last="end")
        self.entry_alamat.delete(first=0, last="end")
        self.entry_nama.insert(index=0, string=str(data[1]))
        self.entry_alamat.insert(index=0, string=str(data[2]))

    def toggle_tombol_utama(self, state):
        status = "normal" if state == "enabled" else "disabled"
        self.btn_tambah_data.configure(state=status)
        self.btn_edit_data.configure(state=status)
        self.btn_hapus_data.configure(state=status)
        self.btn_cari_data.configure(state=status)

    def jalankan(self):
        self.base.mainloop()


if __name__ == "__main__":
    app = App()
    app.jalankan()
