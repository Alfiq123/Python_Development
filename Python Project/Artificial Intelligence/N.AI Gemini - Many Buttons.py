import tkinter as tk
from tkinter import ttk # Use themed widgets for a more modern look

# --- Class for the Pop-up Windows ---
# It's good practice to make this a separate class if the windows
# will have more complex content or functionality.
class PopupWindow(tk.Toplevel):
    """A simple Toplevel window associated with a specific button."""
    _open_windows = {} # Class variable to track open windows by ID

    def __init__(self, parent, window_id, title="Popup Window"):
        """
        Initializes the Toplevel window.

        Args:
            parent: The parent widget (usually the main app window).
            window_id: A unique identifier for this window type (e.g., button name).
            title: The base title for the window.
        """
        # Check if a window for this ID is already open
        if window_id in PopupWindow._open_windows and PopupWindow._open_windows[window_id].winfo_exists():
            print(f"Window for '{window_id}' is already open. Bringing it to front.")
            PopupWindow._open_windows[window_id].lift() # Bring the existing window to the front
            PopupWindow._open_windows[window_id].focus_set()
            # Optionally destroy self if we don't want a new instance attempt
            # super().__init__(parent) # Need to init before destroying cleanly
            # self.destroy()
            return # Stop initialization

        # If not open or the old one was closed, proceed
        super().__init__(parent) # Initialize the Toplevel window
        self.window_id = window_id
        self.title(f"{title} - {window_id}")
        self.geometry("300x200+150+150") # Width x Height + X offset + Y offset

        # Keep track of this new window
        PopupWindow._open_windows[window_id] = self

        # --- Add content specific to this window ---
        label = ttk.Label(self, text=f"This is the window for '{window_id}'.")
        label.pack(pady=20, padx=20)

        info_label = ttk.Label(self, text="Add specific widgets and logic here.")
        info_label.pack(pady=5, padx=20)

        close_button = ttk.Button(self, text="Close", command=self.destroy_window)
        close_button.pack(pady=10)

        # Ensure the window is removed from tracking when closed via the 'X' button
        self.protocol("WM_DELETE_WINDOW", self.destroy_window)

        # Focus this new window
        self.focus_set()
        self.lift() # Bring to front

    def destroy_window(self):
        """Destroys the window and removes it from tracking."""
        print(f"Closing window for '{self.window_id}'")
        if self.window_id in PopupWindow._open_windows:
            del PopupWindow._open_windows[self.window_id] # Remove from tracking
        self.destroy() # Destroy the tkinter window


# --- Main Application Class ---
class App:
    """The main application window holding the buttons."""
    def __init__(self, root):
        """
        Initializes the main application.

        Args:
            root: The main tkinter root window (tk.Tk()).
        """
        self.root = root
        self.root.title("Main Application with Many Buttons")
        self.root.geometry("300x400+100+100")

        # --- Frame for Buttons ---
        button_frame = ttk.Frame(self.root, padding="10")
        button_frame.pack(fill=tk.BOTH, expand=True)

        # --- Data for Buttons ---
        # In a real app, this might come from a file, database, etc.
        button_configs = [
            {"id": "Action 1", "text": "Open Window 1"},
            {"id": "Data Entry", "text": "Open Data Form"},
            {"id": "Settings", "text": "Configure Settings"},
            {"id": "Help Topic A", "text": "Show Help A"},
            {"id": "Process X", "text": "Start Process X"},
            # Add as many buttons as you need
        ]

        # --- Create Buttons Dynamically ---
        for config in button_configs:
            button_id = config["id"]
            button_text = config["text"]

            # *** Crucial Part: Using lambda ***
            # Create a function (lambda) that captures the current 'button_id'.
            # If you just used `self.open_window(button_id)`, it would try to
            # use the *last* value of button_id from the loop for all buttons.
            # `lambda id=button_id:` creates a default argument for the lambda,
            # effectively "freezing" the value of button_id for that specific button.
            cmd = lambda id=button_id: self.open_window(id)

            button = ttk.Button(button_frame, text=button_text, command=cmd)
            button.pack(pady=5, fill=tk.X) # Place button vertically, fill horizontally


    def open_window(self, button_id):
        """
        Callback function executed when a button is clicked.
        Creates and shows a new PopupWindow.
        """
        print(f"Button '{button_id}' clicked. Attempting to open window.")
        # Create an instance of our custom Toplevel window class
        # Pass the main window (self.root) as the parent and the identifier
        PopupWindow(self.root, window_id=button_id, title="Details")
        # The PopupWindow class now handles whether to create a new window
        # or bring an existing one to the front.


# --- Main Execution ---
if __name__ == "__main__":
    main_root = tk.Tk()
    app = App(main_root) # Create an instance of our main application class
    main_root.mainloop() # Start the tkinter event loop