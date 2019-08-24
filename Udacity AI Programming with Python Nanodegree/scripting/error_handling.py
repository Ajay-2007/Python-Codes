while True:
    try:
       x = int(input('Enter a number: '))
       break
    except:
        print('That\'s not a valid number')
    finally:
        print('\nAttemptedInput\n')

################################################
# Specifying Exceptions
try:
    # some code
except ValueError:
    # some code

# Now it catches ValueError exceptions but not other exception. It we want this
# handler to address more than one type of exception, we can include a parenthesized
# tuple after the except with the exceptions

try:
    #some code
except (ValueError, KeyboardInterrupt):
    # some code

# If we want to execute different blocks of code depending on the exception, you can
# have multiple except blocks
try:
    # some code
except ValueError:
    # some code
except KeyboardInterrupt:
    # some code
finally:
    print("Enter correc number")
