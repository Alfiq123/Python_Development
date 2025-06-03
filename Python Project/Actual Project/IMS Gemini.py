import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox

class ScrollableButtonApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Scrollable Frame with Dynamic Buttons")
        self.geometry("600x500")

        # --- Data Storage ---
        # This list will hold the names of our items/buttons
        self.items = ["Item A", "Item B", "Item C", "Item D", "Item E",
                      "Item F", "Item G", "Item H", "Item I", "Item J"]

        # --- UI Setup ---

        # 1. Control Frame (for adding items)
        self.control_frame = ctk.CTkFrame(self)
        self.control_frame.pack(pady=10, padx=10, fill="x")

        self.add_entry = ctk.CTkEntry(self.control_frame, placeholder_text="New item name")
        self.add_entry.pack(side="left", expand=True, fill="x", padx=(0, 10))

        self.add_button = ctk.CTkButton(self.control_frame, text="Add Item", command=self.add_new_item)
        self.add_button.pack(side="left")

        # 2. Scrollable Frame
        self.scrollable_frame = ctk.CTkScrollableFrame(self, label_text="Your Items")
        self.scrollable_frame.pack(pady=10, padx=10, expand=True, fill="both")

        # Configure the grid within the scrollable frame to allow buttons to expand
        self.scrollable_frame.grid_columnconfigure(0, weight=1)

        # Initial population of buttons
        self.refresh_item_buttons()

    def refresh_item_buttons(self):
        """
        Clears all existing buttons in the scrollable frame
        and re-creates them based on the current self.items list.
        """
        # Destroy all existing widgets in the scrollable frame
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        # Create new buttons for each item in the list
        if not self.items:
            no_items_label = ctk.CTkLabel(self.scrollable_frame, text="No items yet. Add some above!", text_color="gray")
            no_items_label.pack(pady=20)
            return

        for idx, item_name in enumerate(self.items):
            # Create a frame for each item row to hold the item button and delete button
            item_row_frame = ctk.CTkFrame(self.scrollable_frame, fg_color="transparent")
            # Use grid for the scrollable frame content to allow consistent rows
            item_row_frame.grid(row=idx, column=0, pady=5, padx=5, sticky="ew")
            item_row_frame.grid_columnconfigure(0, weight=1) # Item button expands

            # Item Button (main button for the item)
            # The command uses lambda to pass the specific item_name to item_command
            item_button = ctk.CTkButton(
                item_row_frame,
                text=item_name,
                command=lambda name=item_name: self.item_command(name)
            )
            item_button.grid(row=0, column=0, sticky="ew", padx=(0, 10))

            # Delete Button
            # The command uses lambda to pass the specific item_name to delete_item
            delete_button = ctk.CTkButton(
                item_row_frame,
                text="X", # Or a trash icon
                width=30, # Make it smaller
                fg_color="red",
                hover_color="#b30000",
                command=lambda name=item_name: self.delete_item(name)
            )
            delete_button.grid(row=0, column=1, sticky="e")

    def item_command(self, item_name):
        """
        This function is called when one of the main item buttons is clicked.
        It has access to the specific item_name that was clicked.
        """
        messagebox.showinfo("Item Clicked", f"You clicked: {item_name}")
        print(f"Command for item: {item_name}")

    def add_new_item(self):
        """
        Adds a new item to the list and refreshes the display.
        """
        new_item = self.add_entry.get().strip()
        if new_item:
            if new_item in self.items:
                messagebox.showwarning("Duplicate Item", f"'{new_item}' already exists.")
            else:
                self.items.append(new_item)
                self.add_entry.delete(0, ctk.END) # Clear the entry field
                self.refresh_item_buttons() # Refresh all buttons
        else:
            messagebox.showwarning("Input Error", "Please enter an item name.")

    def delete_item(self, item_name):
        """
        Deletes an item from the list and refreshes the display.
        """
        if messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete '{item_name}'?"):
            if item_name in self.items:
                self.items.remove(item_name)
                self.refresh_item_buttons() # Refresh all buttons
            else:
                messagebox.showerror("Error", f"Could not find '{item_name}' to delete.")

if __name__ == "__main__":
    ctk.set_appearance_mode("System")  # Modes: "System" (default), "Dark", "Light"
    ctk.set_default_color_theme("blue") # Themes: "blue" (default), "dark-blue", "green"

    app = ScrollableButtonApp()
    app.mainloop()