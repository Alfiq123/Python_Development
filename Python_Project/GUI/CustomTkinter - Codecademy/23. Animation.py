import customtkinter as ctk

from os import path
from tkinter import PhotoImage

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.app_icon = None
        self.title("Object Oriented")
        self.resizable(width=False, height=False)
        self.grid_columnconfigure(index=0, weight=1)

        self.images()
        self.center_window_predefined(width=700, height=500)

        self.y_co = 500 / 2 + 400
        self.font = ctk.CTkFont(family="Roboto", size=14, weight="normal")

        self.frame = ctk.CTkFrame(master=self)
        self.frame.grid(row=0, column=0, padx=10, pady=10)

        self.button_up = ctk.CTkButton(
            master=self.frame,
            text="up",
            font=self.font,
            command=self.up
        )
        self.button_up.grid(row=0, column=0, padx=10, pady=10)

        self.button_down = ctk.CTkButton(
            master=self.frame,
            text="Down",
            font=self.font,
            command=self.down
        )
        self.button_down.grid(row=0, column=1, padx=10, pady=10)

        self.tbox = ctk.CTkTextbox(
            master=self,
            width=500,
            height=300
        )
        self.tbox.place(x=700 / 2, y=self.y_co, anchor="center")

    # Up the Widget.
    def up(self):
        self.y_co -= 20

        if self.y_co >= 250:
            self.tbox.place(x=700 / 2, y=self.y_co, anchor="center")
            self.after(ms=10, func=self.up)

    # Down the Widget.
    def down(self):
        self.y_co += 20

        if self.y_co <= 800:
            self.tbox.place(x=700 / 2, y=self.y_co, anchor="center")
            self.after(ms=10, func=self.down)

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
