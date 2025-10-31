import tkinter as tk
import customtkinter as ctk

from os import path
from PIL import Image

app = ctk.CTk()
app.geometry("300x300")
app.title("The Buttons")
app.resizable(width=False, height=False)

photo = ctk.CTkImage(
    dark_image=Image.open(
        path.join(path.dirname(__file__), "Assets", "icon_like.png")
    ), size=(32, 32)
)

click = 0


def click_button():
    global click
    click += 1
    print(f"Like: {click}")


button = ctk.CTkButton(
    master=app,
    text="Like Button",
    command=click_button,
    font=("Roboto", 14, "normal"),
    image=photo,
    compound="bottom"
)
button.pack(padx=10, pady=10)

app_icon = tk.PhotoImage(
    file=path.join(path.dirname(__file__), "Assets", "icon_python.png")
)
app.iconphoto(True, app_icon)

app.mainloop()
