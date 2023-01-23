#!/usr/bin/env python

from functools import wraps

def print_name( old_func ):

    @wraps(old_func)
    def new_func( *args, **kwargs ):
        # added functionality
        print("==> Calling function {0}".format(old_func.__name__))
        return old_func( *args, **kwargs )  # call the 'real' function

    return new_func   # return the new function object


@print_name
def hello():
    print("Hello!")

@print_name
def goodbye():
    print("Goodbye!")

hello()
goodbye()
hello()
goodbye()
