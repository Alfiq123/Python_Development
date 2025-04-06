import tkinter as tk
import ttkbootstrap as ttk

"""
• The widget is called tk.Menu.
• You use several of them and nest them... a lot.
• If you place a tk.Menu inside of another tk.Menu it becomes one option.
• For a sub menu, you would place a menu inside of a menu inside of another menu.
"""

# App
app = ttk.Window(themename = "journal")
app.title("Tab Widget")
app.resizable(width = False, height = False)


# Menus
menu = tk.Menu(master = app)
app.configure(menu = menu)


# File Menu
file_menu = tk.Menu(master = menu, tearoff = False)
menu.add_cascade(label = "File", menu = file_menu)
file_menu.add_command(label = "Open", command = lambda: print("Open File"))
file_menu.add_command(label = "Save", command = lambda: print("Save File"))
file_menu.add_separator()
file_menu.add_command(label = "Exit", command = app.quit)

# Edit Menu
edit = tk.Menu(master = menu, tearoff = False)
menu.add_cascade(label = "Edit", menu = edit)
edit.add_command(label = "Undo", command = lambda: print("Undo Changes"))
edit.add_command(label = "Redo", command = lambda: print("Redo Changes"))
edit.add_separator()
edit.add_command(label = "Destroy", command = app.destroy)

# Help Menu
help_menu = tk.Menu(master = menu, tearoff = False)
menu.add_cascade(label = "Help", menu = help_menu)

help_menu_str = tk.StringVar(value = "on")
help_menu.add_checkbutton(label = "Check Button 1", onvalue = "on", offvalue = "off", variable = help_menu_str)
help_menu.add_checkbutton(label = "Check Button 2", onvalue = "on", offvalue = "off", variable = help_menu_str)
help_menu.add_radiobutton(label = "Radio Button 1")
help_menu.add_radiobutton(label = "Radio Button 2")

# Menu Button
menu_button = ttk.Menubutton(master = app, text = "Menu Button")
menu_button.pack(padx = 30, pady = 30)

menu_button_menu = tk.Menu(master = menu_button, tearoff = False)

# menu_button.configure(menu = menu_button_menu)
menu_button["menu"] = menu_button_menu # Alternative

menu_button_menu.add_command(label = "Menu Button 1", command = lambda: print("Menu Button 1"))
menu_button_menu.add_command(label = "Menu Button 2", command = lambda: print("Menu Button 2"))
menu_button_menu.add_separator()
menu_button_menu.add_checkbutton(label = "Check Button 3")
menu_button_menu.add_checkbutton(label = "Check Button 4")

# --- #

# Exercise
# TODO: add another menu to the main menu, this one should have a sub menu
# TODO: try to read the website below and add a submenu
# TODO: docs: https://www.tutorialspoint.com/python/tk_menu.htm

exercise_menu = tk.Menu(master = menu, tearoff = False)
menu.add_cascade(label = "Exercise", menu = exercise_menu)
exercise_menu.add_command(label = "Exercise Menu 1", command = lambda: print("Exercise Menu 1"))

exercise_submenu = tk.Menu(master = exercise_menu, tearoff = False)
exercise_menu.add_cascade(label = "Exercise Sub Menu", menu = exercise_submenu)

exercise_submenu.add_command(label = "Exercise Sub Menu 1", command = lambda: print("Exercise Sub Menu 1"))
exercise_submenu.add_command(label = "Exercise Sub Menu 2", command = lambda: print("Exercise Sub Menu 2"))
exercise_submenu.add_separator()
exercise_submenu.add_checkbutton(label = "Exercise Sub Menu Check Button 3")


# App Icon
app_icon = tk.PhotoImage(file="Python_Intermediate/Python Project/Icon_Python.png")
app.iconphoto(True, app_icon)

# App Loop
app.mainloop()
