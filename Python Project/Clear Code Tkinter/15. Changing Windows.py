import tkinter as tk
import customtkinter as ctk
from tkinter import ttk

# Application
app = ctk.CTk()
app.title("Custom")
app.resizable(width = False, height = False)

# Appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")



# * Label
label = ctk.CTkLabel(master = app, text = "Login", font = ("Seoge UI", 24))
label.pack(pady = 10, padx = 10)

# * Entry
entry = ctk.CTkEntry(master = app, placeholder_text = "Name...", font = ("Seoge UI", 12))
entry.pack(pady = 10, padx = 10)

# * Button
button = ctk.CTkButton(master = app, text = "Proceed", font = ("Seoge UI", 12))
button.pack(pady = 10, padx = 10)

# * Checkbutton
check = ctk.CTkCheckBox(master = app, text = "Remember Me")
check.pack(pady = 10, padx = 10)

# * Window Attribute
# ! Doesn't Works on Linux
# app.attributes("-alpha", 0.5)

# // Works Well (Useless)
# app.attributes("-topmost" , True)
# app.attributes("-fullscreen", True)

# ! Windows Only
# app.attributes("-disable", True) 
# app.attributes("-toolwindow", True)

# * Security Event
app.bind("<Escape>", lambda event: app.destroy())

# ? Title Bar - Why would i use it?
# app.overrideredirect(True)
# grip = ttk.Sizegrip(master = app)
# grip.place(relx = 1.0, rely = 1.0, anchor = "se")


# TODO: Start window in the middle of the screen
# app_width = 512
# app_height = 512

# NOTE: Alternative
app.update_idletasks()

app_width = app.winfo_width()
app_height = app.winfo_height()

# Get screen width and height
display_width = app.winfo_screenwidth()
display_height = app.winfo_screenheight()

left = (display_width / 2) - (app_width / 2)
top = (display_height / 2) - (app_height / 2)

# left = (display_width // 2) - (app_width // 2)
# top = (display_height // 2) - (app_height // 2)

app.geometry(f"{app_width}x{app_height}+{int(left)}+{int(top)}")



# App Icon
app_icon = tk.PhotoImage(file="Python_Intermediate/Python Project/Assets/Icon_Python.png")
app.iconphoto(True, app_icon)

# Run
app.mainloop()
