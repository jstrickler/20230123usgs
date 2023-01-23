import numpy as np

sample_data = np.loadtxt(   # Read in sample data
    "../DATA/columns_of_numbers.txt",
    skiprows=1,
    dtype=float
)

sample_data  /= 10  # Modify sample data

print(sample_data)
print("-" * 60)

file_name = 'sample.dat'

sample_data.tofile(file_name)  # Write data to file (binary, but not portable)

data = np.fromfile(file_name)  # Read binary data from file as one-dimensional array
data.shape = sample_data.shape  # Set shape to shape of original array

print(data)
