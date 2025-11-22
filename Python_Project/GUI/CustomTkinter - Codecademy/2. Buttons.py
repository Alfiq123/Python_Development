import tkinter as tk
import customtkinter as ctk

from os import path
from PIL import Image

app = ctk.CTk()
app.title("Buttons")
app.resizable(width=False, height=False)


icon_power = ctk.CTkImage(
    dark_image=Image.open(
        path.join(path.dirname(__file__), "Assets", "icon_power.png")
    ), size=(16, 16)
)

icon_reset = ctk.CTkImage(
    dark_image=Image.open(
        path.join(path.dirname(__file__), "Assets", "icon_reset.png")
    ), size=(16, 16)
)


# Change label status.
def change_label():
    label.configure(text="Status Off")
    button.configure(state="disabled", image=None, width=32)

# Reset the button.
def reset_button():
    label.configure(text="Status On")
    button.configure(state="normal", image=icon_power, width=32)


label = ctk.CTkLabel(
    master=app,
    text="Status On",
    font=("Arial", 14, "normal")
)
label.grid(padx=10, pady=10, row=0, column=0, columnspan=2)

button = ctk.CTkButton(
    master=app,
    text="",
    command=change_label,
    image=icon_power,
    fg_color="white",
    width=32,
)
button.grid(padx=10, pady=10, row=1, column=0)

button_reset = ctk.CTkButton(
    master=app,
    text="",
    font=("Arial", 14, "normal"),
    command=reset_button,
    fg_color="white",
    image=icon_reset,
    width=32
)
button_reset.grid(padx=10, pady=10, row=1, column=1)

app_icon = tk.PhotoImage(
    file=path.join(path.dirname(__file__), "Assets", "logo_python.png"))
app.iconphoto(True, app_icon)

app.mainloop()
