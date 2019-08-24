manifest = [('bananas', 15),
            ('matteresses', 24),
            ('dog kennels', 42),
            ('machine', 120),
            ('cheese', 5)]

# the code breaks the loop when weight exceeds or reaches the limit
print("Method 1")
weight = 0
items = []

for cargo_name, cargo_weight in manifest:
    print("current weight: {}".format(cargo_weight)) # this is for debugging purpose
    if weight >= 100:
        print("Breaking the loop now")
        break
    elif weight + cargo_weight > 100:
        print("Skipping {} ({})".format(cargo_name, cargo_weight))
        continue
    else:
        print("adding {} ({})".format(cargo_name, cargo_weight))
        items.append(cargo_name)
        weight += cargo_weight
        print(weight, end="*******\n")

print("\n Final weight {}".format(weight))
print("\n Final Items {}".format(items))
