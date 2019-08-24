# names = [name for name in input().split(',')] # get and process input for a list of names
# assignments = [assignment for assignment in input(',')] # get and process input for a list of the number of assignments
# grades =  [grade for grade in input().split(',')]# get and process input for a list of grades
#
# # message string to be used for each student
# # HINT: use .format() with this string in your for loop
# message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
# submit before you can graduate. You're current grade is {} and can increase \
# to {} if you submit all assignments before the due date.\n\n"
#
# # write a for loop that iterates through each set of names, assignments, and grades to print each student's message
# for name, assignment, grade in zip(names, assignments, grades):
#     extra_credit = str(int(grade) + int(assignment)*2)
#     # print(name, assignment, grade, type(name), type(grade),type(assignment)
#     print(message.format(name, assignment, grade, extra_credit))
'''
INPUT : chandler bing, phoebe buffay, monica geller, ross geller
        3,6,0,2
        81, 77, 92, 88
'''
names = input("Enter names separated by commas: ").title().split(",")
assignments = input("Enter assignment counts separated by commas: ").split(",")
grades = input("Enter grades separated by commas: ").split(",")

message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

for name, assignment, grade in zip(names, assignments, grades):
    print(message.format(name, assignment, grade, int(grade) + int(assignment)*2))
