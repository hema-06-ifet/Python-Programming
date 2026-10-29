```python
# Exercise 7(b): Count the number of words in a file

number_of_words = 0

with open("INPUT.txt", "r") as file:
    data = file.read()
    words = data.split()
    number_of_words += len(words)

print(number_of_words)
```
