

import numpy as np

sample_data = np.loadtxt(   # Read some sample data into an ndarray
    "../DATA/columns_of_numbers.txt",
    skiprows=1,
    dtype=int
)

sample_data  *= 100  # Modify the sample data (multiply every element by 100)

print(sample_data)

file_name = 'sampledata'

np.save(file_name, sample_data)  # Write entire array out to NumPy-format data file (adds .npy extension)

retrieved_data = np.load(file_name + '.npy')  # Retrieve data from saved file

print('-' * 60)
print(retrieved_data)

