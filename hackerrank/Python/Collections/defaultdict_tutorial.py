# Problem Link
# https://www.hackerrank.com/challenges/defaultdict-tutorial

from collections import defaultdict

d = defaultdict(list)
size_a, size_b = tuple(map(int, input().split()))

for _ in range(size_a):
    d['A'].append(input())


for _ in range(size_b):
    d['B'].append(input())

d['A'].insert(0, 0)
d['B'].insert(0, 0)
c = defaultdict(lambda: defaultdict(list))

for word in d:
    for i in range(1, len(d[word])):
        c[word][d[word][i]].append(i)


for i in range(1, len(d['B'])):
    if d['B'][i] in c['A']:
        for j in c['A'][d['B'][i]]:
            print(j, end=' ')
        print()
    else:
        print(-1)
