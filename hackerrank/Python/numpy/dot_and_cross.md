<details><summary>Question</summary>
<p>
dot

The dot tool returns the dot product of two arrays.

import numpy

A = numpy.array([ 1, 2 ])
B = numpy.array([ 3, 4 ])

print numpy.dot(A, B)       #Output : 11
cross

The cross tool returns the cross product of two arrays.

import numpy

A = numpy.array([ 1, 2 ])
B = numpy.array([ 3, 4 ])

print numpy.cross(A, B)     #Output : -2
Task

You are given two arrays  and . Both have dimensions of X.
Your task is to compute their matrix product.

Input Format

The first line contains the integer .
The next  lines contains  space separated integers of array .
The following  lines contains  space separated integers of array .

Output Format

Print the matrix multiplication of  and .

Sample Input

2
1 2
3 4
1 2
3 4
Sample Output

[[ 7 10]
 [15 22]]
</p>
</details>

[Question Link](https://www.hackerrank.com/challenges/np-dot-and-cross "https://www.hackerrank.com/challenges/np-dot-and-cross")
```python
import numpy as np

n = int(input())

a = []
for _ in range(n):
    a.append(list(map(int, input().split())))
b = []
for _ in range(n):
    b.append(list(map(int, input().split())))

# a = np.array(a)
# b = np.array(b)
# b = np.matrix.transpose(b)
# ans = []
# for i in a:
#     for j in b:
#         ans.append(np.dot(i, j))


# print(np.reshape(ans, (n, n)))
print(np.dot(a, b))
```
