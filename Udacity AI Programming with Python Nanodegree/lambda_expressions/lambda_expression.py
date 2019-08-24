# Lambda Expressions
numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]

def mean(num_list):
    return sum(num_list)/len(num_list)

# mean_lambda = [lambda num_list:sum(num_list)/len(num_list) for num_list in numbers ]
# print(mean_lambda)
averages = list(map(mean, numbers))
print(averages)

# using lambda expression
averages_lambda = list(map(lambda x: sum(x)/len(x), numbers))
print(averages_lambda)

###################################################################
# lambda_filter.py

cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

def short_cities(name):
    return len(name) < 10

short_cities = list(filter(short_cities, cities))
print(short_cities)

# using lambda expression
short_cities_lambda = list(filter(lambda x: len(x) < 10, cities))
print(short_cities_lambda)
