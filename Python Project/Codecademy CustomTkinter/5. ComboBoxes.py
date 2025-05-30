import customtkinter as ctk

from os import path
# from PIL import Image
from tkinter import PhotoImage


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.app_icon = None
        self.title("ComboBoxes")
        self.grid_columnconfigure(index=0, weight=1)

        self.images()
        self.center_window_predefined(width=256, height=256)

        self.label_title = ctk.CTkLabel(
            master=self,
            text="Color Chooser",
            font=("Roboto", 24, "bold")
        )
        self.label_title.grid(
            padx=10, pady=10,
            row=0, column=0,
            columnspan=2
        )

        # The ComboBox.
        self.choices = ["Red", "Green", "Blue", "Yellow", "Orange"]
        self.combo = ctk.CTkComboBox(
            master=self,
            values=self.choices,
            command=self.color_picker
        )
        self.combo.grid(
            padx=10, pady=10,
            row=1, column=0
        )

        # Confirmation Button.
        self.button = ctk.CTkButton(
            master=self,
            text="Confirm",
            font=("Roboto", 14, "normal"),
            command=self.color_picker_button
        )
        self.button.grid(
            padx=10, pady=10,
            row=2, column=0
        )

        # Frame to hold color buttons and center them
        cbutton_frame = ctk.CTkFrame(master=self, fg_color="transparent")
        cbutton_frame.grid(row=3, column=0, columnspan=2, pady=10)

        # Cyan Button.
        self.button_cyan = ctk.CTkButton(
            master=cbutton_frame,
            text="",
            command=lambda: self.configure(fg_color="Cyan"),
            width=32,
            fg_color="Cyan"
        )
        self.button_cyan.grid(
            padx=10,
            row=0, column=0
        )

        # Antique Button
        self.button_chocolate = ctk.CTkButton(
            master=cbutton_frame,
            text="",
            command=lambda: self.configure(fg_color="Chocolate"),
            width=32,
            fg_color="Chocolate"
        )
        self.button_chocolate.grid(
            padx=10,
            row=0, column=1
        )

        # Azure Button
        self.button_azure = ctk.CTkButton(
            master=cbutton_frame,
            text="",
            command=lambda: self.configure(fg_color="Azure"),
            width=32,
            fg_color="Azure"
        )
        self.button_azure.grid(
            padx=10,
            row=0, column=2
        )

        self.label_output = ctk.CTkLabel(
            master=self,
            text="",
            font=("Roboto", 24, "bold"),
        )
        self.label_output.grid(
            padx=10, pady=10,
            row=4, column=0
        )

    def color_picker(self, choice):
        self.label_output.configure(text=choice)

    def color_picker_button(self):
        self.configure(fg_color=self.combo.get())
        self.label_output.configure(
            text=self.combo.get(),
            text_color=self.combo.get()
        )

        self.label_output.configure(
            text=self.combo.get(),
            text_color=self.combo.get()
        )

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
