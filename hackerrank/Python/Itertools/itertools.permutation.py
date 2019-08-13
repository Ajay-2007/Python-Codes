# Problem Link
# https://www.hackerrank.com/challenges/itertools-permutations/problem?h_r=next-challenge&h_v=zen&isFullScreen=false


from itertools import permutations


string, k = tuple(map(str, input().split()))
k = int(k)
string = sorted(string)
string = ''.join(string)
answer = list(permutations(string, k))


for ans in answer:
    print(''.join(ans))
