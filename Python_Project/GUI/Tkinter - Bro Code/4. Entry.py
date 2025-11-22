import tkinter as tk
from tkinter.constants import DISABLED

import customtkinter as ctk

from os import path
from PIL import Image

app = ctk.CTk()
app.title("The Entry")
app.resizable(width=False, height=False)


# ══════════════ Begin Icon ══════════════ #


icon_send = ctk.CTkImage(
    dark_image=Image.open(
        path.join(path.dirname(__file__), "Assets", "icon_send.png")
    ), size=(16, 16)
)

icon_delete = ctk.CTkImage(
    dark_image=Image.open(
        path.join(path.dirname(__file__), "Assets", "icon_bin.png")
    ), size=(16, 16)
)

icon_backspace = ctk.CTkImage(
    dark_image=Image.open(
        path.join(path.dirname(__file__), "Assets", "icon_backspace.png")
    ), size=(16, 16)
)


# ══════════════ End Icon ══════════════ #


def send_and_end():
    print(f"Send {entry.get()}")
    entry.configure(state=DISABLED)
    entry_submit.configure(state=DISABLED)


# Entry
entry = ctk.CTkEntry(
    master=app,
    font=("Arial", 14, "normal"),
    # show="*"  # ← Password like text.
)
entry.insert(index=0, string="Enter the text...")  # ← Insert text to entry.
entry.grid(padx=10, pady=10, row=0, column=0, columnspan=3)

# Submit.
entry_submit = ctk.CTkButton(
    master=app,
    text="",
    font=("Arial", 14, "normal"),
    command=send_and_end,
    image=icon_send,
    width=32,
    corner_radius=32,
    fg_color="#F8F8F5"
)
entry_submit.grid(padx=10, pady=10, row=1, column=0)

# Delete.
entry_delete = ctk.CTkButton(
    master=app,
    text="",
    font=("Arial", 14, "normal"),
    command=lambda: entry.delete(
        first_index=0, last_index=tk.END  # ← Delete `entry` completely.
    ),
    image=icon_delete,
    width=32,
    corner_radius=32,
    fg_color="#F8F8F5"
)
entry_delete.grid(padx=10, pady=10, row=1, column=1)

# Backspace.
entry_backspace = ctk.CTkButton(
    master=app,
    text="",
    font=("Arial", 14, "normal"),
    command=lambda: entry.delete(
        first_index=len(entry.get()) - 1, last_index=tk.END  # ← Backspace.
    ),
    image=icon_backspace,
    width=32,
    corner_radius=32,
    fg_color="#F8F8F5"
)
entry_backspace.grid(padx=10, pady=10, row=1, column=2)

app_icon = tk.PhotoImage(
    file=path.join(path.dirname(__file__), "Assets", "icon_python.png")
)
app.iconphoto(True, app_icon)

app.mainloop()
