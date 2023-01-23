#!/usr/bin/env python
"""

@author: jstrick
Created on Sat Jun 15 02:34:14 2013

"""
import numpy as np

a = np.arange(35)

print(a)
print()

a.shape = (5, 7)

print(a)
print()

a.shape = (7, 5)

print(a)
print()