import tkinter as tk
from tkinter import ttk

class HeaderFrame(ttk.Frame):
    """Custom header frame component"""
    
    def __init__(self, parent, title):
        super().__init__(parent)
        
        self.title_label = ttk.Label(
            self,
            text=title,
            font=("Arial", 18, "bold")
        )
        self.title_label.pack(pady=10)


class InputFrame(ttk.Frame):
    """Custom input frame component"""
    
    def __init__(self, parent, submit_callback):
        super().__init__(parent)
        self.submit_callback = submit_callback
        
        # Name input
        ttk.Label(self, text="Name:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.name_entry = ttk.Entry(self, width=25)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # Email input
        ttk.Label(self, text="Email:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.email_entry = ttk.Entry(self, width=25)
        self.email_entry.grid(row=1, column=1, padx=5, pady=5)
        
        # Submit button
        self.submit_btn = ttk.Button(
            self,
            text="Submit",
            command=self.on_submit
        )
        self.submit_btn.grid(row=2, column=0, columnspan=2, pady=10)
    
    def on_submit(self):
        """Handle submit button click"""
        name = self.name_entry.get()
        email = self.email_entry.get()
        self.submit_callback(name, email)
    
    def clear(self):
        """Clear all input fields"""
        self.name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)


class DisplayFrame(ttk.Frame):
    """Custom display frame component"""
    
    def __init__(self, parent):
        super().__init__(parent)
        
        # Listbox with scrollbar
        scrollbar = ttk.Scrollbar(self)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.listbox = tk.Listbox(
            self,
            width=40,
            height=8,
            yscrollcommand=scrollbar.set
        )
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.listbox.yview)
    
    def add_entry(self, text):
        """Add an entry to the listbox"""
        self.listbox.insert(tk.END, text)
    
    def clear(self):
        """Clear all entries"""
        self.listbox.delete(0, tk.END)


class Application(tk.Tk):
    """Main application window"""
    
    def __init__(self):
        super().__init__()
        
        # Window configuration
        self.title("Advanced Tkinter OOP")
        self.geometry("500x450")
        self.resizable(False, False)
        
        # Create UI
        self.create_widgets()
    
    def create_widgets(self):
        """Create and layout all widgets"""
        # Header
        self.header = HeaderFrame(self, "User Registration")
        self.header.pack(fill=tk.X, padx=10, pady=5)
        
        # Separator
        ttk.Separator(self, orient=tk.HORIZONTAL).pack(fill=tk.X, padx=10, pady=5)
        
        # Input frame
        self.input_frame = InputFrame(self, self.handle_submit)
        self.input_frame.pack(padx=10, pady=10)
        
        # Separator
        ttk.Separator(self, orient=tk.HORIZONTAL).pack(fill=tk.X, padx=10, pady=5)
        
        # Display frame
        display_label = ttk.Label(self, text="Registered Users:", font=("Arial", 12))
        display_label.pack(padx=10, pady=(10, 5))
        
        self.display_frame = DisplayFrame(self)
        self.display_frame.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
        
        # Clear button
        self.clear_btn = ttk.Button(
            self,
            text="Clear All",
            command=self.clear_all
        )
        self.clear_btn.pack(pady=10)
    
    def handle_submit(self, name, email):
        """Handle form submission"""
        if name and email:
            entry_text = f"{name} - {email}"
            self.display_frame.add_entry(entry_text)
            self.input_frame.clear()
        else:
            # You could show a messagebox here
            print("Please fill in all fields")
    
    def clear_all(self):
        """Clear all data"""
        self.display_frame.clear()
        self.input_frame.clear()


# Run the application
if __name__ == "__main__":
    app = Application()
    app.mainloop()
