import numpy as np

r1 = np.arange(50)  # create range of ints from 0 to 49
print(r1)
print("size is", r1.size)  # size is 50
print()

r2 = np.arange(5, 101, 5)  # create range of ints from 5 to 100 counting by 5
print(r2)
print("size is", r2.size)
print()

r3 = np.arange(1.0, 5.0, .3333333)  # start, stop, and step may be floats
print(r3)
print("size is", r3.size)
print()

r4 = np.linspace(1.0, 2.0, 10)  # 10 equal steps between 1.0 and 2.0
print(r4)
print("size is", r4.size)
print()
