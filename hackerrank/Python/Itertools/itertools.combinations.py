# Problem Link
# https://www.hackerrank.com/challenges/itertools-combinations/problem?h_r%5B%5D%5B%5D

from itertools import combinations

string, k = tuple(map(str, input().split()))

k = int(k)
string = ''.join(sorted(string))

ans_list = []

for r in range(1, k+1):
    s = list(combinations(string, r))
    ans_list.append(s)

for each_list in ans_list:
    for comb in each_list:
        print(''.join(comb))
