## Creating a DataFrame
```python
data = {'Course': ['STAT 3A', 'STAT 3A', 'STAT 3A', 'STAT 3B', 'STAT 3B'],
        'Sect': [1, 2, 4, 1, 2],
        'Enroll': [41, 46, 39, 78, 84]}
df = DataFrame(data)
df
```
#### The order of columns is alphabetical by default.
#### Let's change it to move Sect next to Course.
```python
df = DataFrame(data, columns=['Course', 'Sect', 'Enroll'])
df
```
#### The index is set by default to 0, 1, 2, ...
#### We can change it to statistics-friendly 1, 2, 3, ...
```python
df = df.set_index([[1, 2, 3, 4, 5]])
df
```
#### Add a new empty column 'GPA' to df1, and populate with NaN
```python
df['GPA'] = np.nan  # np.nan = "NaN" (not a number)
df
```
#### Change GPA for STAT 3A, Sect 2 to 4.0
```python
df.loc[2, 'GPA'] = 4.0  # Row = 2, Column = 'GPA'
df
```
#### Change everyone's GPA
```python
df['GPA'] = 4.0  # A's for everyone!
df
```
#### Remove a column
```python
del df['GPA']  # No one cares about GPA
df
```
#### Add a column about class size
```python
df['Large'] = df.Enroll > 50  # True when Enroll > 50
df
```
#### Remove rows from a data frame
```python
df.drop(2)  # Remove row indexed by 2
df.drop([2, 5])  # Remove rows indexed by 2 & 5
df  # df unchanged, use df = ... to change df
```
```python
df.index  # List of indices
df.Sect == 1  # True when Sect = 1
df.index[df.Sect == 1]  # Indices for rows with Sect == 1
df.drop(df.index[df.Sect == 1])  # Drop rows with Sect == 1
df  # df unchanged, use df = ... to change df
```
```python
from pandas import Series  # Load Series into namespace
```
#### Generate a Series of class start times
```python
time = Series(['10:00', '1:00', '9:30'], index=[1, 4, 5])
```
#### Add the times to df with new column 'Time' that only
#### provides information for indexed rows
```python
df['Time'] = time
df
```
#### Extracting subsets of a DataFrame
#### Columns
```python
df['Enroll']  # The column 'Enroll'
df.Enroll  # Also the column 'Enroll'
df[['Sect', 'Time']]  # The columns Sect, Time
df[[1, 3, 4]]  # The 2nd, 4th, and 5th columns
```
#### Rows
```python
df.ix[4]  # The row with index 4
df.ix[[2, 4, 5]]  # Rows indexed by 2,4,5
df.ix[df.Course == 'STAT 3B']  # Rows with Course='STAT 3B'
```
#### Columns and Rows
```python
df[['Enroll', 'Large']].ix[[1, 3]]  # Rows 1, 3
df[['Course', 'Time']].ix[1:3]  # Row 1-3
df[['Course', 'Sect']].ix[df.Enroll <= 40]  # Enroll <= 40
df  # df unchanged, use df = ... to change df
```