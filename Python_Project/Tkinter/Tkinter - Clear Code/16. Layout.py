import tkinter as tk
import ttkbootstrap as ttk
import customtkinter as ctk

# Application
app = ctk.CTk()
app.title("Layout")
app.geometry("512x512")
app.resizable(width = False, height = False)

# Appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


# * Widgets
label1 = ctk.CTkLabel(master = app, 
    text = "Label 1", 
    text_color = "#EBE8DB", 
    bg_color = "#D76C82", 
    corner_radius = 10, 
    width = 100, 
    height = 100
)
label2 = ctk.CTkLabel(master = app, 
    text = "Label 2", 
    text_color = "#EBE8DB", 
    bg_color = "#B03052", 
    corner_radius = 10, 
    width = 100, 
    height = 100
)

# * Pack
# label1.pack(pady = 10, padx = 10)
# label2.pack(pady = 10, padx = 10)

# * Grid
# app.columnconfigure(0, weight = 1)
# app.columnconfigure(1, weight = 1)
# app.columnconfigure(2, weight = 2)
# app.rowconfigure(0, weight = 1)
# app.rowconfigure(1, weight = 1)

# label1.grid(row = 0, column = 0, sticky = "nsew")
# label2.grid(row = 1, column = 1, columnspan = 2, sticky = "nsew")

# * Place
label1.place(x = 64, y = 64)
label2.place(relx = 0.5, rely = 0.5, relwidth = 0.5, relheight = 0.5, anchor = "center")


# App Icon
app_icon = tk.PhotoImage(file="Python_Intermediate/Python Project/Assets/Icon_Python.png")
app.iconphoto(True, app_icon)

# Run
app.mainloop()