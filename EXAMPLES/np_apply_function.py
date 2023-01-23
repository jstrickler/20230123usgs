#
import numpy as np

a = np.arange(1, 31) # create sample data
a.shape = 3, 10 # reshape into 5x20 array
print(a)

def spam(value): # define function that takes one parameter and returns twice its value
    return value ** 2

b = spam(a) # pass array to function; it is applied to every element
print(b)
