import pandas as pd


# columns:
# Name,Position Title,Department,Employee Annual Salary
df = pd.read_csv(
    "../DATA/city-of-chicago-salaries.csv"
)

print("Counts per department:")
print(df['Department'].value_counts(), '\n')

print('*' * 60)
print("WITHOUT CATEGORIES:")
print('*' * 60)

print(df.memory_usage(deep=True))
print()

print('*' * 60)
print("WITH CATEGORIES:")
print('*' * 60)

df = pd.read_csv(
    "../DATA/city-of-chicago-salaries.csv",
    dtype={"Position Title": "category", "Department": "category"}
)
print(df.memory_usage(deep=True))
print()
