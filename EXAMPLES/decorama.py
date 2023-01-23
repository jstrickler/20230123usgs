"""
decorama -- demo of 8 combinations of decorator implementation

decorators applied to functions:
    1. decorator without args   @deco_func
        decorator returns replacement function
    2. decorator with args  @deco_func(arg, ...)
        decorator returns wrapper
        wrapper returns replacement function
    3. class without args   @deco_class
        __call__ IS replacement function
    4. class with args   @deco_class(arg, ...)
        __call__ RETURNS replacement function

#TODO: straighten this mess out
decorators applied to classes:
    (NOTE: replacement class is frequently the original class, but doesn't have to be)
    5. decorator function without args @deco_func
        decorator returns replacement class
    6. decorator function with args @deco_func(arg, ...)
        decorator returns wrapper
        wrapper return replacement class
    7. decorator class without args @deco_class
        __call__ returns replacement class
    8. decorator class with args @deco_class(arg, ...)
        ???
"""

from functools import wraps, update_wrapper


def deco_one(wrapped_function):
    """
    function without params decorating a function -- the simplest kind of decorator

    @deco_one
    def bar():
        pass

    same as
    bar = deco_one(bar)


    :param wrapped_function: function to decorate
    :return: replacement function
    """
    @wraps(wrapped_function)
    def _replacement(*args, **kwargs):
        print("GREETINGS from deco_one!")
        result = wrapped_function(*args, **kwargs)
        return result + 1

    return _replacement

@deco_one
def target_one():
    print("Hello from target_one")
    return 1

print('-' * 60)
print("** deco_one() **")
print('-' * 60)

result = target_one()
print("target_one() result is:", result)
result = target_one()
print("target_one() result is:", result)

print('-' * 60)

def deco_two(animal):
    """
    function with params decorating a function

    The decorator gets the args, and then returns a wrapper
    function.

    The wrapper gets the function being wrapped, and returns
    the replacement function.

    @deco_two('some string')
    def bar():
        pass

    same as
    bar  = deco_two('some_string')(bar)
    or,
    wrapper = foo('blah')
    bar = wrapper(bar)


    :param value: decorator parameter
    :return: wrapper function (which returns replacement function)
    """

    def wrapper(wrapped_function):

        @wraps(wrapped_function)
        def _replacement(*args, **kwargs):
            print(("GREETINGS from deco_two -- animal is {}!".format(animal)))
            result = wrapped_function(*args, **kwargs)
            return result

        return _replacement

    return wrapper

@deco_two('wombat')
def target_two_alpha():
    print("GREETINGS from target_two_alpha")

@deco_two('coatimundi')
def target_two_beta():
    print("GREETINGS from target_two_beta")

target_two_alpha()
target_two_alpha()
target_two_beta()

class DecoThree():
    """
    class without params decorating a function

    __call__() is the replacement function

    __init__() is passed the wrapped function

    @DecoThree
    def bar():
        pass

    same as
    bar  = DecoThree(bar)


    """

    def __init__(self, wrapped_function):
        self.__name__ = wrapped_function.__name__
        self._wrapped = wrapped_function

    def __call__(self, *args, **kwargs):
        print("GREETINGS from deco_three!")
        result = self._wrapped(*args, **kwargs)
        return result + 3


class DecoFour():
    """
    class with params decorating a function

    __call__() RETURNS the replacement function


    @deco_four('blah')
    def bar():
        pass

    same as
    bar  = deco_four('blah')(bar)
    or,
    wrapper = deco_four('blah')
    bar = wrapper(bar)
    """

    def __init__(self, value):
        self._value = value

    def __call__(self, wrapped_function):
        @wraps(wrapped_function)
        def _replacement(*args, **kwargs):
            print(("GREETINGS from deco_four -- value is {}!".format(self._value)))
            result = wrapped_function(*args, **kwargs)
            return result + 4

        return _replacement


print("Function decorators:")


@deco_one
@deco_two('APPLE')
@DecoThree
@DecoFour('BANANA')
def target_function(color, value):
    """
    Target function for decorators 1-4

    :param color: Color as string
    :param value: Any value
    :return: None
    """
    print(("Hello from target_function -- color is {} and value is {}".format(color, value)))
    print(("Target function's name is", target_function.__name__))
    return 10 * value


TF_RESULT = target_function('red', 10)
print(("RESULT is", TF_RESULT))
print(('-' * 50))
TF_RESULT = target_function('green', 45)
print(("RESULT is", TF_RESULT))
print(('-' * 50))
print()
print()


def deco_five(target_class):
    """
    function without params decorating a class

    :param target_class: class to be decorated
    :return: modified class
    """
    print("GREETINGS from deco_five!")

    @property
    def _temp(self):
        return self._value1

    target_class.value_one = _temp

    return target_class


def deco_six(fruit):
    """
    function with params decorating a class; returns wrapper which is applied to target class

    :param fruit:
    :return: modified class
    """
    print("GREETINGS from deco_six!")

    def wrapper(target_class):
        target_class._fruit = fruit

        @property
        def _temp(self):
            return self._fruit

        target_class.fruit = _temp

        return target_class

    return wrapper


@deco_five
@deco_six('MANGO')
class TargetClass():

    def __init__(self, v1, v2, v3, v4):
        self._value1 = v1
        self._value2 = v2
        self._value3 = v3
        self._value4 = v4


T1 = TargetClass('fee', 'fi', 'fo', 'fum')
print(("T1 is", T1))
print(("value_one:", T1.value_one))

print(('-' * 50))
T2 = TargetClass('eeny', 'meeny', 'miny', 'mo')
print(("T2:", T2))
print(("T2.value_one:", T2.value_one))
print(("T2.fruit:", T2.fruit))

print(('-' * 50))


class DecoSeven():
    """
    class without params decorating a class

    __new__() returns the modified class (not __init__, because __init__ is *instance* initializer)

    """

    def __new__(cls, class_):   # self is the old class
        print("GREETINGS from deco_seven!")
        class_.color = 'blue'
        return class_


@DecoSeven
class TargetClass():
    pass


T1 = TargetClass()
print((T1.color))
print(("T1 id:", id(T1)))
print((TargetClass.__name__, T1))

T2 = TargetClass()
print((T2.color))
print(("T2 id:", id(T2)))

print(('-' * 50))


class DecoEight():
    """
    class with params decorating a class

    __call__() returns the modified class
    """

    def __init__(self, color):
        print("GREETINGS from deco_eight!")
        self._color = color

    def __call__(self, old_class):
        old_class.color = self._color
        return old_class


@DecoEight('purple')
class TargetClass():
    pass

T1 = TargetClass()
print((T1.color))
