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
        self.center_window_predefined(width=300, height=300)

        # TabView.
        self.tab = ctk.CTkTabview(master=self, height=280)
        self.tab.grid(row=0, column=0, padx=10, pady=10)

        self.tab_1 = self.tab.add("Tommy")
        self.tab_2 = self.tab.add("Carl")
        self.tab_3 = self.tab.add("Claude")

        self.tab_2.grid_columnconfigure(0, weight=1)

        self.tab_button = ctk.CTkButton(
            master=self.tab_2,
            text="Inside",
            font=("Roboto", 14, "normal")
        ).grid(row=0, column=0, padx=10, pady=10)

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
