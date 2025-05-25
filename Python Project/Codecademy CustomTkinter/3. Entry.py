import customtkinter as ctk

from os import path
from PIL import Image
from tkinter import END, PhotoImage


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.app_icon = None
        self.icon_send, self.icon_exit, self.icon_clean = None, None, None
        self.icons_and_images()
        self.title("Entry")

        # Entry.
        self.entry = ctk.CTkEntry(
            master=self,
            font=("Roboto", 14, "normal"),
            placeholder_text="Enter Something...",
            corner_radius=16
        )
        self.entry.grid(padx=10, pady=10, row=0, column=0, columnspan=2)

        # Button Send and Exit.
        self.button = ctk.CTkButton(
            master=self,
            text="",
            command=self.button_func,
            image=self.icon_send,
            fg_color="white",
            width=32
        )
        self.button.grid(padx=10, pady=10, row=1, column=0)

        # Button Clear.
        self.button_clear = ctk.CTkButton(
            master=self,
            text="",
            command=self.button_clear_func,
            image=self.icon_clean,
            fg_color="white",
            width=32
        )
        self.button_clear.grid(padx=10, pady=10, row=1, column=1)

        # Label Empty
        self.label = ctk.CTkLabel(
            master=self,
            text="Hello",
            font=("Roboto", 14, "normal"),
        )
        self.label.grid(padx=10, pady=10, row=2, column=0, columnspan=2)

    def icons_and_images(self):
        # Main Icon.
        self.app_icon = PhotoImage(
            file=path.join(path.dirname(__file__), "Assets", "logo_python.png")
        )
        self.iconphoto(True, self.app_icon)

        # Icon for Send.
        self.icon_send = ctk.CTkImage(
            dark_image=Image.open(
                path.join(path.dirname(__file__), "Assets", "icon_send.png")
            ), size=(16, 16)
        )

        # Icon for Exit.
        self.icon_exit = ctk.CTkImage(
            dark_image=Image.open(
                path.join(path.dirname(__file__), "Assets", "icon_door.png")
            ), size=(16, 16)
        )

        # Icon for Clean.
        self.icon_clean = ctk.CTkImage(
            dark_image=Image.open(
                path.join(path.dirname(__file__), "Assets", "icon_clean.png")
            ), size=(16, 16)
        )

    # Main Button Function.
    def button_func(self):
        print(f"Send {self.entry.get()}")
        self.button.configure(image=self.icon_exit, command=quit)
        self.label.configure(text=f"Good Live {self.entry.get()}")

    # Clear Button Function.
    def button_clear_func(self):
        self.entry.delete(first_index=0, last_index=END)


if __name__ == "__main__":
    app = App()
    app.mainloop()
