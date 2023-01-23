import pandas as pd
import numpy as np

URL = "https://en.wikipedia.org/wiki/AFI%27s_100_Years...100_Laughs"

df_list = pd.read_html(URL)

df  = df_list[1]
df.columns = 'rank title director year'.split()
print(df.head())
print('-' * 60)

movies_by_director = df_list[1].value_counts("director")

def afc_sort(director):
    return director.split()[-1]

for x, y in movies_by_director.iteritems():
    print(x, y)


# for director, count in sorted(movies_by_director.items(), key=afc_sort):
#     print(f"{director:30.30s} {count:2d}")

