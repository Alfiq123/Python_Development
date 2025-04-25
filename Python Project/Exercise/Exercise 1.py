
# TODO 1: Calculate the multiplication and sum of two numbers
# TODO 2: Print the Sum of a Current Number and a Previous number
# TODO 3: Print characters present at an even index number
# TODO 4: Remove first "n" characters from a string
# TODO 5: Check if the first and last numbers of a list are the same

## * Exercise 1: Calculate the multiplication and sum of two numbers
    # ? Given two integer numbers,
    # ? write a Python code to return their product only if the product is equal to or lower than 1000. 
    # ? Otherwise, return their sum.

def two_int(number_1, number_2):
    return (number_1 * number_2) if (number_1 * number_2) <= 1000 else number_1 + number_2

print(two_int(40, 30))


## * Exercise 2: Print the Sum of a Current Number and a Previous number
    # ? Write a Python code to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.

def sum_number(number):
    previous = 0
    for current in range(number):
        sum_n = current + previous
        print(f"Current Number ({current}) Previous Number ({previous}) Sum: {sum_n}")
        previous = current


## * Exercise 3: Print characters present at an even index number
    # ? Write a Python code to accept a string from the user and display characters present at an even index number.

def display_char(text):
    return text[::2]


## * Exercise 4: Remove first `n` characters from a string
    # ? Write a Python code to remove characters from a string from 0 to n and return a new string.

def first_n(text, slice):
    return text[slice:]


## * Exercise 5: Check if the first and last numbers of a list are the same
    # ? Write a code to return "True" if the list’s first and last numbers are the same. If the numbers are different, return "False".

def same_first(type_list):
    return True if type_list[0] == type_list[-1] else False
