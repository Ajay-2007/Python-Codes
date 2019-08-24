# Good and Bad Example

# Don't use True or False as conditions
# Bad Example
is_cold = True
wheather = True

if True:
    print("This indented code will always get run")

# Another bad example
if is_cold or (not is_cold):
    print("This indented code will always get run")

# Bad Example
if wheather == 'snow' or 'rain':
    print("wear boots")
    # This code is valid in python, but it is not a boolean
    # expression, although it reads like one


# Don't compare boolean variable with == True or == False
# This comparision is neccessary, since the boolean variable itself
# is a boolean expression

# bad example
if is_cold == True:
    print("The wheather is cold")
    # This is a valid condition, but we can make the code
    # more readable by using the variable itself as the
    # condition instead, as below
# Good Example
if is_cold:
    print("The Wheather is cold")

# if you want to check whether a boolean is False you can use
# a not operator
if not is_cold:
    print("The Wheather is not cold")

# Truth Testing
# truth testing example
errors = 3
if errors:
    print("you have {} errors to fix".format(errors))
else:
    print("No errors to fix")
    # This is a nice, succinct way of writting an if statement

#################################################################
