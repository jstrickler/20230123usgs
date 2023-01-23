import numpy as np

a = np.array(
    [[70, 31, 21, 76, 19, 5, 54, 66],
     [23, 29, 71, 12, 27, 74, 65, 73],
     [11, 84, 7, 10, 31, 50, 11, 98],
     [25, 13, 43, 1, 31, 52, 41, 90],
     [75, 37, 11, 62, 35, 76, 38, 4]]
)  # sample data

print('a =>', a, '\n')

i = a > 50  # create Boolean mask
print('i (a > 50) =>', i, '\n')

print('a[i] =>', a[i], '\n')  # print elements of a that are > 50 using mask

print('a[a > 50] =>', a[a > 50], '\n')  # same, but without creating a separate mask

print('a[i].min(), a[i].max() =>', a[i].min(), a[i].max(), '\n')  # min and max values of result set with values less than 50

a[i] = 0  # set elements with value > 50 to 0
print('a =>', a, '\n')

print("a[a < 15] += 10")
a[a < 15] += 10  # add 10 to elements < 15
print(a, '\n')
