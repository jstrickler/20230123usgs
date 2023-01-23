import numpy as np

a = np.array(
    [
        [5, 10, 15],
        [2, 4, 6],
        [3, 6, 9, ],
    ]
)  # create 2D array

b = np.array(
    [
        [10, 85, 92],
        [77, 16, 14],
        [19, 52, 23],
    ]
)  # create another 2D array
print("a")
print(a)
print()
print("b")
print(b)
print()

print("a * 10")
print(a * 10)  # multiply every element by 10 (not in place)
print()

print("a + b")
print(a + b)  # add every element of a to the corresponding element of b
print()

print("b + 3")
print(b + 3)  # add 3 to every element of b
print()

print("a.sum(): {}".format(a.sum()))
print("a.std(): {}".format(a.std()))
print("a.mean(): {}".format(a.mean()))
print("a.cumsum(): {}".format(a.cumsum()))
print("a.cumprod(): {}".format(a.cumprod()))

print()
a += 1000  # add 1000 to every element of a (in place)
print(a)
