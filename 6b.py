```python
# Exercise 6(b): Check whether a string is a palindrome

def isPalindrome(s):
    return s == s[::-1]

s = input("Enter the string: ")
ans = isPalindrome(s)

if ans:
    print("The string is palindrome")
else:
    print("The string is not a palindrome")
```
