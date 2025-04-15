import random
import string
import tkinter as tk


class LetterGenerator:
    def __init__(self):
        self.reset_deck()

    def reset_deck(self):
        # Create a new shuffled deck of A–Z
        self.deck = list(string.ascii_uppercase)
        random.shuffle(self.deck)

    def next_letter(self):
        if not self.deck:
            self.reset_deck()
        return self.deck.pop()


# GUI setup
gen = LetterGenerator()


def show_letter():
    letter = gen.next_letter()
    label.config(text=letter)


root = tk.Tk()
root.title("Random Letter Generator")
root.geometry("800x600")

label = tk.Label(root, text="", font=("Helvetica", 300))
label.pack(pady=40)

button = tk.Button(
    root,
    text="Generate Letter",
    command=show_letter,
    font=("Helvetica", 24),
    width=20,
    height=2
)
button.pack(pady=20)

root.mainloop()