import time


def hello():
    print("Hello")


# even functions are objects
message = hello

# call new function
message()


# Example
def hello(func):
    def inner():
        print("Hello ", end="")
        func()

    return inner


def name():
    print("Alice")


obj = hello(name)
obj()


# Example 2
def who():
    print("Alice")


def display(func):
    def inner():
        print("The current user is: ", end="")
        func()

    return inner


@hello
def name():
    print("Alice")


# Arguments
def sumab(a, b):
    summed = a + b
    print(summed)


def pretty_sumab(func):
    def inner(a, b):
        print(str(a) + " + " + str(b) + " is ", end="")
        return func(a, b)

    return inner


@pretty_sumab
def sumab(a, b):
    summed = a + b
    print(summed)


# Real World Example
def my_function(n):
    time.sleep(n)


def measure_time(func):
    def wrapper(*args):
        t = time.time()
        res = func(*args)
        print("Function took " + str(time.time() - t) + " seconds to run")
        return res

    return wrapper


@measure_time
def my_function(n):
    time.sleep(n)


if __name__ == "__main__":
    myobj = display(who)
    myobj()

    name()

    sumab(a=5, b=3)

    my_function(2)
