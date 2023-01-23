import pandas as pd

df = pd.read_excel('http://qrc.depaul.edu/Excel_Files/Presidents.xlsx', sheet_name='Master',
                  na_values='NA()')
df.index = range(1,len(df)+1)

# print(df.head())
parties = df['Political Party'].value_counts()
print(parties)
# parties.plot(kind='bar')
