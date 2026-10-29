print("\nLISTS:")

materials = ["cementbags", "bricks", "sand", "Steelbars", "Paint"]

materials.append("Tiles")
materials.insert(3, "Aggregates")
materials.remove("sand")
materials[5] = "electrical"

print(materials)

print("\nTUPLES:")

materials = ("cementbags", "bricks", "sand", "Steelbars", "Paint")

print(materials)
print("list of element is=", materials)
print("materials[0]:", materials[0])
print("materials[1:3]:", materials[1:3])
