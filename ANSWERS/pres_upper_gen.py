#!/usr/bin/python

with open('../DATA/presidents.txt') as pres_in:
    presidents = (line.upper().split(':')[1:3] for line in pres_in)

    pres_upper = ("{} {}".format(first, last) for last, first in presidents)

    for pres in pres_upper:
        print(pres)
