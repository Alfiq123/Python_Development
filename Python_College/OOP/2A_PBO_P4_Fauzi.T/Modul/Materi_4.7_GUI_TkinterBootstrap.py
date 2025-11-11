import ttkbootstrap as ttk


class App(ttk.Window):
    def __init__(self):
        super().__init__(themename="cosmo")

        self.title('Contoh 0807')
        self.geometry("300x100")

        self.my_frame = ttk.Frame(self)
        self.my_frame.pack()

        self.label_1 = ttk.Label(master=self.my_frame, text="Keyboard Events (Key Pressed)")
        self.label_2 = ttk.Label(master=self.my_frame, text="Keyboard Events (Key Released)")

        self.label_1.pack(pady=10)
        self.label_2.pack(pady=10)

        self.bind("<KeyPress>", self.on_key_press)
        self.bind("<KeyRelease>", self.on_key_release)

    def on_key_press(self, event):
        self.label_1.configure(text=f"Key Pressed: {event.keysym}")

    def on_key_release(self, event):
        self.label_2.configure(text=f"Key Released: {event.keysym}")


if __name__ == "__main__":
    app = App()
    app.mainloop()
