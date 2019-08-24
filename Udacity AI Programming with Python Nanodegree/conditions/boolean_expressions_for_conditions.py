# Complex Boolean Expressions

weight, height = 23, 45
is_raining, is_sunny = True, False
unsubscribed, location = False, "USA"

if 18.5 <= (weight / height**2) < 25:
    print("BMI is considered 'normal'")

if is_raining and is_sunny:
    print("Is there a rainbow")

if (not unsubscribed) and (location == 'USA' or location == 'CAN'):
    print("send mail")
