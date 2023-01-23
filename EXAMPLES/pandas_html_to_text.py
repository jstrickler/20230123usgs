import pandas as pd

df_list = pd.read_html('http://money.cnn.com/data/us_markets/', header=0)

df = df_list[0]

print(df.head())

df.to_csv('money.csv', sep="|")

