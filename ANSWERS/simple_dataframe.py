#!/usr/bin/env python
"""

@author: jstrick
Created on Sat Jun 15 02:48:07 2013

"""
from random import random
import numpy as np
import pandas as pd

cols = ['Test1', 'Test2', 'Test3', 'Test4', 'Test5', 'Test6' ]

raw_array = np.random.rand(5, 6)

df = pd.DataFrame(raw_array, columns=cols)

print(df)
print()

print(df[['Test3','Test5']])
print()

print(df * 3.6)
