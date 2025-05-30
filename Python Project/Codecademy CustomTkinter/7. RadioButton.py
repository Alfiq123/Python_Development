import customtkinter as ctk

from os import path
from PIL import Image
from time import sleep
from tkinter import PhotoImage

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.image_pizza = None
        self.app_icon = None
        self.title("Radio Button")
        self.resizable(width=False, height=False)

        self.images()
        self.icon_and_images()
        self.center_window(width=325, height=325)

        self.label = ctk.CTkLabel(
            master=self,
            text="Do you like Pizza?",
            font=("Roboto", 14, "normal"),
            image=self.image_pizza,
            compound="top"
        )
        self.label.pack(padx=10, pady=10)

        # Radio Button.
        self.radio_var = ctk.StringVar(value="other")
        self.radio1 = ctk.CTkRadioButton(  # Yes
            master=self,
            text="Yes I Do",
            font=("Roboto", 14, "normal"),
            value="yes",
            variable=self.radio_var,
            command=self.radio_status,
            corner_radius=5
        )
        self.radio1.pack(padx=10, pady=10)

        self.radio2 = ctk.CTkRadioButton(  # No
            master=self,
            text="No I Don't",
            font=("Roboto", 14, "normal"),
            value="no",
            variable=self.radio_var,
            command=self.radio_status,
            corner_radius=5
        )
        self.radio2.pack(padx=10, pady=10)

        self.radio3 = ctk.CTkRadioButton(  # Unsure
            master=self,
            text="What?",
            font=("Roboto", 14, "normal"),
            value="what",
            variable=self.radio_var,
            command=self.radio_status,
            corner_radius=5
        )
        self.radio3.pack(padx=10, pady=10)

        self.button_destroy = ctk.CTkButton(
            master=self,
            text="Destroy",
            font=("Roboto", 14, "normal"),
            command=self.clear_window,
            state="disabled"
        )
        self.button_destroy.pack(padx=10, pady=10)

        self.labelout = ctk.CTkLabel(
            master=self,
            text="",
            font=("Roboto", 14, "normal")
        )
        self.labelout.pack(padx=10, pady=10)

    def radio_status(self):
        if self.radio_var.get() == "yes":
            self.labelout.configure(text="You May Enter")
            self.button_destroy.configure(state="normal")
        elif self.radio_var.get() == "no":
            self.labelout.configure(text="You Cannot Enter")
            self.button_destroy.configure(state="disabled")
        else:
            self.labelout.configure(text="Who Don't Know Pizza?")
            self.button_destroy.configure(state="disabled")

    def clear_window(self):
        for widget in self.winfo_children():
            widget.destroy()
            widget.update_idletasks()
            sleep(0.5)
        self.destroy()
        print("HAHAHAHAHAHA...")

    def icon_and_images(self):
        self.image_pizza = ctk.CTkImage(
            dark_image=Image.open(
                path.join(path.dirname(__file__), "Assets", "image_pizza.png")
            ), size=(64, 64)
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
