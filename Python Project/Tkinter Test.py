# from tkinter import *

# root = Tk()
# button = Button(root, text="Click me")
# button.pack()
# root.mainloop()

# import tkinter

# root = tkinter.Tk()
# button = tkinter.Button(root, text="Click me")
# button.pack()
# root.mainloop()

# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance
#         pass

from abc import ABC, abstractmethod  
class Shape(ABC):  
    @abstractmethod  
    def area(self):  
        pass  