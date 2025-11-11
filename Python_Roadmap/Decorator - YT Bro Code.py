# Decorator = A function that extends the behavior of another function
#             w/o modifying the base function
#             Pass the base function as an argument to the decorator

def add_sprinkles(func_any):
    def whatever(*args, **kwargs) -> None:
        print("** 🧁 You add sprinkles 🧁 **")
        func_any(*args, **kwargs)

    return whatever


def add_fudge(func_again):
    def whenever(*args, **kwargs) -> None:
        print("** 🍫 You add fudge 🍫 **")
        func_again(*args, **kwargs)

    return whenever


@add_sprinkles
@add_fudge
def get_ice_cream(flavor: str) -> None:
    print(f"\n🍨🍦 Here is your {flavor} ice cream 🍦🍨\n")


get_ice_cream(flavor="Vanilla")
get_ice_cream(flavor="Chocolate")
get_ice_cream(flavor="Strawberry")
