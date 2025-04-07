import tkinter as tk
import ttkbootstrap as ttk
import customtkinter as ctk

root = ctk.CTk()
root.geometry("256x256")
root.title("Figma")
root.resizable(width = False, height = False)

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# Frame
frame = ctk.CTkFrame(master = root, border_color = "black", border_width = 1)
frame.pack(pady = 20, padx = 20, fill = "both", expand = True)

# Label
label = ctk.CTkLabel(master = frame, text = "Figma Design")
label.pack(pady = 10, padx = 10)

# Button
button = ctk.CTkButton(
    master = frame, 
    text = "Process", 
    fg_color = "#9ACBD0", 
    border_color= "#D4C9BE", 
    border_width = 1, 
    hover_color = "#F2EFE7", 
    text_color = "#006A71", 
    corner_radius = 10
)
button.pack(pady = 10, padx = 10)

# Entry
entry = ctk.CTkEntry(
    master = frame, 
    text_color = "#006A71", 
    border_color= "#D4C9BE", 
    border_width = 1, 
    fg_color = "#9ACBD0", 
    placeholder_text = "Username", 
    placeholder_text_color = "#006A71", 
    corner_radius = 10
)
entry.pack(pady = 10, padx = 10)

root.mainloop()
