import pandas as pd

df = pd.read_csv("../DATA/sales_records.csv")

df.info() # view original columns
print()

df["Total Revenue"] = df["Units Sold"] * df["Unit Price"]

df["Total Cost"] = df["Units Sold"] * df["Unit Cost"]

df["Total Profit"] = df["Total Revenue"] - df["Total Cost"]

print(df.info(), '\n')  # show added columns

print(df.iloc[1])  # one row, showing added columns with values
