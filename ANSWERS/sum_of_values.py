#!/usr/bin/env python
import operator
from functools import reduce

with open('../DATA/float_values.txt') as fv_in:
    sum = reduce(operator.add, map(float, fv_in))

print("{:.2f}".format(sum))

# or, for the truly functional experience:

print(reduce(operator.add, map(float, open('../DATA/float_values.txt'))))
