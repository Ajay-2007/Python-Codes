# Problem Link
# https://www.hackerrank.com/challenges/nested-list

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    
    students.sort(key = lambda kv: kv[1])
    t = students[0][1]
    second_less = []
    for i in range(len(students)):
        if students[i][1] > t:
            second_less.append(students[i])
    t = second_less[0][1]
    second_less.sort(key = lambda kv: kv[0])
    for i in range(len(second_less)):
        if second_less[i][1] == t:
            print(second_less[i][0])
