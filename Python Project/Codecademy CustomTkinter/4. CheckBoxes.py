import customtkinter as ctk

from os import path
from PIL import Image
from tkinter import PhotoImage


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.app_icon = None


    def images(self):
        self.app_icon = PhotoImage(
            file=path.join(path.dirname(__file__), "Assets", "logo_python.png")
        )
        self.iconphoto(True, self.app_icon)


if __name__ == "__main__":
    app = App()
    app.mainloop()
