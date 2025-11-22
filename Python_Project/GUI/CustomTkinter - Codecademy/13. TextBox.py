import customtkinter as ctk

from os import path
from tkinter import PhotoImage


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.app_icon = None
        self.title("TabView")
        self.resizable(width=False, height=False)
        self.grid_columnconfigure(index=0, weight=1)

        self.images()
        self.center_window_predefined(width=500, height=360)

        self.thing = ""

        # Text Box.
        self.tbox = ctk.CTkTextbox(
            master=self,
            width=480,
            height=280,
            font=("Roboto", 14, "normal")
        )
        self.tbox.grid(row=0, column=0, padx=10, pady=10)

        self.frame = ctk.CTkFrame(master=self)
        self.frame.grid(row=1, column=0, padx=0, pady=0)

        self.button_delete = ctk.CTkButton(
            master=self.frame,
            text="Delete",
            font=("Roboto", 14, "normal"),
            width=80,
            command=lambda: self.tbox.delete(index1=0.0, index2="end")
        )
        self.button_delete.grid(row=0, column=0, padx=10, pady=10)

        self.button_copy = ctk.CTkButton(
            master=self.frame,
            text="Copy",
            font=("Roboto", 14, "normal"),
            width=80,
            command=self.copy_func
        )
        self.button_copy.grid(row=0, column=1, padx=10, pady=10)

        self.button_paste = ctk.CTkButton(
            master=self.frame,
            text="Paste",
            font=("Roboto", 14, "normal"),
            width=80,
            command=self.paste_func
        )
        self.button_paste.grid(row=0, column=2, padx=10, pady=10)

    def copy_func(self): self.thing = self.tbox.get(0.0, "end")

    def paste_func(self): self.tbox.insert(index="end", text=self.thing)

    def images(self):
        """ Store images and Icons """
        self.app_icon = PhotoImage(
            file=path.join(path.dirname(__file__), "Assets", "logo_python.png")
        )
        self.iconphoto(True, self.app_icon)

    def center_window_predefined(self, width, height):
        """
        Centers the window on the screen with a specified width and height.
        In this structure, 'self' refers to the main CTk window.
        """
        # Access screen dimensions directly via 'self' (the window object)
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Calculate x and y coordinates for the window to be centered
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)

        # Set the window's geometry directly via 'self'
        self.geometry(f"{width}x{height}+{x}+{y}")


if __name__ == "__main__":
    app = App()
    app.mainloop()
