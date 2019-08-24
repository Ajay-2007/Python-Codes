lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]

def my_enumerate(iterable, start=0):
    # Implement your generator function here
    # i = 1
    while start <= len(iterable):
        yield start, iterable[start-1]
        start += 1

for i, lesson in my_enumerate(lessons, 1):
    print("Lesson {}: {}".format(i, lesson))

# Udacity Solution

def my_enumerate_1(iterable, start=0):
    count = start
    for element in iterable:
        yield count, element
        count += 1

for i, lesson in my_enumerate_1(lessons, 1):
    print("Lesson {}: {}".format(i, lesson))
