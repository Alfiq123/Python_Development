import tkinter as tk
from tkinter import ttk

root = tk.Tk()

tree = ttk.Treeview(root)
tree.pack()

# Define columns (optional)
tree["columns"] = ("size", "modified")
tree.column("#0", width=200)  # Tree column
tree.column("size", width=100)
tree.column("modified", width=150)

tree.heading("#0", text="Name")
tree.heading("size", text="Size")
tree.heading("modified", text="Modified")

# Insert items
parent = tree.insert("", "end", text="My Documents", open=True)
tree.insert(parent, "end", text="Report.docx", values=("10KB", "2023-10-27"))
tree.insert(parent, "end", text="Image.jpg", values=("500KB", "2023-10-26"))

root.mainloop()
