import ttkbootstrap as ttk

class App(ttk.Window):
    def __init__(self):
        super().__init__(themename="cosmo")

        self.geometry("250x100")
        self.title("Contoh 0808")

        self.my_frame = ttk.Frame(master=self)
        self.my_frame.pack()

        self.label = ttk.Label(
            master=self.my_frame,
            text="Focus Events",
            foreground="black"
        )
        self.label.pack(pady=10)

        self.button = ttk.Button(
            master=self.my_frame,
            text="Click Me"
        )
        self.button.pack(pady=10)
        self.button.bind("<Enter>", self.on_focus_in)
        self.button.bind("<Leave>", self.on_focus_out)

    def on_focus_in(self, event):
        self.label.configure(
            text="Focus In: Button entered",
            foreground="green"
        )

    def on_focus_out(self, event):
        self.label.configure(
            text="Focus Out: Button left",
            foreground="red"
        )


if __name__ == "__main__":
    app = App()
    app.mainloop()
