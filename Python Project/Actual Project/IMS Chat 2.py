import customtkinter as ctk

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class InventoryApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Inventory Management")
        self.geometry("600x600")

        self.items = []
        self.counter = 1

        # Header
        header = ctk.CTkLabel(self, text="📦 Inventory Management",
                              font=ctk.CTkFont(size=20, weight="bold"))
        header.pack(pady=(10, 0))

        # Controls: Sort and Search
        controls_frame = ctk.CTkFrame(self)
        controls_frame.pack(pady=10, padx=10, fill="x")

        self.sort_combobox = ctk.CTkComboBox(controls_frame,
                                             values=["Name", "Quantity",
                                                     "Status"])
        self.sort_combobox.set("Sort By")
        self.sort_combobox.pack(side="left", padx=5)

        self.search_entry = ctk.CTkEntry(controls_frame,
                                         placeholder_text="Search...")
        self.search_entry.pack(side="left", padx=5, fill="x", expand=True)

        # Scrollable Table
        self.table_frame = ctk.CTkScrollableFrame(self, height=400)
        self.table_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Table Header
        self.add_table_header()

        # Dummy data
        for _ in range(5):
            self.add_row(f"Item {self.counter}", f"Desc {self.counter}",
                         self.counter * 2, "In Stock")
            self.counter += 1

    def add_table_header(self):
        header_frame = ctk.CTkFrame(self.table_frame)
        header_frame.pack(fill="x")

        headers = ["Item", "Deskripsi", "Kuantitas", "Status", "Action"]
        for text in headers:
            label = ctk.CTkLabel(header_frame, text=text, anchor="w",
                                 width=100)
            label.pack(side="left", padx=5)

    def add_row(self, item, deskripsi, qty, status):
        row_frame = ctk.CTkFrame(self.table_frame)
        row_frame.pack(fill="x", pady=2)

        # Item columns
        ctk.CTkLabel(row_frame, text=item, width=100).pack(side="left", padx=5)
        ctk.CTkLabel(row_frame, text=deskripsi, width=100).pack(side="left",
                                                                padx=5)
        ctk.CTkLabel(row_frame, text=str(qty), width=100).pack(side="left",
                                                               padx=5)
        ctk.CTkLabel(row_frame, text=status, width=100).pack(side="left",
                                                             padx=5)

        # Delete Button
        delete_btn = ctk.CTkButton(row_frame, text="❌", width=40,
                                   fg_color="red",
                                   command=lambda: self.delete_row(row_frame))
        delete_btn.pack(side="left", padx=5)

        # Optionally track it
        self.items.append({
            "frame": row_frame,
            "item": item,
            "desc": deskripsi,
            "qty": qty,
            "status": status
        })

    def delete_row(self, frame):
        frame.destroy()
        self.items = [i for i in self.items if i["frame"] != frame]


if __name__ == "__main__":
    app = InventoryApp()
    app.mainloop()
