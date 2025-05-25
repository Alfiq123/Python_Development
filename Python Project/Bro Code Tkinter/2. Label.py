import tkinter as tk
import customtkinter as ctk

from os import path
from PIL import Image

app = ctk.CTk()
app.geometry("300x300")
app.title("The Label")
app.resizable(width=False, height=False)

photo = ctk.CTkImage(
	dark_image=Image.open(
        path.join(path.dirname(__file__), "Assets", "icon_desktop.png")
    ), size=(64,64)
)

label = ctk.CTkLabel(
    master=app,
    text="The Label",
    font=("Comic Sans MS", 24, "bold"),
    text_color="#DFD0B8",
    image=photo,
    compound="top",
)
label.pack(padx=10, pady=10)

app_icon = tk.PhotoImage(
    file=path.join(path.dirname(__file__), "Assets", "icon_python.png")
)
app.iconphoto(True, app_icon)

app.mainloop()
