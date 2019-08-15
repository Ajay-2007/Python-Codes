# Problem Link
# https://www.hackerrank.com/challenges/np-concatenate

import numpy as np

n,m,p = map(int, input().split())

np_matrix = []
mp_matrix = []
for _ in range(n):
    np_matrix.append(list(map(int, input().split())))

for _ in range(m):
    mp_matrix.append(list(map(int, input().split())))

print(np.concatenate((np_matrix, mp_matrix), axis = 0))
