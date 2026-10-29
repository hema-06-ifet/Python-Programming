print("\nSETS:")

cars = {"BMW", "Honda", "Audi", "Mercedes", "Toyota", "Ferrari", "Tesla"}

print("Approach #1 =", cars)
print("==========")
print("Approach #2")

for car in cars:
print("Car name = {}".format(car))

print("==========")

cars.add("Tata")
print("New cars set = {}".format(cars))

cars.discard("Mercedes")
print("discard() method = {}".format(cars))

print("\nDICTIONARY:")

Dict = {}

print("Empty Dictionary:")
print(Dict)

Dict[0] = "BRICKS"
Dict[2] = "CEMENT"
Dict[3] = "BLUE_PRINT"

print("\nDictionary after adding 3 elements:")
print(Dict)

Dict["Value_set"] = (2, 3, 4)

print("\nDictionary after adding 3 elements:")
print(Dict)

Dict[2] = "STEEL"

print("\nUpdated key value:")
print(Dict)

Dict[5] = {"Nested": {"1": "LIME", "2": "SAND"}}

print("\nAdding a Nested Key:")
print(Dict)
