import customtkinter as ctk


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.myLabel = ctk.CTkLabel(self, text="Click a Button")
        self.myLabel.pack(pady=10)

        self.title("Contoh 0805")

        self.my_frame = ctk.CTkFrame(master=self)
        self.my_frame.pack(padx=10, pady=10)

        self.my_button_1 = ctk.CTkButton(
            master=self.my_frame,
            text="ALFA",
            command=self.aksi_tombol_alfa
        )
        self.my_button_1.pack(pady=10)

        self.my_button_2 = ctk.CTkButton(
            master=self.my_frame,
            text="INDO",
            command=self.aksi_tombol_indo
        )
        self.my_button_2.pack(pady=10)

        self.grup_rabu = ctk.IntVar(value=2)

        self.my_radio_button_1 = ctk.CTkRadioButton(
            master=self.my_frame,
            text="Berwarna",
            command=self.aksi_rabu,
            variable=self.grup_rabu,
            value=1
        )
        self.my_radio_button_1.pack()

        self.my_radio_button_2 = ctk.CTkRadioButton(
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
                self.myLabel.configure(bg_color="red")

            elif self.myLabel.cget("text") == "Indomaret":
                self.myLabel.configure(bg_color="light blue")

        else:
            self.myLabel.configure(bg_color="transparent")


if __name__ == "__main__":
    app = App()
    app.mainloop()
