# Problem Link
# https://www.hackerrank.com/challenges/iterables-and-iterators

from itertools import combinations

size_n = int(input())

string = list(map(str, input().split()))
string = ''.join(string)

k = int(input())

ans_list = list(combinations(string, k))

count = 0
for i in range(len(ans_list)):
    if 'a' in ans_list[i]:
        count += 1

print('%.4f'%(count/len(ans_list)))
