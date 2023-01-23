import numpy as np

a = np.array(
    [[70, 31, 21, 76],
     [23, 29, 71, 12]]
)  # sample array

print('a =>\n', a)
print()

print("for row in a: =>")
for row in a:  # iterate over rows
    print("row:", row)
print()

print("for column in a.T:")
for column in a.T:  # iterate over columns by transposing the array
    print("column:", column)
print()

print("for elem in a.flat: =>")
for elem in a.flat:  # iterate over all elements (row-major)
    print("element:", elem)
