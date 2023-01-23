
class Singleton(type): # use type as base class of a metaclas
    _instances = {}  # dictionary to keep track of instances

    def __new__(typ, *junk):
        # print("__new__()")
        return super().__new__(typ, *junk)

    def __call__(cls, *args, **kwargs):  # __call__ is passed the new class plus its parameters
        # print("__call__()")
        if cls not in cls._instances:    # check to see if the new class has already been instantiated
            cls._instances[cls] = super().__call__(*args, **kwargs)  # if not, create the (single) class instance and add to dictionary

        return cls._instances[cls]   # return the (single) class instance


class ThingA(metaclass=Singleton):   # Define two different classes which use Singleton
    def __init__(self, value):
        self.value = value


class ThingB(metaclass=Singleton):   # Define two different classes which use Singleton
    def __init__(self, value):
        self.value = value


ta1 = ThingA(1)  # Create instances of ThingA and ThingB
ta2 = ThingA(2)
ta3 = ThingA(3)

tb1 = ThingB(4)
tb2 = ThingB(5)
tb3 = ThingB(6)

for thing in ta1, ta2, ta3, tb1, tb2, tb3:
    print(type(thing).__name__, id(thing), thing.value)  # Print the type, name, and ID of each thing -- only one instance is ever created for each class
