```python
# Exercise 10(b): Import a Dataset and Explore it Using NumPy

import numpy as np

L = list(range(10))

print("String Values:")
print([str(c) for c in L])

print("\nData Types:")
print([type(item) for item in L])

print("\nZeros Array:")
print(np.zeros(10, dtype='int'))

print("\nOnes Array:")
print(np.ones((3, 5), dtype=float))

print("\nFull Array:")
print(np.full((3, 5), 1.23))

print("\nArange:")
print(np.arange(0, 20, 2))

print("\nLinspace:")
print(np.linspace(0, 1, 5))

print("\nRandom Normal Array:")
print(np.random.normal(0, 1, (3, 3)))

print("\nIdentity Matrix:")
print(np.eye(3))

np.random.seed(0)

x1 = np.random.randint(10, size=6)
# One dimension

x2 = np.random.randint(10, size=(3, 4))
# Two dimensions

x3 = np.random.randint(10, size=(3, 4, 5))
# Three dimensions

print("\nx3 ndim:", x3.ndim)
print("x3 shape:", x3.shape)
print("x3 size:", x3.size)
```
