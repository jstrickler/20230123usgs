
from functools import wraps


def debugger(old_func):  # decorator function -- expects decorated (original) function as a parameter

    @wraps(old_func)  # @wraps preserves name of original function after decoration
    def new_func(*args, **kwargs):  # replacement function; takes generic parameters
        print("*" * 40)  # new functionality added by decorator
        print("** function", old_func.__name__, "**")  # new functionality added by decorator

        if args:  # new functionality added by decorator
            print("\targs are ", args)
        if kwargs:  # new functionality added by decorator
            print("\tkwargs are ", kwargs)

        print("*" * 40)  # new functionality added by decorator

        return old_func(*args, **kwargs)  # call the original function

    return new_func  # return the new function object


@debugger  # apply the decorator to a function
def hello(greeting, whom='world'):
    print("{}, {}".format(greeting, whom))


hello('hello', 'world')  # call new function
print()

hello('hi', 'Earth')
print()

hello('greetings')
