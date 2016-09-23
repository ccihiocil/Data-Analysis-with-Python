##
## File: inclass-04c.py (STAT 3250)
## Topic: Introduction to Python (part 4c)
##

#### Operations on DataFrames

import numpy as np  # load NumPy
import pandas as pd  # load pandas
from pandas import Series, DataFrame

## Data alignment

# Define two sample Series
s1 = Series([-4, 2, 3, 5], index=['a', 'b', 'd', 'c'])
s1
s2 = Series([3, 7, -2], index=['b', 'c', 'e'])
s2

# Adding them:
s1 + s2  # The union of the indices is used
# NaN appear for any nonoverlapping index

# We get something similar for DataFrames
df1 = DataFrame(np.arange(1, 10).reshape((3, 3)),
                columns=['a', 'c', 'd'],
                index=['X', 'Y', 'Z'])
df1
df2 = DataFrame(np.arange(4, 12).reshape((2, 4)),
                columns=['a', 'c', 'e', 'd'],
                index=['X', 'Y'])
df2

# Adding them together:
df1 + df2
df1.add(df2)  # Same as df1+df2

# We can specify a value to replace any value
# missing from one (but not both!) of the data 
# frames.
df1.add(df2, fill_value=0)
df2.add(df1, fill_value=0)  # The same

## DataFrames and Series
s1 = Series([2, 4, 6], index=['a', 'c', 'd'])

# Subtraction is by row (called "broadcasting")
df1
s1
df1 - s1

s2 = Series([2, 4, 6], index=['a', 'c', 'e'])
df1 - s2
df1.sub(s2)  # The same

# We can also broadcast across columns
s3 = Series([2, 4, 6], index=['X', 'Y', 'Z'])
s3

# axis=0 forces addition across columns
df1.add(s3, axis=0)

## Sorting & Ranking
myvals = np.array([2, 5, 4, 9, 11, 12, 1, 7, 15, 3, 6, 14, 13, 8, 10])
df3 = DataFrame(myvals.reshape((3, 5)),
                columns=['a', 'c', 'e', 'd', 'b'],
                index=['Y', 'X', 'Z'])
df3

df3.sort_index(axis=0)  # Sort rows by index
df3.sort_index(axis=1)  # Sort by column

# Sort rows, in reverse order
df3.sort_index(axis=0, ascending=False)
# Sort columns, in reverse order
df3.sort_index(axis=1, ascending=False)

# Sort on column 'c'
df3.sort_index(by='c')

# Ranks
df3
df3.rank(axis=0)  # Entry rank by column
df3.rank(axis=1)  # Entry rank by row

# %%

#### In-class Assignment 4, Part C
##
## All calculations should be done in Python.
##

## C1. Use the DataFrame 'grades' defined below to
##     answer the following questions.

grades = pd.read_csv('samplegrades.csv', index_col='StudID')

##  (a) Sort the DataFrame 'grades' on the CourseAve
##      variable, then determine the mean course average
##      for the students with the top-20 averages.
##  (b) Determine the bottom-10 final exam scores for 
##      students in the MW200 section.
##  (c) Among the students in the top-20% for APDE,
##      determine the percentage that finished in the
##      top-20% for course average.
##      (The top-20% is the top 113 stduents.)
# %%
