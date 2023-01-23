#!/usr/bin/env python
# (c)2015 John Strickler

class Cat(object):
    def meow(self):
        print("Meow!!")

class Dog(object):
    def bark(self):
        print("Arf arf!!")

class CatAdapter(Dog):
    def __init__(self, cat):
        self._cat = cat

    def bark(self):
        self._cat.meow()

Garfield = Cat()

dog = CatAdapter(Garfield)
dog.bark()
