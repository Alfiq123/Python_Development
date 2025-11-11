import ttkbootstrap as ttk


class App(ttk.Window):
    def __init__(self):
        super().__init__(themename="cosmo")

        self.title("Contoh 0803")

        self.my_frame = ttk.Frame(master=self)
        self.my_frame.grid(padx=10, pady=10)

        self.my_label_1 = ttk.Label(master=self.my_frame, text="Nama")
        self.my_label_1.grid(row=0, padx=10)

        self.my_label_2 = ttk.Label(master=self.my_frame, text="Alamat")
        self.my_label_2.grid(row=1, padx=10)

        self.my_entry_1 = ttk.Entry(master=self.my_frame, width=40)
        self.my_entry_1.grid(row=0, column=1)

        self.my_entry_2 = ttk.Entry(master=self.my_frame, width=40)
        self.my_entry_2.grid(row=1, column=1)


if __name__ == "__main__":
    app = App()
    app.mainloop()
