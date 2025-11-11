import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("250x100")
        self.title("Contoh 0808")

        self.my_frame = ctk.CTkFrame(master=self)
        self.my_frame.pack()

        self.label = ctk.CTkLabel(
            master=self.my_frame,
            text="Focus Events",
            fg_color="black"
        )
        self.label.pack(padx=10, pady=10)

        self.button = ctk.CTkButton(
            master=self.my_frame,
            text="Click Me"
        )
        self.button.pack(padx=10, pady=10)
        self.button.bind(sequence="<Enter>", command=self.on_focus_in)
        self.button.bind(sequence="<Leave>", command=self.on_focus_out)

    def on_focus_in(self, event):
        self.label.configure(
            text="Focus In: Button entered",
            fg_color="green"
        )

    def on_focus_out(self, event):
        self.label.configure(
            text="Focus Out: Button left",
            fg_color="red"
        )


if __name__ == "__main__":
    app = App()
    app.mainloop()
