import numpy as np

a1 = np.arange(15)  # create 1D array
print("a1 shape", a1.shape)  # get shape
print()

print(a1)
print()

a1.shape = 3, 5  # reshape to 3x5
print(a1)
print()

a1.shape = 5, 3  # reshape to 5x3
print(a1)
print()

print(a1.flatten())  # print array as 1D
print()

print(a1.transpose())  # print transposed array
print("------------------")

a2 = np.arange(40)  # create 1D array
a2.shape = 2, 5, 4  # reshape go 2x5x4

print(a2)
print()
