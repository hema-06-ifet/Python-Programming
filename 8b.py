```python
# Exercise 8(b): Check voter eligibility

try:
    age = int(input("Enter your age: "))

    if age > 18:
        print("Eligible to vote")
    else:
        print("Not eligible to vote")

except ValueError:
    print("Age must be a valid number")
```
