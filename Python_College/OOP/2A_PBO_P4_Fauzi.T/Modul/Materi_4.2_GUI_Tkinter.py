import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Contoh 0802")

        self.my_frame = tk.Frame(master=self)
        self.my_frame.pack(padx=10, pady=10)

        self.my_button_1 = tk.Button(master=self.my_frame, text="TOMBOL1")
        self.my_button_2 = tk.Button(master=self.my_frame, text="TOMBOL2")
        self.my_button_3 = tk.Button(master=self.my_frame, text="TOMBOL3")
        self.my_button_4 = tk.Button(master=self.my_frame, text="TOMBOL4")
        self.my_button_5 = tk.Button(master=self.my_frame, text="TOMBOL5")
        self.my_button_6 = tk.Button(master=self.my_frame, text="TOMBOL6")

        self.my_button_1.pack(side="left", expand=1, fill="y")
        self.my_button_6.pack(side="right", expand=1, fill="y")
        self.my_button_2.pack(side="top", expand=1, fill="both", padx=6, pady=3)
        self.my_button_5.pack(side="bottom", expand=1, fill="both", padx=6, pady=3)
        self.my_button_4.pack(side="right", expand=1, fill="x", padx=6, pady=3)
        self.my_button_3.pack(side="left", expand=1, fill="x", padx=6, pady=3)


if __name__ == "__main__":
    app = App()
    app.mainloop()
