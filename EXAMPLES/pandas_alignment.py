import numpy as np
import pandas as pd
from printheader import print_header  # provided with lab files to make output easier to read

dataset1 = np.arange(9.).reshape((3, 3))  # create a numpy array

df1 = pd.DataFrame(  # create second Pandas dataframe from dataset, adding row and column numbers; note rows and columns do not quite match
    dataset1,
    columns=['apple', 'banana', 'mango'],
    index=['orange', 'purple', 'blue']
)

dataset2 = np.arange(12.).reshape((4, 3))  # create a numpy array

df2 = pd.DataFrame(  # create second Pandas dataframe from dataset, adding row and column numbers; note rows and columns do not quite match
    dataset2,
    columns=['apple', 'banana', 'kiwi'],
    index=['orange', 'purple', 'blue', 'brown']
)

print_header('df1')
print(df1)  # output dataframe
print()

print_header('df2')
print(df2)  # output dataframe
print()

print_header('df1 + df2')
print(df1 + df2)  # when dataframes are combined, if no match for row + column label, set value to NaN

print_header('df1.add(df2, fill_value=0)')
print(df1.add(df2, fill_value=0))  # same as #5, but where one dataframe has a value, set it to 0
