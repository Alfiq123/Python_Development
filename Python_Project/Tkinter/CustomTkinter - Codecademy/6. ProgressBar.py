import customtkinter as ctk

from os import path
from tkinter import PhotoImage

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.app_icon = None
        self.title("Progress Bar")
        self.resizable(width=False, height=False)
        self.center_window(width=256, height=256)

        self.images()
        self.grid_columnconfigure(index=0, weight=1)

        self.label = ctk.CTkLabel(
            master=self,
            text="My Progress",
            font=("Roboto", 24, "normal")
        )
        self.label.grid(padx=10, pady=10, row=0, column=0)

        # Prograss Bar.
        self.progress = ctk.CTkProgressBar(
            master=self,
            orientation="horizontal",
            mode="determinate",
            determinate_speed=0.25
        )
        self.progress.grid(padx=10, pady=10, row=1, column=0)
        self.progress.set(value=1)  # Set Progress Bar.

        # Frames for holding the button.
        self.frames = ctk.CTkFrame(
            master=self,
            fg_color="transparent"
        )
        self.frames.grid(
            row=2, column=0,
            columnspan=2,
            padx=10, pady=10
        )

        # Start Button.
        self.start_button = ctk.CTkButton(
            master=self.frames,
            text="Start",
            font=("Roboto", 14, "normal"),
            command=lambda: self.progress.start(),
            width=64
        )
        self.start_button.grid(
            padx=10, pady=10,
            row=0, column=0
        )

        # Stop Button.
        self.stop_button = ctk.CTkButton(
            master=self.frames,
            text="Stop",
            font=("Roboto", 14, "normal"),
            command=lambda: self.progress.stop(),
            width = 64
        )
        self.stop_button.grid(
            padx=10, pady=10,
            row=0, column=1
        )

        # Step Button.
        self.step_button = ctk.CTkButton(
            master=self.frames,
            text="Step",
            font=("Roboto", 14, "normal"),
            command=lambda: self.progress.step(),
            width = 64
        )
        self.step_button.grid(
            padx=10, pady=10,
            row=1, column=0,
            columnspan=2
        )

        self.labelout = ctk.CTkLabel(
            master=self,
            text="Output",
            font=("Roboto", 14, "normal")
        )
        self.labelout.grid(
            padx=10, pady=10,
            row=3, column=0
        )

    def button_func(self):
        self.progress.step()
        # self.label.configure(text=self.progress.get())

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
