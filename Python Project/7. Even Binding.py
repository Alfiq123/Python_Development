import tkinter as tk
import ttkbootstrap as ttk

app = ttk.Window(themename = "cosmo")
app.title("Even Binding")
app.resizable(width = False, height = False)



def get_position(event):
    print(f"x: {event.x} y: {event.y}")

# The Title.
title = ttk.Label(master = app, text = "Even Binding", font = ("Times New Roman", 14, "bold"))
title.pack(padx = 10, pady = 10)

# Text.
text = ttk.Text(master = app)
text.pack(padx = 10, pady = 10)

# Entry.
entry = ttk.Entry(master = app)
entry.pack(padx = 10, pady = 10)

# Button.
button = ttk.Button(master = app, text = "This Button")
button.pack(padx = 10, pady = 10)

# Events.
# button.bind("<Alt-KeyPress-a>", lambda event: print("Eventers!"))
# app.bind("<Motion>", get_position)
# text.bind("<Motion>", get_position)

# app.bind("<KeyPress>", lambda event: print(f"Button was pressed! ({event.char})"))

# Selecting Stuff.
entry.bind("<FocusIn>", lambda event: print(f"Entry was selected!"))
entry.bind("<FocusOut>", lambda event: print(f"Entry was unselected!"))

# Exercise.
text.bind("<Shift-MouseWheel>", lambda event: print("MouseWheel"))



app_icon = tk.PhotoImage(file = "Python Project/Icon_Python.png")
app.iconphoto(True, app_icon)
app.mainloop()
