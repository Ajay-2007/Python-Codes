# Functions
# this prints something but does not return anything

def show_plus_ten(num):
    print(num + 10)

# this return something
def add_ten(num):
    return (num + 10)

print("Calling show_plus_ten...")
return_value_1 = show_plus_ten(5) # return value is None for this case
print("Done Calling")
print("This function returned : {}".format(return_value_1))

print("\nCalling add_ten...")
return_value_2 = add_ten(5)
print("Done Calling")
print("This function returned : {}".format(return_value_2))

##########################################################
def cylinder_volume(height, radius):
    pi = 3.14159
    return height * pi * (radius**2)

print(cylinder_volume(10, 5))

############

def default_argument_cylinder_volume(height, radius=5):
    pi = 3.14159
    return height * pi * (radius**2)

print(default_argument_cylinder_volume(10)) # pass in arugment with ommiting radius 
print(default_argument_cylinder_volume(10,7)) # pass in argument by position
print(default_argument_cylinder_volume(radius = 7, height = 10)) # pass in argument by name


##################################################################
# write your function here

def population_density(population, land_area):
    return population / land_area


# test cases for your function
test1 = population_density(10, 1)
expected_result1 = 10
print("expected result: {}, actual result: {}".format(expected_result1, test1))

test2 = population_density(864816, 121.4)
expected_result2 = 7123.6902801
print("expected result: {}, actual result: {}".format(expected_result2, test2))

###################################################################

# write your function here
def readable_timedelta(days):
    # use integer division to get the number of weeks
    """
    Calculate the number of weeks and remaining days for a given number of days.

    INPUT : int: number of days
    OUTPUT : str: returns a string containing number of weeks and remaining
    days for given days
    """
    weeks = days // 7
    # use % to get the number of days that remain
    remainder = days % 7
    #return "{} week(s) and {} day(s).".format(days//7, days - days//7 * 7)
    return '{} week(s) and {} day(s)'.format(weeks, remainder)
# test your function
print(readable_timedelta(10))
