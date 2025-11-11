import tkinter as tk
from tkinter import ttk

class Application(tk.Tk):
    """Main application window"""
    
    def __init__(self):
        super().__init__()
        
        # Window configuration
        self.title("Tkinter OOP Example")
        self.geometry("400x300")
        
        # Initialize variables
        self.counter = 0
        
        # Create widgets
        self.create_widgets()
    
    def create_widgets(self):
        """Create and layout all widgets"""
        # Label
        self.label = ttk.Label(
            self,
            text="Counter: 0",
            font=("Arial", 16)
        )
        self.label.pack(pady=20)
        
        # Button frame
        button_frame = ttk.Frame(self)
        button_frame.pack(pady=10)
        
        # Buttons
        self.increment_btn = ttk.Button(
            button_frame,
            text="Increment",
            command=self.increment_counter
        )
        self.increment_btn.pack(side=tk.LEFT, padx=5)
        
        self.reset_btn = ttk.Button(
            button_frame,
            text="Reset",
            command=self.reset_counter
        )
        self.reset_btn.pack(side=tk.LEFT, padx=5)
        
        # Entry
        self.entry = ttk.Entry(self, width=30)
        self.entry.pack(pady=10)
        self.entry.insert(0, "Type something...")
        
        # Display button
        self.display_btn = ttk.Button(
            self,
            text="Display Text",
            command=self.display_text
        )
        self.display_btn.pack(pady=5)
        
        # Result label
        self.result_label = ttk.Label(self, text="")
        self.result_label.pack(pady=10)
    
    def increment_counter(self):
        """Increment counter and update label"""
        self.counter += 1
        self.label.config(text=f"Counter: {self.counter}")
    
    def reset_counter(self):
        """Reset counter to zero"""
        self.counter = 0
        self.label.config(text="Counter: 0")
    
    def display_text(self):
        """Display text from entry widget"""
        text = self.entry.get()
        self.result_label.config(text=f"You typed: {text}")


# Run the application
if __name__ == "__main__":
    app = Application()
    app.mainloop()
