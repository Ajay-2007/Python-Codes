result = 0
basket_items = {'apples' : 4,
                'oranges' : 19,
                'kites' : 2,
                'sandwiches' : 8}

basket_items = {'pears': 5, 'grapes': 19, 'kites': 3,
                'sandwiches': 8, 'bananas': 4}

basket_items = {'peaches': 5, 'lettuce': 2, 'kites': 3,
                'sandwiches': 8, 'pears': 4}

basket_items = {'lettuce': 2, 'kites': 3, 'sandwiches': 8,
                'pears': 4,'bears': 10}

fruits = ['apples', 'oranges', 'pears',
          'peaches', 'grapes', 'bananas']

# Iterate through the dictionary
for fruit, no_of_fruit in basket_items.items():
    if fruit in fruits:
        result += no_of_fruit

print("There are {} fruits in the basket.".format(result))

fruit_count, not_fruit_count = 0, 0
basket_items = {'apples' : 4,
                'oranges' : 19,
                'kites' : 3,
                'sandwiches': 8}

fruits = ['apples', 'oranges', 'pears',
          'peaches', 'grapes', 'bananas']

for fruit, count in basket_items.items():
    if fruit in fruits:
        fruit_count += count
    else:
        not_fruit_count += count

print(fruit_count, not_fruit_count)
print("The number of fruits is {}. There are {} items that are not\
 fruits.".format(fruit_count, not_fruit_count))
