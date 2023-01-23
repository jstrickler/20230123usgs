import numpy as np
import sys

a = np.array(
    [[70, 31, 21, 76, 19, 5, 54, 66],
     [23, 29, 71, 12, 27, 74, 65, 73],
     [11, 84, 7, 10, 31, 50, 11, 98],
     [25, 13, 43, 1, 31, 52, 41, 90],
     [75, 37, 11, 62, 35, 76, 38, 4]],
    dtype=np.int16
)  #

print(a.size)
print(a.dtype)
print(a.itemsize)
print(a.nbytes)

data_list = [[70, 31, 21, 76, 19, 5, 54, 66],
 [23, 29, 71, 12, 27, 74, 65, 73],
 [11, 84, 7, 10, 31, 50, 11, 98],
 [25, 13, 43, 1, 31, 52, 41, 90],
 [75, 37, 11, 62, 35, 76, 38, 4]]

print("sys.getsizeof(data_list): {}".format(sys.getsizeof(data_list)))
