# Problem Link
# https://www.hackerrank.com/challenges/itertools-combinations-with-replacement

from itertools import combinations_with_replacement

s, k = (map(str, input().split()))

s = ''.join(sorted(s))
k = int(k)
ans_list = list(combinations_with_replacement(s, k))

for ans in ans_list:
    print(''.join(ans))
