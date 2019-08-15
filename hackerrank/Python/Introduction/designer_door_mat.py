# Problem Link
# https://www.hackerrank.com/challenges/designer-door-mat

n,m  = map(int, input().split())
a = []
# print upper door
for i in range((n//2)):
    j = (2*i+1)
    a.append(j)
    print(('.|.'*j).center(m, '-'))
# print WELCOME in center
print("WELCOME".center(m, '-'))
a.sort(reverse=True)
# print lower door
for i in a:
    print(('.|.'*(i)).center(m, '-'))
