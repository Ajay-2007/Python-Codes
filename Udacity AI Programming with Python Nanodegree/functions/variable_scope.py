# Variable Scope

# This will result in error
def some_function():
    word = 'hello'
#print(word)

# This works fine
def some_function_2():
    word = 'hello' # local variable limited to some_function_2() scope

def another_function():
    word = 'goodbye' # local variable limited to another_function() scope

word = 'hello'
def some_function_global():
    word = 'bye'
    print(word)
#print(word) # this represent that global value can't be modified if you want
# to modify that variable value inside this function, it should be passed
# in as argument to the function
some_function_global()

#####################################################
egg_count = 0

def buy_eggs():
    egg_count += 12 # purchase a dozen eggs

#buy_eggs() # this will result in UnboundLocalError

def buy_eggs_new(egg_count):
    egg_count += 12
    return egg_count

egg_count = buy_eggs_new(egg_count)
print(egg_count)
