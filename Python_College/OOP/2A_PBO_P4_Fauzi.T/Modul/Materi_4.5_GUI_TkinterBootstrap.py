import ttkbootstrap as ttk


class App(ttk.Window):
    def __init__(self):
        super().__init__()

        self.myLabel = ttk.Label(self, text="Click a Button")
        self.myLabel.pack(pady=10)

        self.title("Contoh 0805")

        self.my_frame = ttk.Frame(master=self)
        self.my_frame.pack(padx=10, pady=10)

        self.my_button_1 = ttk.Button(
            master=self.my_frame,
            text="ALFA",
            command=self.aksi_tombol_alfa
        )
        self.my_button_1.pack(pady=10)

        self.my_button_2 = ttk.Button(
            master=self.my_frame,
            text="INDO",
            command=self.aksi_tombol_indo
        )
        self.my_button_2.pack(pady=10)

        self.grup_rabu = ttk.IntVar(value=2)

        self.my_radio_button_1 = ttk.Radiobutton(
            master=self.my_frame,
            text="Berwarna",
            command=self.aksi_rabu,
            variable=self.grup_rabu,
            value=1
        )
        self.my_radio_button_1.pack()

        self.my_radio_button_2 = ttk.Radiobutton(
            master=self.my_frame,
            text="Tidak Berwarna",
            command=self.aksi_rabu,
            variable=self.grup_rabu,
            value=2
        )
        self.my_radio_button_2.pack()

    def aksi_tombol_alfa(self):
        self.myLabel.configure(text="Alfamart")
        self.aksi_rabu()

    def aksi_tombol_indo(self):
        self.myLabel.configure(text="Indomaret")
        self.aksi_rabu()

    def aksi_rabu(self):
        if self.grup_rabu.get() == 1:

            if self.myLabel.cget("text") == "Alfamart":
                self.myLabel.configure(background="red")

            elif self.myLabel.cget("text") == "Indomaret":
                self.myLabel.configure(background="light blue")

        else:
            self.myLabel.configure(background=self.cget("background"))


if __name__ == "__main__":
    app = App()
    app.mainloop()
