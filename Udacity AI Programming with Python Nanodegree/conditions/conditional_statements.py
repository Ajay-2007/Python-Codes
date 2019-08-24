# Conditional Statement

phone_balance = 8
bank_balance = 100

print(phone_balance, bank_balance)

if phone_balance < 5:
    phone_balance += 10
    bank_balance -= 10

print(phone_balance , bank_balance)

# If , elif and else
n = 4
if n%2 == 0:
    print("Number " + str(n) + " is even")
else:
    print("Number " + str(n) + " is odd")

season = "spring"

if season == 'spring':
    print('plant the garden')
elif season == 'summer':
    print('water the garden')
elif season == 'fall':
    print('harvest the garden')
elif season == 'winter':
    print('stay indoors')
else:
    print('unrecognized season')




# Third Example
age = 35

# Here are the age limits for bus fares
free_up_to_age = 4
child_up_to_age = 18
senior_from_age = 65

# these lines determines the bus fare prices

concession_ticket = 1.25
adult_ticket = 2.50

# here is the logic for bus fare prices
if age <= free_up_to_age:
    ticket_price = 0
elif age <= child_up_to_age:
    ticket_price = concession_ticket
elif age >= senior_from_age:
    ticket_price = concession_ticket
else:
    ticket_price = adult_ticket

print("Somebody who is {} years old will pay ${} to ride the bus".format(age, ticket_price))

###############################################################################
#which_prize.py

points = 174
if points <= 50:
    result = "Congratulations You won a wooden rabbit"
elif points <= 150:
    result = "Oh dear, no prize this time"
elif points <= 180:
    result = "Congratulations You won a wafer-thin mint"
else:
    result = "Congratulations You won a penguin"

print(result)
