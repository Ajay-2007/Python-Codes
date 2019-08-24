# List Comprehensions
cities = ['new york city',
          'mountain view',
          'chicago',
          'los angeles']

capitalized_cities = []
for city in cities:
    capitalized_cities.append(city.title())

print(capitalized_cities)

# This can be reduced to one single line of code
capitalized_cities = [city.title() for city in cities]
print(capitalized_cities)

########################################################
names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

# write your list comprehension here

first_names = [name.split()[0].lower() for name in names]
print(first_names)

########################################################

# write your list comprehension here
multiples_3 = [x*3 for x in range(1, 21)]
print(multiples_3)

########################################################
'''
Use a list comprehension to create a list of names passed that only include those that scored at least 65.
'''
scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }

# write your list comprehension here
#passed = [name for name in scores if scores.get(name) >= 65]
# Udacity Solution
passed = [name for name, score in scores.items() if score >= 65]
print(passed)


