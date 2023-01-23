#!/usr/bin/env python
# (c) 2018 CJ Associates
#
from functools import wraps

def double_return(old_func):

    @wraps(old_func)
    def new_func(*args, **kwargs):
        result = old_func(*args, **kwargs)
        return result * 2

    return new_func


@double_return
def add(x, y):
    return x + y


@double_return
def bark():
    return "woof!"


print(add(2, 2))
print(add(1, 9))
print(bark())
