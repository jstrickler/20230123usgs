#!/usr/bin/env python

# list.__getitem__ = lambda index: 42
#
# x = [1, 2, 3]
# print(x[0])


class MaxList(list):
    def __init__(self, max_size):
        self._max_size = max_size

    def set_index(self, value):
        pass

    def append(self, value):
        if len(self) == self._max_size:
            raise IndexError("Maximum size reached")
        else:
            super().append(value)

if __name__ == '__main__':

    m = MaxList(3)

    for letter in 'abcdef':
        try:
            m.append(letter)
        except IndexError as err:
            print(err)
        print(m)

    print(type(m))
    print(isinstance(m, list))
    x = m[::]
    print(x)
    print(type(x))

    MaxList.__getitem__ = lambda self, index: 42

    print(m[3])
    print(m["wombat"])

