manifest = [('bananas', 15),
            ('matteresses', 24),
            ('dog kennels', 42),
            ('machine', 120),
            ('cheese', 5)]
items = ['bananas', 'matteresses', 'dog kennels', 'machine', 'cheese']
weights = [15, 34, 42, 120, 5]

#print(list(zip(items, weights)))

for item, weight in zip(items, weights):
    print(item, weight)

items, weights = zip(*manifest)

print(items)
print(weights)

for i, item in zip(range(len(items)), items):
    print(i, item)

# built in function enumerate

for i, item in enumerate(items):
    print(i, item)
