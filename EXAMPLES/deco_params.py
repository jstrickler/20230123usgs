#

from functools import wraps  # wrapper to preserve properties of original function


def multiply(multiplier): # actual decorator -- receives decorator parameters

    def deco(old_func): # "inner decorator" -- receives function being decorated

        @wraps(old_func)  # retain name, etc. of original function
        def new_func(*args, **kwargs): # replacement function -- this is called instead of original
            result = old_func(*args, **kwargs) # call original function and get return value
            return result * multiplier # multiple result of original function by multiplier

        return new_func # deco() returns new_function

    return deco # multiply returns deco



@multiply(4)
def spam():
    return 5


@multiply(10)
def ham():
    return 8

a = spam()
b = ham()
print(a, b)
