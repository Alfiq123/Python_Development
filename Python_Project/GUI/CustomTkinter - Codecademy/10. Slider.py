import customtkinter as ctk

from os import path
from tkinter import PhotoImage

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.app_icon = None
        self.title("Slider")
        self.resizable(width=False, height=False)
        self.grid_columnconfigure(index=0, weight=1)

        self.images()
        self.center_window(window=self, width=325, height=256)


        # The Slider.
        self.slide = ctk.CTkSlider(
            master=self,
            from_=0,
            to=100,
            command=self.slider_func,
            number_of_steps=20
        )
        self.slide.set(0)
        self.slide.grid(row=0, column=0, padx=10, pady=10)

        self.label = ctk.CTkLabel(
            master=self,
            text="",
            font=("Roboto", 14, "normal"),
        )
        self.label.grid(row=1, column=0, padx=10, pady=10)


    def slider_func(self, value):
        self.label.configure(text=int(value))


    def images(self):
        """ Store images and Icons """
        self.app_icon = PhotoImage(
            file=path.join(path.dirname(__file__), "Assets", "logo_python.png")
        )
        self.iconphoto(True, self.app_icon)

    @staticmethod
    def center_window(window, width, height):
        """
        Centers the window on the screen with a specified width and height.
        In this structure, 'self' refers to the main CTk window.
        """
        # Access screen dimensions directly via 'self' (the window object)
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        # Calculate x and y coordinates for the window to be centered
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)

        # Set the window's geometry directly via 'self'
        window.geometry(f"{width}x{height}+{x}+{y}")

if __name__ == "__main__":
    app = App()
    app.mainloop()
