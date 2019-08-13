# Enter your code here. Read input from STDIN. Print output to STDOUT
# Problem Link
# https://www.hackerrank.com/challenges/itertools-product/problem?isFullScreen=false


from itertools import product

A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = [A, B]
answer = list(product(*C))

for ans in answer:
    print(ans, end=' ')
