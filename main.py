flavors = [
    "Banana",
    "Chocolate",
    "Lemon",
    "Pistachio",
    "Raspberry",
    "Strawberry",
    "Vanilla",
]

for i in range(len(flavors)):
    for j in range(i + 1, len(flavors)):  # Ensures unique pairs
        print(flavors[i] + ", " + flavors[j])
            


