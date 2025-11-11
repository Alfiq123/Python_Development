import customtkinter as ctk


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("300x230")
        self.title("Contoh 0804")

        ## self.my_frame = tk.Frame(master=self)
        ## self.my_frame.pack(padx=10, pady=10)

        self.my_label_1 = ctk.CTkLabel(master=self, text="Widget 1", bg_color="cyan")
        self.my_label_2 = ctk.CTkLabel(master=self, text="Widget 2", bg_color="magenta")
        self.my_label_3 = ctk.CTkLabel(master=self, text="Widget 3", bg_color="yellow")

        self.my_label_1.place(x=50, y=20)
        self.my_label_2.place(relx=0.5, rely=0.5, anchor="center")
        self.my_label_3.place(x=150, y=150)


if __name__ == "__main__":
    app = App()
    app.mainloop()
