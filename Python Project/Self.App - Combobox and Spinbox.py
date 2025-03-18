import tkinter as tk
import ttkbootstrap as ttk

app = ttk.Window(themename = "solar")
app.title("Combo and Spin")
app.resizable(width = False, height = False)


    # Combobox.
combo_items = ("Ice Cream", "Hotdog", "Pizza", "Bread", "Hamburger", "Salad")
combo_food = tk.StringVar(value = [combo_items[2]])

combo = ttk.Combobox(master = app, textvariable = combo_food)
combo["value"] = combo_items
# combo.configure(values = combo_items)
combo.pack(padx = 10, pady = 10)

# Special Events.
# combo.bind("<<ComboboxSelected>>", lambda event: print(combo_food.get()))
combo.bind("<<ComboboxSelected>>", lambda event: combo_label.config(text = f"Selected Value: {combo_food.get()}"))

# Label.
combo_label = ttk.Label(master = app, text = "The Label", textvariable = combo_food)
combo_label.pack(padx = 10, pady = 10)


    # Spinbox.
spin_int = tk.IntVar(value = 12)
spin = ttk.Spinbox(master = app, from_ = 3, to = 21, increment = 3, command = lambda: print("Button was pressed!"), textvariable = spin_int)
spin.bind("<<Increment>>", lambda event: print("Up"))
spin.bind("<<Decrement>>", lambda event: print("Down"))
# spin["value"] = (1, 2, 3, 4, 5)
spin.pack(padx = 10, pady = 10)


    # Exercise.
exc_letter = ("A", "B", "C", "D", "E")

exc_string = tk.StringVar(value = exc_letter[0])
exc_spin = ttk.Spinbox(master = app, textvariable = exc_string, values = exc_letter)
# exc_spin["value"] = exc_letter
exc_spin.pack(padx = 10, pady = 10)
exc_spin.bind("<<Decrement>>", lambda event: print(exc_string.get()))


app_icon = tk.PhotoImage(file = "Python Project/Icon_Python.png")
app.iconphoto(True, app_icon)
app.mainloop()
