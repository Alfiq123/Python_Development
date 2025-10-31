import customtkinter as ctk

from os import path
from PIL import Image
from tkinter import PhotoImage


class MainApp(ctk.CTk):
    """ Main Application Class """

    def __init__(self):
        super().__init__()

        self.title("Coffee Maker")
        self.resizable(width=False, height=False)
        self.grid_columnconfigure(index=0, weight=1)

        self.app_icon = None
        self.icon_reset = None
        self.icon_served = None

        # ═════ Load Assets ═════ #
        self.icon_coffee = self.load_image(filename="icon_coffee-beans.png")
        self.icon_milk = self.load_image(filename="icon_milk.png")
        self.icon_water = self.load_image(filename="icon_water-drop.png")
        self.icon_latte = self.load_image(filename="icon_latte.png")
        self.icon_espresso = self.load_image(filename="icon_espresso.png")
        self.icon_mochaccino = self.load_image(filename="icon_mochaccino.png")

        self.images()
        self.center_window(width=500, height=500)

        # ═════ Drink Counter ═════ #
        self.drink = {
            "latte": 0,
            "espresso": 0,
            "mochaccino": 0
        }

        # ═════ Resources Counter ═════ #
        self.resources = {
            "water": 1200,
            "milk": 1100,
            "coffee": 1000
        }

        # ═════ Ingredient Needed ═════ #
        self.ingredients = {
            "latte": {
                "water": 120,
                "milk": 150,
                "coffee": 100
            },
            "mochaccino": {
                "water": 100,
                "milk": 140,
                "coffee": 120
            },
            "espresso": {
                "water": 60,
                "milk": 80,
                "coffee": 120
            }
        }

        self.label = ctk.CTkLabel(
            master=self,
            text="Coffee Machine Simulator",
            font=("Helvetica", 24, "bold")
        )
        self.label.grid(row=0, column=0, padx=10, pady=20)

        self.lbl_instance = Labels(self)
        self.btn_instance = Buttons(self)

    @staticmethod
    def load_image(filename):
        """ Load images and icons """
        return ctk.CTkImage(
            dark_image=Image.open(
                path.join(path.dirname(__file__), "Assets", filename)
            ), size=(64, 64)
        )

    def images(self):
        """ Store images and Icons """
        self.app_icon = PhotoImage(
            file=path.join(
                path.dirname(__file__), "Assets", "icon_coffee-cup.png"
            )
        )
        self.iconphoto(True, self.app_icon)

        self.icon_served = ctk.CTkImage(
            dark_image=Image.open(
                path.join(
                    path.dirname(__file__), "Assets", "icon_coffee_served.png"
                )
            ), size=(32, 32)
        )

        self.icon_reset = ctk.CTkImage(
            dark_image=Image.open(
                path.join(
                    path.dirname(__file__), "Assets", "icon_reset.png"
                )
            ), size=(32, 32)
        )

    def center_window(self, width, height):
        """
        Centers the window on the screen with a specified width and height.
        In this structure, 'self' refers to the main CTk window.
        """
        # Access screen dimensions directly via 'self' (the window object)
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Calculate x and y coordinates for the window to be centered
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)

        # Set the window's geometry directly via 'self'
        self.geometry(f"{width}x{height}+{x}+{y}")

    def update_ui(self):
        """
        Method in MainApp to coordinate UI updates.
        Called by other classes (like Buttons) to refresh the display.
        """
        self.lbl_instance.update_labels()
        self.btn_instance.update_buttons()
        # If other UI elements need updating, add calls here.


class Labels:
    """ Class for Labels """

    def __init__(self, parent):
        self.parent = parent

        # ════════════════════════════════════════════════════════════ #

        # Frame for labels.
        self.frame = ctk.CTkFrame(master=parent)
        self.frame.grid(row=1, column=0, padx=10, pady=20)

        # ═══ Water Status ═══ #
        self.lbl_water = ctk.CTkLabel(
            master=self.frame,
            text=f"{parent.resources['water']}",
            font=("Helvetica", 14),
            image=parent.icon_water,
            compound="top",
            width=64
        )
        self.lbl_water.grid(row=0, column=0, padx=10, pady=10)

        # ═══ Milk Status ═══ $
        self.lbl_milk = ctk.CTkLabel(
            master=self.frame,
            text=f"{parent.resources['milk']}",
            font=("Helvetica", 14),
            image=parent.icon_milk,
            compound="top",
            width=64
        )
        self.lbl_milk.grid(row=0, column=1, padx=10, pady=10)

        # ═══ Coffee Status ═══ $
        self.lbl_coffee = ctk.CTkLabel(
            master=self.frame,
            text=f"{parent.resources['coffee']}",
            font=("Helvetica", 14),
            image=parent.icon_coffee,
            compound="top",
            width=64
        )
        self.lbl_coffee.grid(row=0, column=2, padx=10, pady=10)

    def update_labels(self):
        self.lbl_water.configure(
            text=f"{self.parent.resources['water']}"
        )
        self.lbl_milk.configure(
            text=f"{self.parent.resources['milk']}"
        )
        self.lbl_coffee.configure(
            text=f"{self.parent.resources['coffee']}"
        )


class Buttons:
    """ Class for Buttons """

    def __init__(self, parent):
        self.parent = parent

        # ════════════════════════════════════════════════════════════ #

        # Frame for buttons.
        self.frame = ctk.CTkFrame(master=parent)
        self.frame.grid(row=2, column=0, padx=10, pady=20)

        # ═══ Latte ═══ #
        self.btn_latte = ctk.CTkButton(
            master=self.frame,
            text="0",
            font=("Helvetica", 14),
            command=self.add_latte,
            image=parent.icon_latte,
            compound="top",
            width=64,
        )
        self.btn_latte.grid(row=0, column=0, padx=10, pady=20)

        # ═══ Espresso ═══ #
        self.btn_espresso = ctk.CTkButton(
            master=self.frame,
            text="0",
            font=("Helvetica", 14),
            command=self.add_espresso,
            image=parent.icon_espresso,
            compound="top",
            width=64,
        )
        self.btn_espresso.grid(row=0, column=1, padx=10, pady=20)

        # ═══ Mochaccino ═══ #
        self.btn_mochaccino = ctk.CTkButton(
            master=self.frame,
            text="0",
            font=("Helvetica", 14),
            command=self.add_mochaccino,
            image=parent.icon_mochaccino,
            compound="top",
            width=64,
        )
        self.btn_mochaccino.grid(row=0, column=2, padx=10, pady=20)

        # Confirmation Button
        self.btn_confirm = ctk.CTkButton(
            master=self.frame,
            text="",
            font=("Helvetica", 14),
            command=self.logic_func,
            image=parent.icon_served,
            width=25
        )
        self.btn_confirm.grid(row=1, column=0, padx=10, pady=20, columnspan=2)

        # Reset Button
        self.btn_reset = ctk.CTkButton(
            master=self.frame,
            text="",
            font=("Helvetica", 14),
            command=self.reset_func,
            image=parent.icon_reset,
            width=25
        )
        self.btn_reset.grid(row=1, column=1, padx=10, pady=20, columnspan=2)

    def add_latte(self):
        """ Increase Latte count and update button text """
        self.parent.drink["latte"] += 1
        self.btn_latte.configure(
            text=f"{self.parent.drink['latte']}"
        )

    def add_espresso(self):
        """ Increase Espresso count and update button text """
        self.parent.drink["espresso"] += 1
        self.btn_espresso.configure(
            text=f"{self.parent.drink['espresso']}"
        )

    def add_mochaccino(self):
        """ Increase Mochaccino count and update button text """
        self.parent.drink["mochaccino"] += 1
        self.btn_mochaccino.configure(
            text=f"{self.parent.drink['mochaccino']}"
        )

    def logic_func(self):
        """ Reduce ingredients based on the requirements """
        for drink, ingredients in self.parent.ingredients.items():
            count = self.parent.drink[drink]
            if count > 0:
                print(f"Making {count} {drink}(s). Reducing resources...")
                for resource, amount in ingredients.items():
                    total_used = amount * count
                    self.parent.resources[resource] -= total_used
        self.reset_func()
        self.parent.update_ui()

    def reset_func(self):
        """ Reset the buttons """
        for i in self.parent.drink:
            self.parent.drink[i] = 0
        self.parent.update_ui()

    def update_buttons(self):
        """ Updating the buttons """
        self.btn_latte.configure(
            text="0"
        )
        self.btn_espresso.configure(
            text="0"
        )
        self.btn_mochaccino.configure(
            text="0"
        )


if __name__ == "__main__":
    main = MainApp()
    main.mainloop()
