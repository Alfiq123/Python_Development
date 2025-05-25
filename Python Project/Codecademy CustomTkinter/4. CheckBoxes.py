import customtkinter as ctk

from os import path
# from PIL import Image
from tkinter import PhotoImage


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.app_icon = None
        self.title("CheckBoxes")
        self.check_var = ctk.StringVar(value="off")

        self.check = ctk.CTkCheckBox(
            master=self,
            text="Howdy?",
            font=("Roboto", 14, "normal"),
            variable=self.check_var,
            onvalue="on",
            offvalue="off",
        )
        self.check.pack(padx=10, pady=10)

        self.button = ctk.CTkButton(
            master=self,
            text="ON",
            font=("Roboto", 14, "normal"),
            command=self.check_button
        )
        self.button.pack(padx=10, pady=10)

        self.label = ctk.CTkLabel(
            master=self,
            text="",
        )
        self.label.pack(padx=10, pady=10)

    def images(self):
        self.app_icon = PhotoImage(
            file=path.join(path.dirname(__file__), "Assets", "logo_python.png")
        )
        self.iconphoto(True, self.app_icon)

    def check_button(self):
        if self.check_var.get() == "on":
            self.label.configure(text="GAME ON")
        else:
            self.label.configure(text="GAME OFF")


if __name__ == "__main__":
    app = App()
    app.mainloop()
