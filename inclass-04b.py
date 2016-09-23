##
## File: inclass-04b.py (STAT 3250)
## Topic: Introduction to Python (part 4b)
##

#### pandas DataFrames

import numpy as np  # load NumPy
import pandas as pd  # load pandas

## Reading in a CSV file

# index_col sets the index to the value of 'StudID'
# The file being read should be in the same directory as
# your source Python file.
grades = pd.read_csv('samplegrades.csv', index_col='StudID')
grades

grades.loc['AGEST', :]  # Record AGEST
grades.ix[['AGEST']]  # Same, but as a DataFrame

grades.Calc == 'B'  # True when Calc = B
grades.ix[grades.Calc == 'B']  # Rows with Calc = B
len(grades.ix[grades.Calc == 'B'])  # Number with Calc = B
(grades.Calc == 'B').sum()  # Number with Calc = B (also)

# Math SAT scores for students with Calc = B
grades.Math[grades.Calc == 'B']

# Mean Math SAT scores for all students with a score 
np.mean(grades.Math)

# Mean MATH SAT scores for students with Calc = B
np.mean(grades.Math[grades.Calc == 'B'])

# Final exam scores for students with Calc = AP5 and
# Math SAT > 700
grades.Final[(grades.Calc == 'AP5') & (grades.Math > 700)]

# How many are there?
((grades.Calc == 'AP5') & (grades.Math > 700)).sum()

# Their mean Final exam score?
np.mean(grades.Final[(grades.Calc == 'AP5') & (grades.Math > 700)])

# What about for the entire data set?
np.mean(grades.Final)

# How many students are missing SAT scores?
np.isnan(grades.Math).sum()

# Are any missing the prerequisite?
sum(grades.Calc == 'None')

# Which records are missing the prerequisite?
grades.ix[grades.Calc == 'None']

# What is the mean Final exam score for those missing the
# course prerequisite?
np.mean(grades.Final[grades.Calc == 'None'])

# The Final mean and sample standard deviation
# for all students
np.mean(grades.Final)
np.std(grades.Final, ddof=1)  # ddof=1 sets denom = n-1

# How many of each type of Calc prerequisite were there?
posscalcs = pd.unique(grades.Calc)  # Distinct values
for c in posscalcs:
    ct = sum(grades.Calc == c)
    print('Calc = ', c, ', Count = ', ct)

# %%

#### In-class Assignment 4, Part B
##
## All calculations should be done in Python.
##

## B1. Use the DataFrame 'grades' defined above to
##     answer the following questions.

##  (a) Compute the mean and sample standard deviation for 
##      both the Course Average and the SAT Writing score.
##  (b) Find the mean Final exam score for all females
##      in the class.
##  (c) Repeat (b), this time for all males in the TR930
##      section.
##  (d) Compute the mean Homework score for all 1st-years
##      and then for all 4th-years.
##  (e) Find the probability that a randomly selected 2nd-year
##      was in the MW200 section.
##      
# %%
