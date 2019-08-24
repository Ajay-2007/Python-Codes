# number to find the factorial of
number = 6   

# start with our product equal to one
product = 1

# track the current number being multiplied
current = []

# write your while loop here
while number:
    product *= number
    current.append(number)
    number -= 1

    # multiply the product so far by the current number
    
    
    # increment current with each iteration until it reaches number
new_number = 6
new_current = 1
new_product = 1
while new_current <= new_number:
    new_product *= new_current
    new_current += 1


# print the factorial of number
#print(product)
#print(new_product)

# number to find the factorial of
number = 6   

# start with our product equal to one
product = 1

# write your for loop here
for i in range(2,number+1):
    product *= i
# print the factorial of number
print(product)
