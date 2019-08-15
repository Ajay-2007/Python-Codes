# Problem Link
# https://www.hackerrank.com/challenges/list-comprehensions/problem

from collections import defaultdict

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    ans_dict = defaultdict()
    for i, value in enumerate(arr):
        ans_dict[value] = i
    ans_list = list(ans_dict)
    ans_list.sort()
    print(ans_list[-2])
