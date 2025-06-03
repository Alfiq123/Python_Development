import customtkinter as ctk

# Set appearance mode and theme
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class InventoryApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("IMS - Inventory Management System")
        self.geometry("600x400")

        # List to hold item data
        self.items = []

        # Frame for input + add button
        self.top_frame = ctk.CTkFrame(self)
        self.top_frame.pack(pady=10, padx=10, fill="x")

        # Entry box to add item
        self.item_entry = ctk.CTkEntry(self.top_frame, placeholder_text="Enter item name...")
        self.item_entry.pack(side="left", expand=True, fill="x", padx=(0, 5))

        # Add button
        self.add_button = ctk.CTkButton(self.top_frame, text="Add Item", command=self.add_item)
        self.add_button.pack(side="left")

        # Scrollable Frame to display items
        self.scroll_frame = ctk.CTkScrollableFrame(self)
        self.scroll_frame.pack(fill="both", expand=True, padx=10, pady=5)

    def add_item(self):
        """Add a new item from entry to the scrollable list."""
        item_name = self.item_entry.get().strip()
        if not item_name:
            return

        # Create item dictionary
        item_data = {
            "name": item_name,
            "label": None,
            "edit_btn": None,
            "delete_btn": None
        }

        # Create widgets inside scrollable frame
        item_frame = ctk.CTkFrame(self.scroll_frame)
        item_frame.pack(fill="x", pady=2)

        label = ctk.CTkLabel(item_frame, text=item_name, width=200, anchor="w")
        label.pack(side="left", padx=5)

        edit_btn = ctk.CTkButton(item_frame, text="Edit", width=60, command=lambda f=item_frame, l=label, d=item_data: self.edit_item(f, l, d))
        edit_btn.pack(side="left", padx=2)

        delete_btn = ctk.CTkButton(item_frame, text="Delete", width=60, fg_color="red", hover_color="dark red",
                                   command=lambda f=item_frame, d=item_data: self.delete_item(f, d))
        delete_btn.pack(side="left", padx=2)

        # Update item_data with widgets
        item_data["frame"] = item_frame
        item_data["label"] = label
        item_data["edit_btn"] = edit_btn
        item_data["delete_btn"] = delete_btn

        self.items.append(item_data)
        self.item_entry.delete(0, "end")

    def edit_item(self, frame, label, item_data):
        """Allow user to edit an item's name."""
        old_name = item_data["name"]

        # Ask for new name using dialog or popup
        dialog = ctk.CTkInputDialog(text="Edit Item Name:", title="Edit")
        new_name = dialog.get_input()

        if new_name and new_name.strip():
            item_data["name"] = new_name.strip()
            label.configure(text=new_name)

    def delete_item(self, frame, item_data):
        """Remove an item from the list and destroy its widgets."""
        self.items.remove(item_data)
        frame.destroy()


if __name__ == "__main__":
    app = InventoryApp()
    app.mainloop()