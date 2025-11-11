import customtkinter as ctk


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Contoh 0806")
        self.attributes("-zoomed", True)
        ## self.state("zoomed")

        self.my_frame = ctk.CTkFrame(self)
        self.my_frame.pack(padx=10, pady=10)

        self.label_1 = ctk.CTkLabel(master=self.my_frame, text="Klik Kiri")
        self.label_2 = ctk.CTkLabel(master=self.my_frame, text="Klik Kanan")
        self.label_3 = ctk.CTkLabel(master=self.my_frame, text="Klik Tengah")
        self.label_4 = ctk.CTkLabel(master=self.my_frame, text="Pergerakan Mouse")

        self.label_1.pack(pady=10)
        self.label_2.pack(pady=10)
        self.label_3.pack(pady=10)
        self.label_4.pack(pady=10)

        self.bind("<Button-1>", self.on_left_click)
        self.bind("<Button-3>", self.on_right_click)
        self.bind("<Button-2>", self.on_middle_click)
        self.bind("<Motion>", self.on_mouse_motion)

    def on_left_click(self, event):
        ## self.label_1.configure(text="Klik Kiri di ({}, {})".format(event.x, event.y))
        self.label_1.configure(text=f"Klik Kiri di ({event.x}, {event.y})")

    def on_right_click(self, event):
        ## self.label_2.configure(text="Klik Kanan di ({}, {})".format(event.x, event.y))
        self.label_2.configure(text=f"Klik Kanan di ({event.x}, {event.y})")

    def on_middle_click(self, event):
        ## self.label_3.configure(text="Klik Tengah di ({}, {})".format(event.x, event.y))
        self.label_3.configure(text=f"Klik Tengah di ({event.x}, {event.y})")

    def on_mouse_motion(self, event):
        ## self.label_4.configure(text="Mouse Bergerak di ({}, {})".format(event.x, event.y))
        self.label_4.configure(text=f"Mouse Bergerak di ({event.x}, {event.y})")


if __name__ == "__main__":
    app = App()
    app.mainloop()
