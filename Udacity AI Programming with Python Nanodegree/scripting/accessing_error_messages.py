# Accessing error messages

def division(x, y):
    try:
        return x // y
    except ZeroDivisionError as e:
        print("ZeroDivisionError occurred {}.".format(e))
        
division(5, 0)


def all_built_in_exception(x, y):
    try:
        return x // y
    except Exception as e:
        print("Exception occurred {}.".format(e))

all_built_in_exception(6, 0)
