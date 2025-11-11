# def f_1() -> None:
#     print("Called ** F1 **")
#
#
# def f_2(f):
#     f()
#
#
# f_2(f_1)
#
#
# def f_1(var_func):
#     def wrapper(*args, **kwargs):
#         print("\nStarter")
#         var = var_func(*args, **kwargs)
#         print("Ended\n")
#         return var
#
#     return wrapper
#
#
# @f_1
# def f(param_a, param_b) -> None:
#     ## print("Hello")
#     print(param_a, param_b)
#
#
# ## f_1(f)()
# ## x = f_1(f)
# ## x()
#
# ## print(f_1(f))
# ## print(f_1(f)())
#
# ## f()
# f("Hi,", "Neutron")
# f(param_a="Hi,", param_b="Neutron")
#
#
# @f_1
# def add(x, y):
#     return x + y
#
#
# print(add(4, 5))
# print(add(5, 8))
# print(add(12, 24))


from time import time, sleep
from datetime import datetime


# Example 1
def before_after(var_func):
    def var_wrapper(*args):
        print("Before")
        var_func(*args)
        print("After")

    return var_wrapper


class Test:
    @before_after
    def decorated_method(self):
        print("Run")


# Example 2
def timer(let_func):
    def let_wrapper():
        let_before = time()
        let_func()
        print(f"Function took: {time() - let_before} seconds")

    return let_wrapper


@timer
def run():
    sleep(2)


# Example 3
def log(func):
    def wrapper(*args, **kwargs):
        with open("logs.txt", "a") as f:
            f.write(
                f"Called function with {' '.join([str(arg) for arg in args])} at {datetime.now()}\n"
            )
        val = func(*args, **kwargs)
        return val

    return wrapper


@log
def run_b(a, b, c=9):
    print(a + b + c)


if __name__ == "__main__":
    test = Test()
    test.decorated_method()

    run()
    run_b(5, 6, c=9)
