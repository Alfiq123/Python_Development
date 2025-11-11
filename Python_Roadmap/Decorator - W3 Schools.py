def change_case(func):
    def my_inner():
        return func().upper()

    return my_inner


@change_case
def my_function() -> str:
    return "Hello Sally"


print(my_function())


# Multiple Decorator Calls
def change_case(func):
    def my_inner():
        return func().upper()

    return my_inner


@change_case
def my_function() -> str:
    return "Hello Adam"


@change_case
def other_function() -> str:
    return "I'm speed!"


print(my_function())
print(other_function())


# Arguments in the Decorated Function

# Fungsi yang memerlukan argumen juga dapat didekorasi,
# └ pastikan Kamu meneruskan argumen ke fungsi pembungkus:

def change_case(func):
    def my_inner(x):
        return func(x).upper()

    return my_inner


@change_case
def my_function(name) -> str:
    return f"Hello {name}"


print(my_function("John"))


# `*args` and `**kwargs`

# Terkadang fungsi dekorator tidak memiliki kendali
# └ atas argumen yang diteruskan dari fungsi yang didekorasi.
# Untuk mengatasi masalah ini, tambahkan (`*args`, `**kwargs`) ke fungsi pembungkus.
# Dengan cara ini, fungsi pembungkus dapat menerima jumlah dan jenis argumen apa pun,
# └ dan meneruskannya ke fungsi yang didekorasi.
def change_case(func):
    def my_inner(*args, **kwargs):
        return func(*args, **kwargs).upper()

    return my_inner


@change_case
def my_function(name) -> str:
    return f"Hello {name}"


print(my_function(name="Price"))


# Decorator With Arguments

# Dekorator dapat menerima argumen mereka sendiri
# └ dengan menambahkan tingkat pembungkus tambahan.
def change_case(n):
    def change_case(func):
        def my_inner():
            if n == 1:
                a = func().lower()
            else:
                a = func().upper()
            return a

        return my_inner

    return change_case


@change_case(1)
def my_function_1() -> str:
    return "Hello Linda"


@change_case(2)
def my_function_2() -> str:
    return "Hello Apache"


print(my_function_1())
print(my_function_2())


# Multiple Decorators

# Kamu dapat menggunakan beberapa dekorator pada satu fungsi.
# Hal ini dilakukan dengan menempatkan panggilan dekorator satu di atas yang lain.
# Dekorator dipanggil dalam urutan terbalik, dimulai dari yang paling dekat dengan fungsi.

def change_case(func):
    def my_inner():
        return func().upper()

    return my_inner


def add_greeting(func):
    def my_inner() -> str:
        return f"Hello {func()}, Have a good day!"

    return my_inner


@change_case  # 2. Selanjutnya
@add_greeting  # 1. Mulai Duluan
def my_function() -> str:
    return "Tobias"


print(my_function())


# Preserving Function Metadata

# Fungsi dalam Python memiliki metadata yang dapat diakses menggunakan atribut `__name__` dan `__doc__`.
def my_function() -> str:
    return "Have a great day!"


print(my_function.__name__)
print(my_function().__doc__)


# Namun, ketika suatu fungsi diberi dekorasi, metadata dari fungsi asli akan hilang.

def change_case(func):
    def my_inner():
        return func().upper()

    return my_inner


@change_case
def my_function() -> str:
    return "Have a great day!"


print(my_function.__name__)

# Untuk memperbaiki hal ini, Python memiliki fungsi bawaan bernama `functools.wraps`
# └ yang dapat digunakan untuk mempertahankan nama dan docstring fungsi asli.

from functools import wraps


def change_case(func):
    @wraps(func)
    def my_inner():
        return func().upper()

    return my_inner


@change_case
def my_function() -> str:
    return "Have a great day!"


print(my_function.__name__)
