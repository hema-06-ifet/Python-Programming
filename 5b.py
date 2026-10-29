def max_num_in_list(numbers):
maximum = numbers[0]

```
for a in numbers:
    if a > maximum:
        maximum = a

return maximum
```

print(max_num_in_list([1, 2, -8, 0]))
