```python
# Exercise 10(a): Import a Dataset and Explore it Using Pandas

import pandas as pd
import numpy as np

data = {
    'animal': ['cat', 'cat', 'snake', 'dog', 'dog',
               'cat', 'snake', 'cat', 'dog', 'dog'],
    'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
    'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'priority': ['yes', 'yes', 'no', 'yes', 'no',
                 'no', 'no', 'yes', 'no', 'no']
}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(data, index=labels)

print("Dataset:")
print(df)

print("\nDataset Information:")
df.info()

print("\nFirst 3 Rows:")
print(df.head(3))

print("\nSelected Rows and Columns:")
print(df.loc[df.index[[3, 4, 8]], ['animal', 'age']])

print("\nVisits Greater Than 2:")
print(df['visits'] > 2)

print("\nRows with Missing Age:")
print(df[df['age'].isnull()])

print("\nCats with Age Less Than 3:")
print(df[(df['animal'] == 'cat') & (df['age'] < 3)])

print("\nAge Between 2 and 4:")
print(df[df['age'].between(2, 4)])

print("\nAverage Age of Each Animal:")
print(df.groupby('animal')['age'].mean())

print("\nAnimal Count:")
print(df['animal'].value_counts())

print("\nSorted Dataset:")
print(df.sort_values(by=['age', 'visits'],
                     ascending=[False, True]))
```
