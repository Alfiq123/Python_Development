import tkinter as tk
import customtkinter as ctk

from os import path

def button_callback():
    print("button clicked")

app = ctk.CTk()
app.title("Introduction")
app.resizable(width=False, height=False)

button = ctk.CTkButton(master=app, text="My Button", command=button_callback)
button.pack(padx=10, pady=10)

app_icon = tk.PhotoImage(
    file=path.join(path.dirname(__file__),"Assets", "logo_python.png"))
app.iconphoto(True, app_icon)

app.mainloop()
