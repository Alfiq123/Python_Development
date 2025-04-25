
# TODO 1: Convert radians into degrees
# TODO 2: Sort a List
# TODO 3: Convert a decimal number into binary
# TODO 4: Count the vowels in a string
# TODO 5: Hide the credit card number
# TODO 6: Are the Xs equal to the Os?
# TODO 7: Create a calculator function
# TODO 8: Give me the discount
# TODO 9: Just the numbers
# TODO 10: Repeat the characters
# TODO 11: Convert lowercase to uppercase
# TODO 12: Add dots


def radian_to_degree(radian):
    return radian * (180 / 3.141592653589793)


def sort_a_list(list_1, sorting):
    if sorting == "asc":
        return sorted(list_1)
    elif sorting == "desc":
        return sorted(list_1, reverse = True)
    else:
        return list_1


def decimal_to_binary(decimal):
    return bin(decimal)[2:]


def vowel(string):
    return sum(1 for word in string if word in ("a", "i", "u", "e", "o"))


def hide_credit_card(card_num):
    return "*" * (len(card_num) - 4) + card_num[-4:]
    

def x_equal_to_o(string):
    # string = string.lower()
    # return string.count('x') == string.count('o')
    return string.count("x".lower()) == string.count("o".lower())


def calculator(num_1, operator, num_2):
    if operator == "+":
        return num_1 + num_2
    elif operator == "-":
        return num_1 - num_2
    elif operator == "*":
        return num_1 * num_2
    elif operator == "/":
        return num_1 / num_2
    

def discount(price, disc):
    return (price - (price * (disc / 100)))


def just_integers(lst):
    return [x for x in lst if isinstance(x, int)]


def repeat_character(string):
    return ''.join([rep * 2 for rep in string])


def lower_tp_upper(string):
    return string.upper()


def add_dots(string):
    return ".".join(string)
