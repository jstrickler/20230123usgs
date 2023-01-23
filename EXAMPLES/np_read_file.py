import numpy as np

a = np.loadtxt(  # Function to read data into NumPy array
    '../DATA/columns_of_numbers.txt',
    usecols=[2, 5], # Only use the 3rd through 5th columns (0-based)
   skiprows=1,  # Skip the first row -- converting to float would fail because first row is character data
)

print(a)
print(a.shape)  # Print number of rows and columns
print(a.size)  # Print total number of elements in array

print(np.where(a < 30, a, 1000))  # Convert all values >= 30 to 1000

