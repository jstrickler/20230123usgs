#!/usr/bin/env python
# (c)2015 John Strickler
import flylib
import quacklib

class Duck(object):

    def __init__(
            self,
            duck_type,
            quack=None,
            fly=None
    ):
        self._duck_type = duck_type
        self._quack_behavior = quacklib.Quack() if quack is None else quack
        self._fly_behavior = flylib.FlyWithWings() if fly is None else fly


    def swim(self):
        print("Swimming")

    def display(self):
        print("I am a", self._duck_type)

    def set_quack(self, quack):
        if not issubclass(quack, quacklib.QuackBase):
            raise TypeError("Invalid quack")
        self._quack_behavior = quack

    def set_fly(self, fly):
        if not issubclass(fly, flylib.FlyBase):
            raise TypeError("Invalid flight type")
        self._fly_behavior = fly

    def quack(self):
        self._quack_behavior.quack()

    def fly(self):
        self._fly_behavior.fly()

