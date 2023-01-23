import pandas as pd

columns = ['year', 'US', 'UK', 'CA', 'MX ']

df = pd.DataFrame(
    [
        ['1950', 157813000, 50616000, 13737000, 27737000],
        ['2015', 321225000, 60566000, 34419000, 119175000]
    ], columns=columns)  # create sample dataframe

print("Original:")
print(df, '\n')

melted = df.melt(
    id_vars=['year'],
    value_vars=['US', 'UK', 'CA', 'MX'],
    var_name='country', value_name='population'
)  # "melt" the dataframe into the other direction

print(melted)


# melted.sort_values(by='year', inplace=True)  # now we want to order by the 'word_name' column; note use of "inplace"
#
# print("Sorted:")
# print(melted, '\n')


