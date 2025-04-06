import tkinter as tk
import ttkbootstrap as ttk

"""
So far, the master was always the window But this isn't always what you want.
A menu item should have a menu as the master.
A tab entry should have a tab widget as the master.
For complex layouts, you can also create a container widget to organise your widgets.

ttk.Frame
Is just an empty widget
You place widgets inside of it and then you place the frame
That way you can arrange widgets easily
"""

# App
app = ttk.Window(themename = "cosmo")
app.title("Frame and Parenting")
app.resizable(width = False, height = False)


# Frame
frame = ttk.Frame(
    master = app, 
    relief = "groove", 
    borderwidth = 1
)
# frame.pack_propagate(False) # Enable "Width" and "Height"
frame.pack(padx = 10, pady = 10, side = "left")

# Master Setting
label = ttk.Label(
    master = frame, 
    text = "Sunken Master", 
    font = ("Segoe UI", "12")
)
label.pack(padx = 10, pady = 10)

button = ttk.Button(
    master = frame, 
    text = "Button Frame"
)
button.pack(padx = 10, pady = 10)

# Example
label2 = ttk.Label(
    master = app, 
    text = "Flat Master", 
    font = ("Segoe UI", "12")
)
label2.pack(padx = 10, pady = 10)

# --- #

# Exercise
# create another frame with a label, a button and an entry and place it to the right
# of the other widgets

exercise_frame = ttk.Frame(master = app, relief = "groove", borderwidth = 1)
exercise_frame.pack(padx = 10, pady = 10, side = "right")

ttk.Label(master = exercise_frame, text = "Exercise Frame", font = ("Segoe UI", "12")).pack(padx = 10, pady = 10)
ttk.Button(master = exercise_frame, text = "Exercise Button").pack(padx = 10, pady = 10)
ttk.Entry(master = exercise_frame, text = "Exercise Entry").pack(padx = 10, pady = 10)


# Window Icon
app_icon = tk.PhotoImage(file="Python_Intermediate/Python Project/Icon_Python.png")
app.iconphoto(True, app_icon)

# Loop
app.mainloop()
