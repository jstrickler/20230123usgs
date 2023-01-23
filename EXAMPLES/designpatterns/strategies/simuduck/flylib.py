#!/usr/bin/env python
# (c)2015 John Strickler

from abc import ABCMeta, abstractmethod

class FlyBase(object, metaclass=ABCMeta):
    @abstractmethod
    def fly(self):
        pass

class FlyWithWings(FlyBase):
    def fly(self):
        print("Soaring on my wings")

class Flightless(FlyBase):
    def fly(self):
        print("Gee, I can't fly")

if __name__ == '__main__':
    fww = FlyWithWings()
    fww.fly()

    fl = Flightless()
    fl.fly()
