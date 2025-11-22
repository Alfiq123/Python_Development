import customtkinter as ctk

from os import path
from tkinter import PhotoImage


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.app_icon = None
        self.title("Switch")
        self.resizable(width=False, height=False)
        self.grid_columnconfigure(index=0, weight=1)

        self.images()
        self.center_window_predefined(width=300, height=280)

        self.onbutton = ctk.CTkButton(
            master=self,
            text="Turn On",
            font=("roboto", 14, "normal"),
            command=self.switchon_func
        )
        self.onbutton.grid(row=0, column=0, padx=10, pady=10)

        # The Switch.
        self.switch_var = ctk.StringVar(value="on")
        self.switch = ctk.CTkSwitch(
            master=self,
            text="Key A",
            font=("roboto", 14, "normal"),
            onvalue="on",
            offvalue="off",
            command=self.switch_func,
            variable=self.switch_var,
            state="disabled"
        )
        self.switch.grid(row=1, column=0, padx=10, pady=10)

        self.switch2_var = ctk.StringVar(value="on")
        self.switch2 = ctk.CTkSwitch(
            master=self,
            text="Key B",
            font=("roboto", 14, "normal"),
            onvalue="on",
            offvalue="off",
            command=self.switch_func,
            variable=self.switch2_var,
            state="disabled"
        )
        self.switch2.grid(row=2, column=0, padx=10, pady=10)

        self.switch3_var = ctk.StringVar(value="on")
        self.switch3 = ctk.CTkSwitch(
            master=self,
            text="Key C",
            font=("roboto", 14, "normal"),
            onvalue="on",
            offvalue="off",
            command=self.switch_func,
            variable=self.switch3_var,
            state="disabled"
        )
        self.switch3.grid(row=3, column=0, padx=10, pady=10)

        self.label = ctk.CTkLabel(
            master=self,
            text="LOCKED",
            font=("roboto", 14, "normal")
        )
        self.label.grid(row=4, column=0, padx=10, pady=10)

        self.button = ctk.CTkButton(
            master=self,
            text="Self Destruct",
            font=("roboto", 14, "normal"),
            command=lambda: self.button.destroy(),
            state="disabled",
            fg_color="grey"
        )
        self.button.grid(row=5, column=0, padx=10, pady=10)

    def switchon_func(self):
        self.switch.configure(state="normal")
        self.switch2.configure(state="normal")
        self.switch3.configure(state="normal")
        self.onbutton.configure(state="disabled", fg_color="grey")

    def switch_func(self):
        if (
            self.switch.get() == "on" and
            self.switch2.get() == "off" and
            self.switch3.get() == "off"
        ):
            self.label.configure(text="UNLOCKED")
            self.button.configure(state="normal", fg_color="#1f6aa5")
        else:
            self.label.configure(text="LOCKED")
            self.button.configure(state="disabled")

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
