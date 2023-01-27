#!/usr/bin/env python
# coding: utf-8

# # Fun with Baby Names
# 
# This notebook explores baby name data provided by the US Census. 
# 
# It contains the percentages of all names of the top 2000 names for each year from 1880 to 2008. In other words, the percentage describes what percentage of people have that name in that year. |
# 
# The file has 285K records. Fields are __*year*__, __*name*__, __*percent*__, and __*sex*__.
# 
# Once the data have been imported (easy to do with Pandas), I'll create an interactive widget for graphing the popularity of a particular name over the time period. 
# 

# ## Import modules
# 
# We'll start by importing all the modules we'll need.

# In[1]:


# %load imports.py
import pandas as pd
import matplotlib.pyplot as plt
from ipywidgets import interact_manual, interact
import ipywidgets as widgets
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
sns.set()


# ## Read the data
# 
# Use __Pandas__ to read the data from the source CSV file. We don't need to add any options; Pandas can read a CSV file and assume the first line contains column names. We'll view the first 5 rows.
# 
# Note: Jupyter displays the value of the last line if it's an expression.

# In[2]:


df = pd.read_csv('../DATA/baby-names.csv')
df.head()


# In[55]:


df.describe()


# Let's count how many rows there are for the year. Apparently, we have the 2000 most popular names for each year from 1880 to 2008. 

# In[56]:


df.value_counts('year').sort_index()


# We'll calculate the total memory used by the dataframe with the `info()` method. 

# In[57]:


df.info(memory_usage="deep")


# ## Saving memory
# Currently the dataframe is using 34MB of memory. 
# 
# Let's take a look at the "Object" (string) columns. This time .describe() tells us how many distinct values there are per column. _Cardinality_ refers to the number of distinct values in a data set. _Low cardinality_ means that there are few distinct values. 

# In[58]:


df.describe(include='O')


# Let's read the data again, but this time, we'll mark the string columns as _categoricals_. This represents strings as very small integers, and saves a lot of memory. It is useful for columns with low cardinality.  For example, the 'sex' column only has two values, "boy" and "girl". Likewise, the 'name' field has relatively few values (6782/258000) for the number of rows. We can set the data type of these two columns as "category".

# In[59]:


df = pd.read_csv('../DATA/baby-names.csv', dtype={'sex': 'category', 'name': 'category'})


# And now we can see that memory usage has gone from about 34 MB to about 5 MB. 

# In[60]:


df.info(memory_usage="deep")


# Checking the dataframe, our data still looks the same. Categorical columns are presented with their original values. 

# In[61]:


df.head()


# ## Plotting name data
# 
# We can plot the popularity of a given name across all years. Pandas uses matplotlib behind the scenes to do the plotting. To get the data for plotting, we select all rows from the database with a specified name and sex. Then, we plot the 'year' column against the 'percent' column.
# 
# We can call `plt.savefig()` to save the plot as a file. The file type is inferred from the filename extension. 

# In[62]:


name = "Mary"
sex = "girl"
df_name = df[(df.name == name) & (df.sex == sex)]
df_name.plot('year', 'percent', xlabel='year', ylabel='percentage', title=name)
plt.savefig(name + ".png")


# ### Adding widgets
# To make it easy to plot different names, we can add some widgets to the plot. To do this, we'll use the __ipywidgets__ package, and import the __widgets__ module.
# 
# First we create a set of radio buttons, to make it easy to choose "boy" or "girl". 
# 
# Then we write a function to do the actual plot. The arguments to the function are __name__ and __sex__, corresponding to those columns in the dataframe. We use the _xlim_ and _ylim_ arguments to keep the X and Y scales the same for all plots. Otherwise the data will be scaled for each plot and high values will be difficult to tell from low values. 
# 
# To make our plot interactive, we call __interact_manual.options(manual_name="Plot")__ to create an interactive object. It will have a button to create the plot on demand. The "manual_name" argument is for the label on the button. 
# 
# When we call our interactive object, the first argument is the function to call when the button is pushed. The other arguments correspond to input widgets. The type of widget depends on what is passed. A string creates a text entry blank. As mentioned above, you can also create check boxes, radio buttons, and many other widgets. 
# 
# When the button is pressed, it copies the data from the input widgets and passes it to the function, which then plots the data.
# 
# NOTE: There are several variants of the __interact__ functionality.
# 
# 
# 
# 

# In[63]:


# define radio buttons for boy/girl
rb = widgets.RadioButtons(
    options=['boy', 'girl'], value = 'boy',
)


# In[64]:


y_min = df['percent'].min()
y_max = df['percent'].max()
x_min = df['year'].min()
x_max = df['year'].max()

def plot_name(name, sex):
    title = f"{name} ({sex})"
    df_name = df[(df.name == name) & (df.sex == sex)]
    df_name.plot('year', 'percent',
                 title = title, xlabel='year', ylabel='percentage', ylim=(y_min, y_max), xlim=(x_min, x_max))
    
im = interact_manual.options(manual_name="Plot")
im(plot_name, name="", sex=rb)


# ### FInding popular names
# To determine the most popular name in all years, we can find the row where the percent matches the maximum value for the *percent* column. Only one name and year matches. 

# In[65]:


df[df.percent == df.percent.max()]


# ### Finding unpopular names
# Likewise, we can find the names that are the least popular names across all years.

# In[93]:


df[df.percent == df.percent.min()].head(10)


# ## Name length trends
# We can look at the trend of name length. What is the average length of a name for each year? Let's group the dataset by year, then within each year we can calculate the length of the 'name' column. Then we can calculate the average, minimum, and maximum length of name for that year, by gender.
# 
# Turns out that over 130 or so years, the most names have varied from 2 to 11 characters long, with no significant changes in mean length. 

# In[67]:


dy = df.groupby("year")  # group the data by year
    
df_lengths = pd.DataFrame(
    (
        (
            year, 
            data['name'].str.len().min(),
            data['name'].str.len().max(),
            data['name'].str.len().mean(),
            data['name'].str.len().median(),
        ) for year, data in dy
    ), 
    columns=['year', 'min', 'max', 'mean', 'median']
)
df_lengths.head()


# In[ ]:





# In[68]:


plt.plot(df_lengths['year'], df_lengths['min'], label="shortest")
plt.plot(df_lengths['year'], df_lengths['mean'], label="mean")
plt.plot(df_lengths['year'], df_lengths['median'], label="median")
plt.plot(df_lengths['year'], df_lengths['max'], label="longest")
plt.legend(loc="upper center")
plt.ylim(1,16)


# Just for fun, we'll use Seaborn to plot the mean. Same result as previous graph.

# In[92]:


# sns plot functions return a FacetGrid instance, which we can use to configure the plot
fg = sns.relplot(x='year', y='mean', data=df_lengths, kind="line")
fg.set(ylim=(df_lengths['min'].min(), df_lengths['max'].max()))  # minimum min and maximum max :-)


# In[ ]:




