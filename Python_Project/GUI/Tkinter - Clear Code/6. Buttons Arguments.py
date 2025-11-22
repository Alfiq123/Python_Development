import tkinter as tk
import ttkbootstrap as ttk

from os import path

app = ttk.Window(themename="flatly")
app.title("Buttons Arguments")
app.resizable(width=False, height=False)


def button_func(get_entry_string):
    print("Button Pressed!")
    print(get_entry_string.get())


# def outer_func(parameters):
# def inner_func():
# print(f"Button Pressed!")
# print(parameters.get())
# return inner_func

label = ttk.Label(
    master=app,
    text="Arguments",
    font=("Times New Roman", 14, "bold")
)
label.pack(padx=10, pady=10)

entry_string = tk.StringVar(value="Stringer")
entry = ttk.Entry(master=app, textvariable=entry_string)
entry.pack(padx=10, pady=10)

button = ttk.Button(
    master=app,
    text="Return",
    command=lambda: button_func(entry_string)
)
button.pack(padx=10, pady=10)

# Window Icon
app_icon_path = path.join(path.dirname(__file__),"Assets", "Icon_Python.png")
app_icon = tk.PhotoImage(file=app_icon_path)
app.iconphoto(True, app_icon)

# Run
app.mainloop()
