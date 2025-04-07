import customtkinter as ctk
import time

class StopwatchApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("CTk Stopwatch")
        self.geometry("350x250")
        # self.resizable(False, False) # Optional: Prevent resizing

        # --- Stopwatch State Variables ---
        self.running = False
        self.start_time = 0.0
        self.elapsed_time = 0.0 # Time accumulated before the current run
        self._timer_id = None  # To store the 'after' job ID

        # --- GUI Elements ---
        # Time Display Label
        self.time_label = ctk.CTkLabel(self, text="00:00:00.000", font=("Segoe UI", 40))
        self.time_label.pack(pady=20, padx=20, fill="x")

        # Button Frame
        button_frame = ctk.CTkFrame(self, fg_color="transparent")
        button_frame.pack(pady=10)

        # Start Button
        self.start_button = ctk.CTkButton(button_frame, text="Start", width=80, command=self.start)
        self.start_button.pack(side="left", padx=10)

        # Stop Button
        self.stop_button = ctk.CTkButton(button_frame, text="Stop", width=80, command=self.stop, state="disabled")
        self.stop_button.pack(side="left", padx=10)

        # Reset Button
        self.reset_button = ctk.CTkButton(button_frame, text="Reset", width=80, command=self.reset)
        self.reset_button.pack(side="left", padx=10)

    def _format_time(self, seconds_float):
        """Formats elapsed time into HH:MM:SS.ms"""
        total_seconds = int(seconds_float)
        milliseconds = int((seconds_float - total_seconds) * 1000)
        minutes, seconds = divmod(total_seconds, 60)
        hours, minutes = divmod(minutes, 60)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}.{milliseconds:03d}"

    def _update_time(self):
        """Updates the time label periodically."""
        if self.running:
            current_elapsed = self.elapsed_time + (time.time() - self.start_time)
            formatted_time = self._format_time(current_elapsed)
            self.time_label.configure(text=formatted_time)
            # Schedule the next update (e.g., every 50 milliseconds)
            self._timer_id = self.after(50, self._update_time)
        else:
             self._timer_id = None # Ensure timer_id is cleared if not running

    def start(self):
        """Starts or resumes the stopwatch."""
        if not self.running:
            self.running = True
            self.start_time = time.time() # Record the exact start/resume time
            self.start_button.configure(state="disabled")
            self.stop_button.configure(state="normal")
            self.reset_button.configure(state="normal") # Allow reset while running
            self._update_time() # Start the update loop

    def stop(self):
        """Stops or pauses the stopwatch."""
        if self.running:
            self.running = False
            # Add the duration of the *last run* to the total elapsed time
            self.elapsed_time += (time.time() - self.start_time)
            self.start_button.configure(state="normal")
            self.stop_button.configure(state="disabled")
            # Cancel the scheduled update if it exists
            if self._timer_id:
                self.after_cancel(self._timer_id)
                self._timer_id = None

    def reset(self):
        """Resets the stopwatch to zero."""
        was_running = self.running # Check if it was running before reset
        self.running = False
        self.elapsed_time = 0.0
        self.start_time = 0.0 # Not strictly necessary but good practice

        # Cancel any pending update
        if self._timer_id:
             self.after_cancel(self._timer_id)
             self._timer_id = None

        # Update label immediately
        self.time_label.configure(text="00:00:00.000")

        # Reset button states
        self.start_button.configure(state="normal")
        self.stop_button.configure(state="disabled")
        # Optionally disable reset button if already at 0 (and not running)
        # self.reset_button.configure(state="disabled" if not was_running and self.elapsed_time == 0 else "normal")


if __name__ == "__main__":
    # Set appearance mode (optional)
    ctk.set_appearance_mode("System")  # Modes: "System" (default), "Dark", "Light"
    ctk.set_default_color_theme("blue") # Themes: "blue" (default), "green", "dark-blue"

    app = StopwatchApp()
    app.mainloop()