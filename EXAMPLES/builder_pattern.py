#
from abc import ABCMeta, abstractmethod


class Director(object):

    def construct(self, builder):
        '''
        Builder uses multiple steps
        :param builder: A Builder object
        :return:
        '''
        builder.build_part_A()
        builder.build_part_B()

class BuilderBase(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def build_part_A(self): pass

    @abstractmethod
    def build_part_B(self): pass

    @abstractmethod
    def get_result(self): pass

class Product(object):
    def __init__(self, name):
        self._name = name
        self._parts = []

    def add(self, part):
        self._parts.append(part)

    def show(self):
        print("{} Parts -------".format(self._name))
        for part in self._parts:
            print(part)
        print()

class Builder1(BuilderBase):
    def __init__(self):
        self._product = Product("Product 1")

    def build_part_A(self):
        self._product.add("PartA")

    def build_part_B(self):
        self._product.add("PartB")

    def get_result(self):
        return self._product


class Builder2(BuilderBase):
    def __init__(self):
        self._product = Product("Product 2")

    def build_part_A(self):
        self._product.add("PartX")

    def build_part_B(self):
        self._product.add("PartY")

    def get_result(self):
        return self._product

if __name__ == '__main__':
    director = Director()
    builder1 = Builder1()
    builder2 = Builder2()

    director.construct(builder1)
    product1 = builder1.get_result()
    product1.show()

    director.construct(builder2)
    product2 = builder2.get_result()
    product2.show()
