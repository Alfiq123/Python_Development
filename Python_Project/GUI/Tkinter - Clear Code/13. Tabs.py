import tkinter as tk
import ttkbootstrap as ttk

# App
app = ttk.Window(themename = "flatly")
app.title("Tab Widget")
app.resizable(width = False, height = False)


# Notebook Widget
notebook = ttk.Notebook(master = app)


tab1 = ttk.Frame(master = notebook)
label1 = ttk.Label(master = tab1, text = "Primary Tab 1")
label1.pack(padx = 10, pady = 10)
button1 = ttk.Button(master = tab1, text = "Primary Button")
button1.pack(padx = 10, pady = 10)

tab2 = ttk.Frame(master = notebook)
label2 = ttk.Label(master = tab2, text = "Secondary Tab 2")
label2.pack(padx = 10, pady = 10)
button2 = ttk.Button(master = tab2, text = "Secondary Button")
button2.pack(padx = 10, pady = 10)


notebook.add(tab1, text = "Tab 1")
notebook.add(tab2, text = "Tab 2")
notebook.pack(padx = 10, pady = 10)

# --- #

# Exercise
# Add another tab with 2 button and one label inside.

exercise_tab = ttk.Frame(master = notebook)

exercise_label = ttk.Label(master = exercise_tab, text = "Exercise Tab")
exercise_label.pack(padx = 10, pady = 10)

exercise_button1 = ttk.Button(master = exercise_tab, text = "Exercise Button 1")
exercise_button1.pack(padx = 10, pady = 10)

exercise_button2 = ttk.Button(master = exercise_tab, text = "Exercise Button 2")
exercise_button2.pack(padx = 10, pady = 10)

notebook.add(exercise_tab, text = "Exercise Tab")
notebook.pack(padx = 10, pady = 10)


# Window Icon
app_icon = tk.PhotoImage(file="Python_Intermediate/Python_Project/Assets/Icon_Python.png")
app.iconphoto(True, app_icon)

# Loop
app.mainloop()