import numpy as np

m1 = np.array(
    [[2, 4, 6],
     [10, 20, 30]]
)  # sample 2x3 array

m2 = np.array([[1, 15],
                [3, 25],
                [5, 35]])  # sample 3x2 array

print('m1 =>\n', m1)
print()

print('m2 =>\n', m2)
print()

print('m1 * 10 =>\n', m1 * 10)  # multiply every element of m1 times 10
print()

print('m1 @ m2 =>\n', m1 @ m2)  # matrix multiply m1 times m2 -- diagonal product
print()

