import customtkinter as ctk

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("IMS Scrollable Frame Example")
        self.geometry("400x500")

        # Inventory data (list of items)
        self.inventory = []
        self.item_counter = 1

        # Add button
        self.add_button = ctk.CTkButton(self, text="Add Item", command=self.add_item)
        self.add_button.pack(pady=10)

        # Scrollable Frame
        self.scrollable_frame = ctk.CTkScrollableFrame(self, width=350, height=400)
        self.scrollable_frame.pack(pady=10, padx=10, fill="both", expand=True)

    def add_item(self):
        # Fake item name with ID
        item_name = f"Item {self.item_counter}"
        self.item_counter += 1

        # Frame for each item row
        item_frame = ctk.CTkFrame(self.scrollable_frame)
        item_frame.pack(fill="x", pady=5)

        # Label
        label = ctk.CTkLabel(item_frame, text=item_name)
        label.pack(side="left", padx=(10, 5))

        # Delete button with custom command using lambda
        delete_button = ctk.CTkButton(
            item_frame,
            text="Delete",
            width=80,
            fg_color="red",
            command=lambda f=item_frame: self.delete_item(f)
        )
        delete_button.pack(side="right", padx=10)

        # Store reference (optional, if you need to track data)
        self.inventory.append({"name": item_name, "frame": item_frame})

    def delete_item(self, frame):
        # Destroy the widget
        frame.destroy()

        # Optionally, remove from inventory list
        self.inventory = [item for item in self.inventory if item["frame"] != frame]

if __name__ == "__main__":
    app = App()
    app.mainloop()
