# Party Planner

def party_planner(no_party_people, cookies):
    no_of_cookies = cookies // no_party_people
    left_cookies = cookies % no_party_people
    return no_of_cookies, left_cookies

while True:
    try:
        print(party_planner(10, 20))
        break
    except ZeroDivisionError:
        print("Please Input valid number")
    
# Udacity Solution

def party_planner(cookies, people):
    leftovers = None
    num_each = None

    try:
        num_each = cookies // people
        leftovers = cookies % people
    except ZeroDivisionError:
        print("Oops, you entered 0 people will be attending.")
        print("Please enter a good number of people for a party.")
    return (num_each, leftovers)


print(party_planner(6, 5))
