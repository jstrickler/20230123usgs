from abc import ABCMeta, abstractmethod

class Animal(metaclass=ABCMeta):  # metaclasses control how classes are created; ABCMeta adds restrictions to classes that inherit from Animal

    @abstractmethod   # when decorated with @abstractmethod, speak() becomes an abstract method
    def speak(self):
        pass

class Dog(Animal):  # Inherit from abstract base class Animal
    def speak(self):   # speak() must be implemented
        print("woof! woof!")

class Cat(Animal):  # Inherit from abstract base class Animal
    def speak(self):  # speak() must be implemented
        print("Meow meow meow")

class Duck(Animal): # Inherit from abstract base class Animal
    pass  # Duck does not implement speak()

d = Dog()
d.speak()

c = Cat()
c.speak()

try:
    d = Duck()  # Duck throws a TypeError if instantiated
    d.speak()
except TypeError as err:
    print(err)
