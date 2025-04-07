import tkinter as tk
import ttkbootstrap as ttk

app = ttk.Window(themename = "flatly")
app.title("Buttons Arguments")
app.resizable(width = False, height = False)


def button_func(entry_string):
    print(f"Button Pressed!")
    print(entry_string.get())

# def outer_func(parameters):
    # def inner_func():
        # print(f"Button Pressed!")
        # print(parameters.get())
    # return inner_func

label = ttk.Label(master = app, text = "Arguments", font = ("Times New Roman", 14, "bold"))
label.pack(padx = 10, pady = 10)

entry_string = tk.StringVar(value = "Stringer")
entry = ttk.Entry(master = app, textvariable = entry_string)
entry.pack(padx = 10, pady = 10)

button = ttk.Button(master = app, text = "Return", command = button_func(entry_string))
button.pack(padx = 10, pady = 10)


# Window Icon
app_icon = tk.PhotoImage(file="Python_Intermediate/Python Project/Assets/Icon_Python.png")
app.iconphoto(True, app_icon)

# Run
app.mainloop()