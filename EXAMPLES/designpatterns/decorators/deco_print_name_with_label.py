#!/usr/bin/env python

from functools import wraps

def print_name(label):

    def wrapper(old_func):

        @wraps(old_func)
        def new_func( *args, **kwargs ):
            # added functionality
            print("{0}: function {1}".format(
                label,
                old_func.__name__
            ))
            return old_func( *args, **kwargs )  # call the 'real' function

        return new_func   # return the new function object
    return wrapper

@print_name('HELLO')
def hello():
    print("Hello!")

@print_name('HELLO')
def howdy():
    print("Howdy!")

@print_name('GOODBYE')
def goodbye():
    print("Goodbye!")

@print_name('GOODBYE')
def solong():
    print("So long!")


hello()
howdy()
goodbye()
solong()
