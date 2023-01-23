import numpy as np
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [20, 30, 40]]

a = np.array(data)  # create array from nested sequences
print(a, '\n')

print("a.ndim (# dimensions):", a.ndim)  # get number of dimensions
print("a.shape (lengths of axes/dimensions):", a.shape)  # get shape
print("a.size (number of elements in array):", a.size)
print("a.itemsize (size of one item):", a.itemsize)
print("a.nbytes (number of bytes used):", a.nbytes)

print()

a_zeros = np.zeros((3, 5), dtype=np.uint32)  # create array of specified shape and datatype, initialized to zeroes
print(a_zeros)
print()

a_ones = np.ones((2, 3, 4, 5))  # create array of specified shape, initialized to ones
print(a_ones)
print()

# with uninitialized values
a_empty = np.empty((3, 8))  # create uninitialized array of specified shape
print(a_empty)

print(a.dtype)  # defaults to float64

nan_array = np.full((5, 10), np.NaN)  # create array of NaN values
print(nan_array)

