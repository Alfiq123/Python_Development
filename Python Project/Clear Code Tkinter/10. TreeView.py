import tkinter as tk
from tkinter import ttk
from random import choice

# Window.
app = tk.Tk()
app.title("TreeView")
app.resizable(False, False)


# Data.
first_name = ["Bob", "Maria", "Alex", "James", "Susan", "Henry", "Lisa", "Anna"]
last_name = ["Smith", "Brown", "Wilson", "Thomson", "Jones", "Taylor", "Walker", "Clark"]

# TreeView.
table = ttk.Treeview(master = app, columns = ("first", "last", "email"), show = "headings")
table.heading("first", text = "First Name")
table.heading("last", text = "Last Name")
table.heading("email", text = "Email")
table.pack(padx = 10, pady = 10)

# Insert Valuo on the Table.
# table.insert(parent = "", index = 0, values = ())

for i in range(35):
    """ Insert Valuo on the Table. """
    first = choice(first_name)
    last = choice(last_name)
    email = f"{first.lower()}{last.lower()}@gmail.com"
    table.insert(parent = "", index = "end", values = (first, last, email))

# Events.
def item_selected(event):
    """ Select Items. """
    for i in table.selection():
        print(table.item(i)["values"])

def delete_item(event):
    """ Delete Items. """
    for i in table.selection():
        table.delete(i)

# table.bind("<<TreeviewSelect>>", lambda event: print(table.selection()))
# table.bind("<<TreeviewSelect>>", lambda event: print(table.item(table.selection())["values"]))

table.bind("<<TreeviewSelect>>", item_selected)
table.bind("<Delete>", delete_item)


# Window Icon
app_icon = tk.PhotoImage(file="Python_Intermediate/Python Project/Assets/Icon_Python.png")
app.iconphoto(True, app_icon)

# Run
app.mainloop()
