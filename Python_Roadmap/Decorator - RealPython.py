#
# Python Functions
#

# First-Class Objects
def say_hello(name):
    return f"Hello {name}"


def be_awesome(name):
    return f"Yo {name}, together we're the awesomest!"


def gret_bob(greeter_func):
    return greeter_func("Bob")


print()
print(gret_bob(say_hello))
print(gret_bob(be_awesome))


# Inner Function
def parent():
    print("Printing from `parent()`")

    def first_child():
        print("Printing from `first_child()`")

    def second_child():
        print("Printing from `second_child()`")

    first_child()
    second_child()


print()
parent()


# Functions as Return Values
def parent(num):
    def first_child():
        return "Hi, I'm Elias"

    def second_child():
        return "Call me Ester"

    if num == 1:
        return first_child
    else:
        return second_child


first = parent(1)
second = parent(2)

print()
print(first)
print(second)

print()
print(first())
print(second())


#
# Simple Decorators in Python
#

def decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper


def say_whee():
    print("Whee!")


print()
say_whee = decorator(say_whee)
say_whee()

print()
print(say_whee)

from datetime import datetime


def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass  # Hush, the neighbors are asleep

    return wrapper


def say_whee():
    print("Whee!")


print()
say_whee = not_during_the_night(say_whee)
say_whee()


# Adding Syntactic Sugar
def decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper


@decorator
def say_whee():
    print("Sheesh!")


print()
say_whee()


# Reusing Decorators
def do_twice(func):
    def wrapper_do_twice():
        func()
        func()

    return wrapper_do_twice


@do_twice
def say_whee():
    print("Raaah!")


print()
say_whee()


# Decorating Functions With Arguments
def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)

    return wrapper_do_twice


@do_twice
def say_whee():
    print("Arsenal!")


@do_twice
def greet(name):
    print(f"Hello {name}")


greet(name="World!")
