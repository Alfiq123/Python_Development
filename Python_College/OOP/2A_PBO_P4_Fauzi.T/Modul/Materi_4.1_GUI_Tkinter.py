import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Contoh 0801")

        self.window_frame = tk.Frame(master=self)
        self.window_frame.pack()

        self.window_label = tk.Label(master=self.window_frame, text="Contoh 0801", font=("TImes New Roman", 12))
        self.window_label.pack(padx=64, pady=64)


if __name__ == "__main__":
    app = App()
    app.mainloop()
