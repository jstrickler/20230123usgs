import pandas as pd
from printheader import print_header

col_names = ["Desc", "1960", "1965", "1970", "1975", "1980", "1985", "1990",
             "1991", "1992", "1993", "1994", "1995", "1996", "1997", "1998",
             "1999", "2000", "2001", "2002", "2003", "2004", "2005", "2006",
             "2007", "2008", "2009", "(R) 2010", "2011"]  # column names (years)

df = pd.read_csv(  # read CSV file into dataframe
    '../DATA/energy_use_quad.csv',
    names=col_names,
    header=None,
    index_col="Desc",
)

print_header("database header")
print(df.head(), "\n")
print("-" * 60)

print_header("Only column 2003")
print(df[:]['2003'], "\n")  # print only the 2003 column
print("-" * 60)

print_header('Only row "Transportation as percent..."')
print(df.loc['Transportation as percent of total energy consumption'])
