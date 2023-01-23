#!/usr/bin/env python
# (c)2015 John Strickler
from abc import ABCMeta, abstractmethod

class QuackBase(object, metaclass=ABCMeta):
    @abstractmethod
    def quack(self):
        pass

class Quack(QuackBase):
    def quack(self):
        print('"Quack, quack"')

class Squeak(QuackBase):
    def quack(self):
        print('"Squeaky-squeaky"')

class MuteQuack(QuackBase):
    def quack(self):
        print("<I can't make any sounds>")

if __name__ == '__main__':
    q = Quack()
    q.quack()

    s = Squeak()
    s.quack()

    m = MuteQuack()
    m.quack()
