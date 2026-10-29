```python
# Exercise 9(a): Implementing Pandas

import pandas as pd

df = pd.DataFrame({
    "Name": ["Mr. Owen Harris", "Mr. William Henry", "Miss. Elizabeth"],
    "Age": [22, 35, 58],
    "Sex": ["male", "male", "female"]
})

print(df)
print(df["Age"])

ages = pd.Series([22, 35, 58], name="Age")
print(ages)

print(ages.max())
print(df.describe())
```
