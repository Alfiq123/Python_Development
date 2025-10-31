import customtkinter as ctk

from os import path
from tkinter import PhotoImage

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.image_pizza = None
        self.app_icon = None
        self.title("Scrollables")
        self.resizable(width=False, height=False)

        self.images()
        self.center_window(width=256, height=256)

        self.scroll = ctk.CTkScrollableFrame(master=self)
        self.scroll.pack(padx=10, pady=10)

        for _ in range(20):
            ctk.CTkButton(
                master=self.scroll,
                text="Button"
            ).pack(
                padx=10,
                pady=10
            )

    def images(self):
        """ Store images and Icons """
        self.app_icon = PhotoImage(
            file=path.join(path.dirname(__file__), "Assets", "logo_python.png")
        )
        self.iconphoto(True, self.app_icon)

    def center_window(self, width, height):
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