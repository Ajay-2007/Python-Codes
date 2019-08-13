# Problem Link
# https://www.hackerrank.com/challenges/compress-the-string

from itertools import groupby


string = input()

ans_list = [(len(list(g)), int(k)) for k,g in groupby(string)]

for ans in ans_list:
    print(ans, end=' ')
