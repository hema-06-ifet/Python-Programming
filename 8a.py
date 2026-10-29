```python
# Exercise 8(a): Exception handling - Divide by zero

a = int(input("Enter a = "))
b = int(input("Enter b = "))

try:
    c = (a + b) / (a - b)
except ZeroDivisionError:
    print("a/b result in 0")
else:
    print(c)
```
