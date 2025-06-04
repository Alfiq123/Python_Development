import customtkinter as ctk


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("IMS Alpha")
        self.geometry("500x500")
        self.resizable(width=False, height=False)
        self.grid_rowconfigure(index=2, weight=1)
        self.grid_columnconfigure(index=0, weight=2)

        self.label = ctk.CTkLabel(
            master=self,
            text="Scrollable Frame",
            font=("Helvetica", 24)
        )
        self.label.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        self.button = ctk.CTkButton(
            master=self,
            text="Click",
            font=("Helvetica", 14),
            command=self.button_func
        )
        self.button.grid(row=1, column=0, padx=10, pady=10)

        self.entry = ctk.CTkEntry(
            master=self,
            font=("Helvetica", 14),
            placeholder_text="Something..."
        )
        self.entry.grid(row=1, column=1, padx=10, pady=10)

        self.scroll = ctk.CTkScrollableFrame(master=self)
        self.scroll.grid(
            row=2, column=0, padx=10, pady=10,
            sticky="nsew", columnspan=2
        )

    def button_func(self):
        text = self.entry.get().strip()  # Remove leading/trailing spaces
        if not text:
            # Show a warning message
            warning_label = ctk.CTkLabel(
                master=self,
                text="Please enter some text!",
                text_color="Azure",
                font=("Helvetica", 14)
            )
            warning_label.grid(row=3, column=0, columnspan=2, pady=5)
            self.after(ms=2000, func=warning_label.destroy)
            print(self.after)
            return

        new_frame = ctk.CTkFrame(master=self.scroll, fg_color="Chocolate")
        new_frame.pack(padx=10, pady=10)

        new_label = ctk.CTkLabel(
            master=new_frame,
            text="Outsider",
            font=("Helvetica", 14)
        )
        new_label.grid(row=0, column=0, padx=10, pady=10)

        new_button = ctk.CTkButton(
            master=new_frame,
            text="Delete",
            font=("Helvetica", 14),
            fg_color="Maroon"
        )
        new_button.grid(row=0, column=1, padx=10, pady=10)

        new_label.configure(text=text)  # Use the cleaned input
        new_button.configure(command=new_frame.destroy)


if __name__ == "__main__":
    app = App()
    app.mainloop()
