class Parrot:
    species = "bird"

    def __init__(self, name, age):
        self.name = name
        self.age = age
blu = Parrot("Blu", 9)
woh = Parrot("Woh", 12)

print("Blu is a {}".format(blu.species))
print("Woh is a {}".format(woh.species))

print(f"{blu.name} is {blu.age} years old.")
print(f"{woh.name} is {woh.age} years old.")