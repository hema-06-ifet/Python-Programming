# Exercise 7(a): Copy content from one file to another

with open("INPUT.txt", "r") as scan:
    data = scan.read()

with open("OUTPUT.txt", "w") as output_file:
    output_file.write(data)

print("File copied successfully!")