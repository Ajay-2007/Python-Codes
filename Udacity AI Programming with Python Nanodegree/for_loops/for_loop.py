# For Loops

cities = ['new york city',
          'mountain view',
          'chicago',
          'los angeles']


for city in cities:
    print(city, end=",")
print("Done")

capitalized_cities = [] # empty list
for city in cities:
    capitalized_cities.append(city.title())

for city in capitalized_cities:
    print(city, end=',')

for index in range(len(cities)):
    cities[index] = cities[index].title()
print('')
for city in cities:
    print(city, end=',')
