import customtkinter as ctk


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Contoh 0801")

        window_frame = ctk.CTkFrame(master=self)
        window_frame.pack()

        window_label = ctk.CTkLabel(master=window_frame, text="Primary Key", font=("Helvetica", 14, "bold"))
        window_label.pack(padx=64, pady=64)


if __name__ == "__main__":
    app = App()
    app.mainloop()
