import numpy as np

a1 = np.r_[np.array([1, 2, 3]), 0, 0, np.array([4, 5, 6])]  # build array from a sequence of array-like things
print(a1)
print()

a2 = np.r_[-1:1:6j, [0] * 3, 5, 6]  # faux slice with complex step implements linspace
print(a2)
print()

a = np.array([[0, 1, 2], [3, 4, 5]])
a3 = np.r_['-1', a, a]
print("a3:", a3)
print()

a4 = np.r_['0,2', [1, 2, 3], [4, 5, 6]]
print(a4)
print()

a5 = np.r_['0,2,0', [1, 2, 3], [4, 5, 6]]
print(a5)
print()

a6 = np.r_['1,2,0', [1, 2, 3], [4, 5, 6]]
print(a6)
print()

m = np.r_['r', [1, 2, 3], [4, 5, 6]]
print(m)
print(type(m))
