import tkinter as tk
from tkinter import ttk

products = [
    {"name": "Laptop", "price": 1200, "rating": 4.5},
    {"name": "Smartphone", "price": 800, "rating": 4.7},
    {"name": "Tablet", "price": 400, "rating": 4.2},
    {"name": "Monitor", "price": 300, "rating": 4.3},
]

def bubble_sort(data, key, reverse=False):
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            a = data[j][key]
            b = data[j + 1][key]
            if (a > b and not reverse) or (a < b and reverse):
                data[j], data[j + 1] = data[j + 1], data[j]
    return data

def linear_search(data, keyword):
    result = []
    keyword = keyword.lower()
    for item in data:
        if keyword in item["name"].lower():
            result.append(item)
    return result

def update_tree(data):
    for row in tree.get_children():
        tree.delete(row)
    for product in data:
        tree.insert("", tk.END, values=(product["name"], product["price"], product["rating"]))

def search_products():
    keyword = search_var.get()
    filtered = linear_search(products, keyword)
    update_tree(filtered)

def sort_products(event=None):
    key = sort_var.get()
    reverse = False
    keymap = {
        "Name (A-Z)": ("name", False),
        "Name (Z-A)": ("name", True),
        "Price (Low to High)": ("price", False),
        "Price (High to Low)": ("price", True),
        "Rating": ("rating", True),
    }
    if key in keymap:
        sort_key, reverse = keymap[key]
        copied = products[:]  # manual clone
        sorted_list = bubble_sort(copied, sort_key, reverse)
        update_tree(sorted_list)

# GUI Setup
root = tk.Tk()
root.title("E-Commerce Sort/Search Simulator (No Built-ins!)")

search_var = tk.StringVar()
tk.Entry(root, textvariable=search_var).grid(row=0, column=0, padx=5, pady=5)
tk.Button(root, text="Search", command=search_products).grid(row=0, column=1, padx=5)

sort_var = tk.StringVar()
sort_options = ["Name (A-Z)", "Name (Z-A)", "Price (Low to High)", "Price (High to Low)", "Rating"]
sort_menu = ttk.Combobox(root, textvariable=sort_var, values=sort_options, state="readonly")
sort_menu.grid(row=0, column=2, padx=5)
sort_menu.bind("<<ComboboxSelected>>", sort_products)

columns = ("Name", "Price", "Rating")
tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
tree.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

update_tree(products)
root.mainloop()
