import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledFrame
import json
import os
from datetime import datetime

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cool To-Do List")
        self.root.geometry("700x600")
        self.root.resizable(True, True)
        
        # Setup variables
        self.tasks = []
        self.filter_var = tk.StringVar(value="All")
        self.search_var = tk.StringVar()
        self.search_var.trace("w", self.filter_tasks)
        
        # Data file
        self.data_file = "todo_data.json"
        self.load_tasks()
        
        # Create widgets
        self.create_widgets()
        
        # Set theme colors for custom styling
        self.accent_color = ttk.Style().colors.primary
        self.warning_color = ttk.Style().colors.warning
        self.success_color = ttk.Style().colors.success
        
    def create_widgets(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding=15)
        main_frame.pack(fill=BOTH, expand=YES)
        
        # Header
        header_frame = ttk.Frame(main_frame)
        header_frame.pack(fill=X, pady=(0, 15))
        
        app_title = ttk.Label(header_frame, text="COOL TO-DO LIST", font=("TkDefaultFont", 18, "bold"))
        app_title.pack(side=LEFT)
        
        date_label = ttk.Label(header_frame, text=datetime.now().strftime("%B %d, %Y"), font=("TkDefaultFont", 12))
        date_label.pack(side=RIGHT)
        
        # Input area
        input_frame = ttk.Frame(main_frame)
        input_frame.pack(fill=X, pady=10)
        
        self.task_entry = ttk.Entry(input_frame, width=40, font=("TkDefaultFont", 12))
        self.task_entry.pack(side=LEFT, fill=X, expand=YES, padx=(0, 5))
        self.task_entry.bind("<Return>", lambda e: self.add_task())
        
        self.priority_combo = ttk.Combobox(input_frame, values=["Low", "Medium", "High"], width=10)
        self.priority_combo.current(1)  # Default to Medium
        self.priority_combo.pack(side=LEFT, padx=5)
        
        add_btn = ttk.Button(input_frame, text="Add Task", command=self.add_task, style="accent.TButton", width=10)
        add_btn.pack(side=LEFT, padx=5)
        
        # Search and filter area
        filter_frame = ttk.Frame(main_frame)
        filter_frame.pack(fill=X, pady=10)
        
        ttk.Label(filter_frame, text="Search:").pack(side=LEFT, padx=(0, 5))
        search_entry = ttk.Entry(filter_frame, textvariable=self.search_var, width=20)
        search_entry.pack(side=LEFT, padx=5)
        
        ttk.Label(filter_frame, text="Filter:").pack(side=LEFT, padx=(10, 5))
        filter_options = ["All", "Active", "Completed"]
        for option in filter_options:
            ttk.Radiobutton(filter_frame, text=option, variable=self.filter_var, 
                           value=option, command=self.filter_tasks).pack(side=LEFT, padx=5)
        
        # Tasks area
        task_container = ttk.LabelFrame(main_frame, text="My Tasks", padding=10)
        task_container.pack(fill=BOTH, expand=YES, pady=10)
        
        self.tasks_frame = ScrolledFrame(task_container, autohide=True)
        self.tasks_frame.pack(fill=BOTH, expand=YES)
        
        # Bottom buttons
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(fill=X, pady=(10, 0))
        
        clear_completed_btn = ttk.Button(btn_frame, text="Clear Completed", 
                                        command=self.clear_completed, style="warning.TButton")
        clear_completed_btn.pack(side=RIGHT, padx=5)
        
        delete_all_btn = ttk.Button(btn_frame, text="Delete All", 
                                   command=self.delete_all, style="danger.TButton")
        delete_all_btn.pack(side=RIGHT, padx=5)
        
        # Status bar
        self.status_var = tk.StringVar(value="0 tasks")
        status_bar = ttk.Label(main_frame, textvariable=self.status_var, anchor=E)
        status_bar.pack(fill=X, pady=(10, 0))
        
        # Update task display
        self.update_task_display()
    
    def add_task(self):
        task_text = self.task_entry.get().strip()
        if task_text:
            priority = self.priority_combo.get()
            task = {
                "text": task_text,
                "priority": priority,
                "completed": False,
                "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            self.tasks.append(task)
            self.task_entry.delete(0, tk.END)
            self.save_tasks()
            self.update_task_display()
    
    def toggle_task(self, task_index):
        self.tasks[task_index]["completed"] = not self.tasks[task_index]["completed"]
        self.save_tasks()
        self.update_task_display()
    
    def delete_task(self, task_index):
        del self.tasks[task_index]
        self.save_tasks()
        self.update_task_display()
    
    def clear_completed(self):
        if not any(task["completed"] for task in self.tasks):
            messagebox.showinfo("Info", "No completed tasks to clear.")
            return
            
        if messagebox.askyesno("Confirm", "Remove all completed tasks?"):
            self.tasks = [task for task in self.tasks if not task["completed"]]
            self.save_tasks()
            self.update_task_display()
    
    def delete_all(self):
        if not self.tasks:
            messagebox.showinfo("Info", "No tasks to delete.")
            return
            
        if messagebox.askyesno("Confirm", "Delete ALL tasks? This cannot be undone."):
            self.tasks = []
            self.save_tasks()
            self.update_task_display()
    
    def filter_tasks(self, *args):
        self.update_task_display()
    
    def update_task_display(self):
        # Clear previous tasks
        for widget in self.tasks_frame.winfo_children():
            widget.destroy()
        
        # Filter tasks
        filter_type = self.filter_var.get()
        search_text = self.search_var.get().lower()
        
        filtered_tasks = []
        for task in self.tasks:
            # Filter by status
            if filter_type == "Active" and task["completed"]:
                continue
            if filter_type == "Completed" and not task["completed"]:
                continue
            
            # Filter by search text
            if search_text and search_text not in task["text"].lower():
                continue
                
            filtered_tasks.append(task)
        
        # Display filtered tasks
        for i, task in enumerate(filtered_tasks):
            self.create_task_item(i, task)
        
        # Update status
        active_count = sum(1 for task in self.tasks if not task["completed"])
        total_count = len(self.tasks)
        self.status_var.set(f"{active_count} active, {total_count} total")
    
    def create_task_item(self, index, task):
        # Get the real index in the original tasks list
        real_index = self.tasks.index(task)
        
        # Create frame for task
        task_frame = ttk.Frame(self.tasks_frame)
        task_frame.pack(fill=X, pady=3, padx=2)
        
        # Set background based on priority
        priority_colors = {
            "Low": "light",
            "Medium": "info",
            "High": "danger"
        }
        priority_style = priority_colors.get(task["priority"], "light")
        
        # Task item with checkbox
        var = tk.BooleanVar(value=task["completed"])
        cb = ttk.Checkbutton(
            task_frame, 
            variable=var,
            command=lambda idx=real_index: self.toggle_task(idx),
            text="",
            style=f"{priority_style}.TCheckbutton"
        )
        cb.pack(side=LEFT)
        
        # Task text with strikethrough if completed
        if task["completed"]:
            text_style = "success"
            label_font = ("TkDefaultFont", 10, "overstrike")
        else:
            text_style = priority_style
            label_font = ("TkDefaultFont", 10)
        
        task_label = ttk.Label(
            task_frame, 
            text=task["text"],
            font=label_font,
            style=f"{text_style}.TLabel",
            wraplength=450
        )
        task_label.pack(side=LEFT, fill=X, expand=YES, padx=5)
        
        # Priority badge
        priority_badge = ttk.Label(
            task_frame,
            text=task["priority"],
            style=f"{priority_style}.Inverse.TLabel",
            width=8
        )
        priority_badge.pack(side=LEFT, padx=5)
        
        # Delete button
        delete_btn = ttk.Button(
            task_frame,
            text="×",
            width=2,
            command=lambda idx=real_index: self.delete_task(idx),
            style="danger.TButton"
        )
        delete_btn.pack(side=RIGHT, padx=(0, 5))
    
    def load_tasks(self):
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, "r") as f:
                    self.tasks = json.load(f)
            except:
                self.tasks = []
    
    def save_tasks(self):
        with open(self.data_file, "w") as f:
            json.dump(self.tasks, f)

if __name__ == "__main__":
    # Use a modern theme
    root = ttk.Window(themename="darkly")
    app = TodoApp(root)
    root.mainloop()