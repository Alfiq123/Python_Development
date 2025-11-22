import tkinter as tk
import ttkbootstrap as ttk
from tkinter import scrolledtext

"""
Tkinter has a slider and a progress bar,
Both show progress in one dimension.

The slider can be moved by user
or set independently.

The progress bar can only be set
independently.
"""

app = ttk.Window(themename = "darkly")
app.title("Sliders")
app.resizable(width = False, height = False)


# Slider
scale_float = tk.DoubleVar(value = 15)
scale = ttk.Scale(
    master = app, 
    from_ = 0, 
    to = 100, 
    command = lambda value: print(scale_float.get()), 
    length = 128, 
    orient = "horizontal", 
    variable = scale_float
)
scale.pack(padx = 10, pady = 10)

# Progress Bar
progress = ttk.Progressbar(
    master = app, 
    variable = scale_float, 
    mode = "indeterminate", 
    maximum = 100, 
    orient = "horizontal", 
    length = 128
)
progress.pack(padx = 10, pady = 10)

# Scrolled Text
scrolled_text = scrolledtext.ScrolledText(
    master = app, 
    width = 32, 
    height = 5, 
)
scrolled_text.pack(padx = 10, pady = 10)

# Exercise
# Create a progress bar that is vertical, start automatically and also show the progress as a number.
# There should also be a scale slider that is affected by the progress bar.

exercise_progress_int = tk.IntVar(value = 0)
exercise_progress = ttk.Progressbar(master = app, orient = "vertical", variable = exercise_progress_int)
exercise_progress.pack(padx = 10, pady = 10)
exercise_progress.start()

exercise_label = ttk.Label(master = app, textvariable = exercise_progress_int)
exercise_label.pack(padx = 10, pady = 10)

exercise_scale = tk.DoubleVar(value = 0)
exercise_scale_slider = ttk.Scale(master = app, variable = exercise_progress_int, from_ = 0, to = 100)
exercise_scale_slider.pack(padx = 10, pady = 10)

# Window Icon
app_icon = tk.PhotoImage(file="Python_Intermediate/Python_Project/Assets/Icon_Python.png")
app.iconphoto(True, app_icon)

# Run
app.mainloop()