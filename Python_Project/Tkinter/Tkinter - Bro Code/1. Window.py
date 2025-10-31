import tkinter as tk
import customtkinter as ctk

from os import path

app = ctk.CTk()                           # Initialize
app.geometry("300x300")                   # Size of the window.
app.title("The Window")                   # Title name of the window.
app.resizable(width=False, height=False)  # Make the window unresizeable.

app_icon = tk.PhotoImage(                 # `os.path` to fix path problem.
    file=path.join(path.dirname(__file__), "Assets", "icon_python.png")
)
app.iconphoto(True, app_icon)

app.config(background="#222831")          # Change Background.

app.mainloop()                            # Place window on computer screen.
