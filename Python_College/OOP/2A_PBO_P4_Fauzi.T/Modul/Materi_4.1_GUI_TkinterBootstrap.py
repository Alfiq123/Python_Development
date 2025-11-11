import ttkbootstrap as ttk


class App(ttk.Window):
    def __init__(self):
        super().__init__(themename="cosmo")

        self.title("Contoh 0801")

        self.window_frame = ttk.Frame(master=self)
        self.window_frame.pack()

        self.window_label = ttk.Label(master=self.window_frame, text="Contoh 0801", font=("TImes New Roman", 24, "bold"))
        self.window_label.pack(padx=64, pady=64)


if __name__ == "__main__":
    app = App()
    app.mainloop()
