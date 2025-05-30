import customtkinter as ctk

from os import path
from tkinter import PhotoImage


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.app_icon = None
        self.title("Input Dialog Popup")
        self.resizable(width=False, height=False)
        self.grid_columnconfigure(index=0, weight=1)

        self.images()
        self.center_window_predefined(width=200, height=100)

        self.button = ctk.CTkButton(
            master=self,
            text="Level 1",
            font=("Roboto", 14, "normal"),
            command=self.level_1
        )
        self.button.grid(row=0, column=0, padx=10, pady=10)

        self.label = ctk.CTkLabel(
            master=self,
            text="",
            font=("Roboto", 14, "normal")
        )
        self.label.grid(row=1, column=0, padx=10, pady=10)

    def level_1(self):
        level_1_w = ctk.CTkToplevel()
        level_1_w.title("Level 1")
        level_1_w.geometry("200x200")
        level_1_w.grid_columnconfigure(index=0, weight=1)
        self.button.configure(state="disabled")

        def level_2():
            level_2_w = ctk.CTkToplevel()
            level_2_w.title("Level 2")
            level_2_w.geometry("200x200")
            level_2_w.grid_columnconfigure(index=0, weight=1)
            level_1_button.configure(state="disabled")

            def level_3():
                level_3_w = ctk.CTkToplevel()
                level_3_w.title("Level 3")
                level_3_w.geometry("200x200")
                level_3_w.grid_columnconfigure(index=0, weight=1)
                level_2_button.configure(state="disabled")

                level_3_button = ctk.CTkButton(
                    master=level_3_w,
                    text="Level 3",
                    font=("Roboto", 14, "normal")
                )
                level_3_button.grid(row=0, column=0, padx=10, pady=10)

            level_2_button = ctk.CTkButton(
                master=level_2_w,
                text="Level 2",
                font=("Roboto", 14, "normal"),
                command=level_3
            )
            level_2_button.grid(row=0, column=0, padx=10, pady=10)

        level_1_button = ctk.CTkButton(
            master=level_1_w,
            text="Level 1",
            font=("Roboto", 14, "normal"),
            command=level_2
        )
        level_1_button.grid(row=0, column=0, padx=10, pady=10)

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
