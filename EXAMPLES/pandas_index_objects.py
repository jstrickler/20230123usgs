import pandas as pd
from printheader import print_header

index1 = pd.Index(['a', 'b', 'c'], name='letters')  # create some indexes
index2 = pd.Index(['b', 'a', 'c'])
index3 = pd.Index(['b', 'c', 'd'])
index4 = pd.Index(['red', 'blue', 'green'], name='colors')

print_header("index1, index2, index3", 70)  # display indexes
print(index1)
print(index2)
print(index3)
print()

print_header("index2 & index3", 70)
# these are the same
print(index2 & index3)  # get intersection of indexes
print(index2.intersection(index3))  # get intersection of indexes
print()

print_header("index2 | index3", 70)
# these are the same
print(index2 | index3)  # get union of indexes
print(index2.union(index3))
print()

print_header("index1.difference(index3)", 70)
print(index1.difference(index3))  # get difference of indexes
print()

print_header("Series([10,20,30], index=index1)", 70)
series1 = pd.Series([10, 20, 30], index=index1)  # use index with series (can also be used with dataframe)
print(series1)
print()

print_header("DataFrame([(1,2,3),(4,5,6),(7,8,9)], index=index1, columns=index4)", 70)
dataframe1 = pd.DataFrame([(1, 2, 3), (4, 5, 6), (7, 8, 9)], index=index1, columns=index4)
print(dataframe1)
print()

print_header("DataFrame([(1,2,3),(4,5,6),(7,8,9)], index=index4, columns=index1)", 70)
dataframe2 = pd.DataFrame([(1, 2, 3), (4, 5, 6), (7, 8, 9)], index=index4, columns=index1)
print(dataframe2)
print()
