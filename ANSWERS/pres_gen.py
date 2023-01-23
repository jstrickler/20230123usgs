#!/usr/bin/python

def pres_upper():
    with open('../DATA/presidents.txt') as pres_in:
        for line in pres_in:
            _, lname, fname, *_ = line.rstrip().split(':')

            yield '{} {}'.format(fname, lname).upper()

for p in pres_upper():
    print(p)
