import customtkinter as ctk

from os import path
# from PIL import Image
from tkinter import PhotoImage


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.app_icon = None
        self.title("CheckBoxes")
        self.resizable(width=False, height=False)

        self.images()
        self.center_window_predefined(width=300, height=300)

        # Actual CheckBoxes.
        self.check_var = ctk.StringVar(value="off")
        self.check = ctk.CTkCheckBox(
            master=self,
            text="Intercontinental Ballistic Missile?",
            text_color_disabled="red",
            font=("Roboto", 14, "normal"),
            variable=self.check_var,
            onvalue="on",
            offvalue="off",
            corner_radius=10
        )
        self.check.pack(padx=10, pady=10)

        # Submit Button.
        self.button = ctk.CTkButton(
            master=self,
            text="Confirm",
            font=("Roboto", 14, "normal"),
            command=self.check_button
        )
        self.button.pack(padx=10, pady=10)

        # Select Button.
        self.button_select = ctk.CTkButton(
            master=self,
            text="Select",
            font=("Roboto", 14, "normal"),
            command=lambda: self.check.select()
        )
        self.button_select.pack(padx=10, pady=10)

        # De-Select Button.
        self.button_deselect = ctk.CTkButton(
            master=self,
            text="Deselect",
            font=("Roboto", 14, "normal"),
            command=lambda: self.check.deselect()
        )
        self.button_deselect.pack(padx=10, pady=10)

        # Toggle Button.
        self.button_toogle = ctk.CTkButton(
            master=self,
            text="Toggle",
            font=("Roboto", 14, "normal"),
            command=lambda: self.check.toggle()
        )
        self.button_toogle.pack(padx=10, pady=10)

        self.label = ctk.CTkLabel(
            master=self,
            text="",
            font=("Roboto", 14, "normal"),
        )
        self.label.pack(padx=10, pady=10)

    def images(self):
        """ Store images and Icons """
        self.app_icon = PhotoImage(
            file=path.join(path.dirname(__file__), "Assets", "logo_python.png")
        )
        self.iconphoto(True, self.app_icon)

    def check_button(self):
        """ CheckBox Condition """
        if self.check_var.get() == "on":
            self.label.configure(text="TACTICAL NUKE INCOMING!")
            self.check.configure(
                text="WHAT HAVE YOU DONE?",
                fg_color="red",
                text_color="red",
                state="disabled",
                font=("Roboto", 18, "normal")
            )
            self.button.configure(state="disabled", fg_color="red")
            self.button_select.configure(state="disabled", fg_color="red")
            self.button_toogle.configure(state="disabled", fg_color="red")
            self.button_deselect.configure(state="disabled", fg_color="red")
        else:
            self.label.configure(text="PEACE")

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
        print(f"Window centered at: {x},{y} with size {width}x{height}")


if __name__ == "__main__":
    app = App()
    app.mainloop()
