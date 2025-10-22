import tkinter as tk

# Parent window class
class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()  # Initialize the Tk window
        self.title("OOP with Tkinter")
        self.geometry("300x200")

        # Instantiate a frame (child) inside this window
        MainFrame(self).pack(fill="both", expand=True)

# A frame that inherits from tk.Frame
class MainFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)  # parent is an instance of MyApp
        self.label = tk.Label(self, text="Hello from Frame")
        self.label.pack(pady=10)

        self.button = tk.Button(self, text="Click Me", command=self.say_hello)
        self.button.pack()

    def say_hello(self):
        self.label.config(text="You clicked the button!")

# Run the app
if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
