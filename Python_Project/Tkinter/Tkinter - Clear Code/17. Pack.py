import tkinter as tk
import ttkbootstrap as ttk
import customtkinter as ctk

# Setup
app = ctk.CTk()
app.title("Layout")
app.resizable(width = False, height = False)

# Centering
window_width = 512
window_height = 512

screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

left = (screen_width // 2) - (window_width // 2)
top = (screen_height // 2) - (window_height // 2)

app.geometry(f"{window_width}x{window_height}+{left}+{top}")

# Widget
label1 = ctk.CTkLabel(master = app, text = "First Label", fg_color = "red")
label2 = ctk.CTkLabel(master = app, text = "Second Label", fg_color = "blue")
label3 = ctk.CTkLabel(master = app, text = "Third Label", fg_color = "green")
button = ctk.CTkButton(master = app, text = "Button", width = 25)
button2 = ctk.CTkButton(master = app, text = "Button 2", width = 25)

# * Exercise 1
# label1.pack(side = "top", fill = "both")
# label2.pack(side = "top", expand = True)
# label3.pack(side = "top", expand = True, fill = "both")
# button.pack(side = "top", fill = "x")

# Layout
# label1.pack(ipadx = 10, ipady = 10, padx = 10, pady = 10)
# label2.pack(ipadx = 10, ipady = 10, padx = 10, pady = 10)
# label3.pack(ipadx = 10, ipady = 10, padx = 10, pady = 10)
# button.pack(ipadx = 10, ipady = 10, padx = 10, pady = 10)
# button2.pack(ipadx = 5, ipady = 10, padx = 10, pady = 10)

# * Exercise 2
label1.pack(side = "top", expand = True, fill = "both", padx = 10, pady = 10)
label2.pack(side = "left", expand = True, fill = "both")
label3.pack(side = "top", expand = True, fill = "both", ipadx = 10)
button.pack(side = "top", expand = True, fill = "both", ipadx = 10)

# Icon
app_icon = tk.PhotoImage(file="Python_Intermediate/Python Project/Assets/Icon_Python.png")
app.iconphoto(True, app_icon)

# Run
app.mainloop()