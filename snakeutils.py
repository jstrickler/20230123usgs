#!/usr/bin/env python
import re

rx_capword = re.compile(r"[A-Z][^A-Z]+")
rx_nonword = re.compile(r"[^a-zA-Z0-9]+")

def snake_to_camel(name):
    # should split FooBar as well
    if re.search('[A-Z]', name):
        new_name = ""
        for word in rx_capword.findall(name):
            new_word = split_word(word)
            new_name += new_word
    else:
        new_name = split_word(name)

    return new_name

def split_word(word):
    words = rx_nonword.split(word)
    return ''.join(w.capitalize() for w in words)


if __name__ == '__main__':
    test_strings = [
        "junk stuff",
        "test_case",
        "wombat_nest",
        "blue_meany",
        "funk-ball",
        "BigOld_world",
        "Spam.Toast",
        "JunkFile",
        "blorb",
    ]

    for t in test_strings:
        print("{:12s} {}".format(t, snake_to_camel(t)))

