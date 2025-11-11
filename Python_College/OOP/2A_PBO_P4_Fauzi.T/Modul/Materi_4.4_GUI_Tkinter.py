import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("300x230")
        self.title("Contoh 0804")

        ## self.my_frame = tk.Frame(master=self)
        ## self.my_frame.pack(padx=10, pady=10)

        self.my_label_1 = tk.Label(master=self, text="Widget 1", background="cyan")
        self.my_label_2 = tk.Label(master=self, text="Widget 2", background="magenta")
        self.my_label_3 = tk.Label(master=self, text="Widget 3", background="yellow")

        self.my_label_1.place(x=50, y=20)
        self.my_label_2.place(relx=0.5, rely=0.5, anchor="center")
        self.my_label_3.place(x=150, y=150, width=100, height=50)


if __name__ == "__main__":
    app = App()
    app.mainloop()
