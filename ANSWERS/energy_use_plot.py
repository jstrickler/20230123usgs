#!/usr/bin/env python
"""

@author: jstrick
Created on Sat May 18 14:02:18 2013

"""
import pandas as pd
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt


col_names = ['Desc',"1960","1965","1970","1975","1980","1985","1990","1991",
    "1992","1993","1994","1995","1996","1997","1998","1999","2000",
    "2001","2002","2003","2004","2005","2006","2007","2008","2009",
    "2010","2011"
]

df = pd.read_csv(
    '../DATA/energy_use_quad.csv',
    names = col_names,
    
    )

# Transportation
x_values = [ float(f) for f in col_names[1:] ]

plt.xlabel('Year')
plt.ylabel('Gigawatts')

for row in 0, 2, 4:
    row_name = df.loc[row,'Desc']
    y_values = df.ix[row][1:].values
    plt.plot(x_values, y_values, label=row_name, lw=3)

plt.legend(loc='upper left')

# plt.savefig('energy_use.png')
plt.show()
