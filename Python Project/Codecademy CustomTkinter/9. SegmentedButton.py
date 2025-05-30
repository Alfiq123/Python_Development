import customtkinter as ctk

from os import path
from tkinter import PhotoImage

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.app_icon = None
        self.title("Segmented Button")
        self.resizable(width=False, height=False)
        self.grid_columnconfigure(index=0, weight=1)

        self.images()
        self.center_window(window=self, width=325, height=256)

        # Segmented.
        self.segmen = ctk.CTkSegmentedButton(
            master=self,
            values=["Apache", "PHP", "JavaScript", "MySQL", "Laravel"],
            font=("Roboto", 14, "normal"),
            command=self.segmen_func
        )
        self.segmen.grid(row=0, column=0, padx=10, pady=10)

        self.label = ctk.CTkLabel(
            master=self,
            text="Output",
            font=("Roboto", 14, "normal")
        )
        self.label.grid(row=1, column=0, padx=10, pady=10)

        self.button = ctk.CTkButton(
            master=self,
            text="New Window",
            font=("Roboto", 14, "normal"),
            command=self.button_func
        )
        self.button.grid(row=2, column=0, padx=10, pady=10)

    def segmen_func(self, value):
        if self.segmen.get() == "PHP":
            self.label.configure(text=f"FUCK {value}")
        elif self.segmen.get() == "Laravel":
            self.label.configure(text=f"FUCK {value}")
        else:
            self.label.configure(text=f"Hello {value}")

    def button_func(self):
        new_app = ctk.CTkToplevel()
        new_app.title("Info")

        toplevel_width = 300
        toplevel_height = 100
        self.center_window(new_app, toplevel_width, toplevel_height)

        new_label = ctk.CTkLabel(
            master=new_app,
            text="INFO: Programm Is Under Maintenance!",
            font=("Roboto", 14, "normal")
        )
        new_label.pack(padx=10, pady=10)

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