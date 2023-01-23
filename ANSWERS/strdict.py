#!/usr/bin/env python

class StrDict(dict):

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise TypeError("Key must be a string")
        if not isinstance(value, str):
            raise TypeError("Value must be a string")

        key = key.strip().lower()
        value = value.strip().lower()
        super(StrDict, self).__setitem__(key, value)

if __name__ == '__main__':
    s = StrDict()
    for k, v in ('a', 'b'), ('a', 1), (1, 'b'), (1, 1):
        try:
            s[k] = v
        except TypeError as err:
            print(err)

    print(s)
