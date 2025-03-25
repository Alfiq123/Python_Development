import tkinter as tk
from tkinter import messagebox
import random

class BankSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Bank Simulator")
        self.root.geometry("400x500")
        # self.root.resizable(False, False)
        self.root.configure(bg="#f0f0f0")
        
        # Initialize account balance
        self.balance = 1000.00
        self.account_number = f"ACC-{random.randint(10000, 99999)}"
        
        self.create_widgets()
    
    def create_widgets(self):
        # Title
        title_frame = tk.Frame(self.root, bg="#3a7ebf", pady=15)
        title_frame.pack(fill=tk.X)
        
        title_label = tk.Label(title_frame, text="Bank Simulator", font=("Arial", 24, "bold"), bg="#3a7ebf", fg="white")
        title_label.pack()
        
        # Account Info
        info_frame = tk.Frame(self.root, bg="#f0f0f0", pady=20)
        info_frame.pack(fill=tk.X)
        
        account_label = tk.Label(info_frame, text=f"Account Number: {self.account_number}", font=("Arial", 12), bg="#f0f0f0")
        account_label.pack()
        
        self.balance_var = tk.StringVar()
        self.update_balance_display()
        
        balance_label = tk.Label(info_frame, textvariable=self.balance_var, font=("Arial", 18, "bold"), bg="#f0f0f0")
        balance_label.pack(pady=10)
        
        # Transaction Frame
        transaction_frame = tk.Frame(self.root, bg="#f0f0f0", pady=20)
        transaction_frame.pack(fill=tk.X)
        
        # Amount Entry
        amount_frame = tk.Frame(transaction_frame, bg="#f0f0f0")
        amount_frame.pack(pady=10)
        
        amount_label = tk.Label(amount_frame, text="Amount: $", font=("Arial", 14), bg="#f0f0f0")
        amount_label.pack(side=tk.LEFT)
        
        self.amount_entry = tk.Entry(amount_frame, font=("Arial", 14), width=15)
        self.amount_entry.pack(side=tk.LEFT)
        
        # Buttons
        button_frame = tk.Frame(self.root, bg="#f0f0f0", pady=10)
        button_frame.pack()
        
        deposit_button = tk.Button(button_frame, text="Deposit", font=("Arial", 14), 
                                  bg="#4CAF50", fg="white", width=10, command=self.deposit)
        deposit_button.pack(pady=10)
        
        withdraw_button = tk.Button(button_frame, text="Withdraw", font=("Arial", 14), 
                                   bg="#f44336", fg="white", width=10, command=self.withdraw)
        withdraw_button.pack(pady=10)
        
        # Transaction History
        history_frame = tk.LabelFrame(self.root, text="Transaction History", font=("Arial", 12), bg="#f0f0f0", pady=10)
        history_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        self.history_text = tk.Text(history_frame, height=8, width=40, font=("Arial", 10))
        self.history_text.pack(fill=tk.BOTH, expand=True)
        
        # Add scrollbar
        scrollbar = tk.Scrollbar(self.history_text, command=self.history_text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.history_text.config(yscrollcommand=scrollbar.set)
        
        # Initial transaction
        self.add_transaction("Initial balance", self.balance)
    
    def update_balance_display(self):
        self.balance_var.set(f"Balance: ${self.balance:.2f}")
    
    def add_transaction(self, transaction_type, amount):
        transaction_text = f"{transaction_type}: ${amount:.2f}\n"
        self.history_text.insert(tk.END, transaction_text)
        self.history_text.see(tk.END)  # Scroll to the end
    
    def deposit(self):
        try:
            amount = float(self.amount_entry.get())
            if amount <= 0:
                messagebox.showerror("Error", "Please enter a positive amount.")
                return
                
            self.balance += amount
            self.update_balance_display()
            self.add_transaction("Deposit", amount)
            self.amount_entry.delete(0, tk.END)
            messagebox.showinfo("Success", f"${amount:.2f} deposited successfully.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount.")
    
    def withdraw(self):
        try:
            amount = float(self.amount_entry.get())
            if amount <= 0:
                messagebox.showerror("Error", "Please enter a positive amount.")
                return
                
            if amount > self.balance:
                messagebox.showerror("Error", "Insufficient funds!")
                return
                
            self.balance -= amount
            self.update_balance_display()
            self.add_transaction("Withdrawal", amount)
            self.amount_entry.delete(0, tk.END)
            messagebox.showinfo("Success", f"${amount:.2f} withdrawn successfully.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount.")

if __name__ == "__main__":
    root = tk.Tk()
    app = BankSimulator(root)
    root.mainloop()
