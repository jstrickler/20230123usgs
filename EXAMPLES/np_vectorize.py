import time
import numpy as np

sample_data = np.loadtxt(   # Create some sample data
    "../DATA/columns_of_numbers.txt",
    skiprows=1,
)

def set_default(value, limit, default): # Define function with more than one parameter
    if value > limit:
        value = default

    return value

MAX_VALUE = 50      # Define max value
DEFAULT_VALUE = -1  # Define default value

print("Version 1: looping over arrays")
start = time.time() # Get the current time as Unix timestamp (large integer)
try:
    version1_array = np.zeros(sample_data.shape, dtype=int)  # Create array to hold results
    for i, row in enumerate(sample_data):  # Iterate over rows and columns of input array
        for j, column in enumerate(row):
            version1_array[i, j] = set_default(sample_data[i, j], MAX_VALUE, DEFAULT_VALUE)   # Call function and put result in new array
except ValueError as err:
    print("Function failed:", err)
else:
    end = time.time()  # Get current time
    elapsed = end - start  # Get elapsed number of seconds and print them out
    print(version1_array)
    print("took {:.5f} seconds".format(elapsed))
finally:
    print()


print("Version 2: broadcast without vectorize()")
start = time.time()
try:
    print("Without sp.vectorize:")
    version2_array = set_default(sample_data, MAX_VALUE, DEFAULT_VALUE) # Pass array to function; it fails because it has more than one parameter
except ValueError as err:
    print("Function failed:", err)
else:
    end = time.time()
    elapsed = end - start
    print(version2_array)
    print("took {:.5f} seconds".format(elapsed))
finally:
    print()

print("Version 3: broadcast with vectorize()")
set_default_vect = np.vectorize(set_default)  # Convert function to vectorized version -- creates function that takes one parameter and has the other two "embedded" in it

start = time.time()
try:
    print("With sp.vectorize:")
    version3_array = set_default_vect(sample_data, MAX_VALUE, DEFAULT_VALUE) # Call vectorized version with same parameters
except ValueError as err:
    print("Function failed:", err)
else:
    end = time.time()
    elapsed = end - start
    print(version3_array)
    print("took {:.5f} seconds".format(elapsed))
finally:
    print()
