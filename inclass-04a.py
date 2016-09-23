##
## File: inclass-04a.py (STAT 3250)
## Topic: Introduction to Python (part 4a)
##

#### pandas DataFrames

import numpy as np  # load NumPy
from pandas import DataFrame  # load DataFrame in

# local namespace

## Creating a DataFrame

data = {'Course': ['STAT 3A', 'STAT 3A', 'STAT 3A', 'STAT 3B', 'STAT 3B'],
        'Sect': [1, 2, 4, 1, 2],
        'Enroll': [41, 46, 39, 78, 84]}
df = DataFrame(data)
df

# The order of columns is alphabetical by default.
# Let's change it to move Sect next to Course.
df = DataFrame(data, columns=['Course', 'Sect', 'Enroll'])
df

# The index is set by default to 0, 1, 2, ...
# We can change it to statistics-friendly 1, 2, 3, ...
df = df.set_index([[1, 2, 3, 4, 5]])
df

# Add a new empty column 'GPA' to df1, and populate with NaN
df['GPA'] = np.nan  # np.nan = "NaN" (not a number)
df

# Change GPA for STAT 3A, Sect 2 to 4.0
df.loc[2, 'GPA'] = 4.0  # Row = 2, Column = 'GPA'
df

# Change everyone's GPA 
df['GPA'] = 4.0  # A's for everyone!
df

# Remove a column
del df['GPA']  # No one cares about GPA
df

# Add a column about class size
df['Large'] = df.Enroll > 50  # True when Enroll > 50
df

# Remove rows from a data frame
df.drop(2)  # Remove row indexed by 2
df.drop([2, 5])  # Remove rows indexed by 2 & 5
df  # df unchanged, use df = ... to change df

df.index  # List of indices
df.Sect == 1  # True when Sect = 1
df.index[df.Sect == 1]  # Indices for rows with Sect == 1
df.drop(df.index[df.Sect == 1])  # Drop rows with Sect == 1
df  # df unchanged, use df = ... to change df

from pandas import Series  # Load Series into namespace

# Generate a Series of class start times
time = Series(['10:00', '1:00', '9:30'], index=[1, 4, 5])

# Add the times to df with new column 'Time' that only
# provides information for indexed rows
df['Time'] = time
df

# Extracting subsets of a DataFrame
# Columns
df['Enroll']  # The column 'Enroll'
df.Enroll  # Also the column 'Enroll'
df[['Sect', 'Time']]  # The columns Sect, Time
df[[1, 3, 4]]  # The 2nd, 4th, and 5th columns

# Rows
df.ix[4]  # The row with index 4
df.ix[[2, 4, 5]]  # Rows indexed by 2,4,5
df.ix[df.Course == 'STAT 3B']  # Rows with Course='STAT 3B'

# Columns and Rows
df[['Enroll', 'Large']].ix[[1, 3]]  # Rows 1, 3
df[['Course', 'Time']].ix[1:3]  # Row 1-3
df[['Course', 'Sect']].ix[df.Enroll <= 40]  # Enroll <= 40
df  # df unchanged, use df = ... to change df

# %%

#### In-class Assignment 4, Part A
##
## All calculations should be done in Python.
##

## A1. Use the code below to define the DataFrame 'grades'

id = ['AAMUK', 'AAZKS', 'ADJLG', 'AGEST', 'AGUYS', 'AISLZ',
      'AJIZJ', 'ALRMJ', 'ANSGT', 'AOFJF', 'AOOBI', 'AORDW',
      'AOYQZ', 'APUYA', 'AQXCJ', 'ARILQ', 'ARYTS', 'ATDQL',
      'AUFRJ', 'AUOII', 'AURMM', 'AVTHH', 'AWDFQ', 'AWTQN']
hw = [197, 155.7, 172.2, 183.5, 166.9, 184.9, 199, 191, 186.8, 185.6,
      200, 199, 189.7, 199, 199, 193, 200, 195, 178.2, 187.1, 192.7,
      173.7, 197, 194.2]
midterm = [68, 72, 56, 52, 60, 72, 92, 72, 60, 72, 84, 72, 80, 52, 88,
           100, 88, 64, 84, 48, 60, 80, 72, 72]
final = [82.5, 67.5, 75, 70, 50, 65, 95, 65, 75, 80, 75, 72.5, 77.5,
         72.5, 85, 85, 72.5, 65, 65, 55, 55, 67.5, 75, 77.5]
data = {'ID': id, 'HW': hw, 'Midterm': midterm, 'Final': final}
grades = DataFrame(data, columns=['ID', 'HW', 'Midterm', 'Final'])
grades

##  (a) Compute the mean and standard deviation for each of
##      Homework, Midterm, and Final.
##  (b) Regard the data as a sample from a larger population.
##      Find a 95% confidence interval for each of Homework,
##      Midterm, and Final.  (Hint: The t* value for a
##      sample of size 24 is t* = 2.069.) 
##  (c) Add a new column to 'grades'called 'CA' (for 'course
##      average') using the weights Homework = 20%,
##      Midterm = 30%, and Final = 50%.  The course average
##      should be a percentage (max = 100).  (In the data,
##      the maximum Homework score is 200, and the maximum
##      for Midterm and Final is 100.) Put a print out of
##      the updated 'grades' in your answers.
##  (d) Add a new column to 'grades' called 'Grade' which is
##      a letter grade based on CA.  Use the grade scale from
##      inclass-2c.py. Put a print out of the updated 
##      'grades' in your answers. 
##      
# %%
