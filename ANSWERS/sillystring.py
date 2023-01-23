#!/usr/bin/env python3

def main():
    ss1 = SillyString('this is a test')

    print(ss1.every_other())
    print()

    ss2 = SillyString('Dximd8 *i@tz !w7ogrvkb?#')

    print(ss2.every_other())


def _every_other(self):
    return self._string[::2]


def _init(self, string):
    self._string = string


SillyString = type(
    'SillyString',  # internal class name
    (),  # empty list of base classes
    {'__init__': _init, 'every_other': _every_other} # class dict
)

if __name__ == '__main__':
    main()
