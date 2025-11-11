import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.config(background="#E8E8E8")  # #191919
        self.title("Tkinter - Window")
        self.geometry("256x256")


if __name__ == "__main__":
    app = App()
    app.mainloop()
