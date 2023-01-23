from sys import getsizeof
from array import array
from random import randint

values = [randint(1, 30000) for i in range(1000)]  # Create 1000 random values

print(f'Size of integer list: {getsizeof(values)}\n')

for datatype in 'i', 'h', 'L', 'Q', 'd':
    data_array = array(datatype, values)  # Create array object from values with various datatypes
    print(f'Size of {datatype} array: {getsizeof(data_array)}  Contents:',
          data_array[:5], '...')  # Print size of array (will vary based on datatype)
    print()
