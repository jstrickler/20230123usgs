
class Meta(type):

    def __prepare__(class_name, bases):
        """
        "Prepare" the new class. Here you can update the base classes.

        :param name: Name of new class as a string
        :param bases: Tuple of base classes
        :return: Dictionary that initializes the namespace for the new class (must be a dict)
        """
        print("in metaclass (class={}) __prepare__()".format(class_name), end=' ==> ')
        print("params: name={}, bases={}".format(class_name, bases))
        return {'animal': 'wombat', 'id': 100}

    def __new__(metatype, name, bases, attrs):
        """
        Create the new class. Called after __prepare__(). Note this is only called when classes

        :param metatype: The metaclass itself
        :param name: The name of the class being created
        :param bases: bases of class being created (may be empty)
        :param attrs: Initial attributes of the class being created
        :return:
        """
        print("in metaclass (class={}) __new__()".format(name), end=' ==> ')
        print("params: type={} name={} bases={} attrs={}".format(metatype, name, bases, attrs))
        return super().__new__(metatype, name, bases, attrs)

    def __init__(cls, *args):
        """

        :param cls: The class being created (compare with 'self' in normal class)
        :param args: Any arguments to the class
        """
        print("in metaclass (class={}) __init__()".format(cls.__name__), end=' ==> ')
        print("params: cls={}, args={}".format(cls, args))

        super().__init__(cls)

    def __call__(self, *args, **kwargs):
        """
        Function called when the metaclass is called, as in NewClass = Meta(...)

        :param args:
        :param args:
        :param kwargs:
        :return:
        """
        print("in metaclass (class={})__call__()".format(self.__name__))


class MyBase():
    pass

print('=' * 60)

class A(MyBase, metaclass=Meta):
    id = 5

    def __init__(self):
        print("In class A __init__()")

print('=' * 60)

class B(MyBase, metaclass=Meta):
    animal = 'wombat'

    def __init__(self):
        print("In class B __init__()")


print('-' * 60)
m1 = A()
print('-' * 60)
m2 = B()
print('-' * 60)
m3 = A()
print('-' * 60)
m4 = B()
print('-' * 60)
print("animal: {} id: {}".format(A.animal, B.id))
