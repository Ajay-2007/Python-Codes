#!/bin/python3
# Problem Link
# https://www.hackerrank.com/challenges/kangaroo/problem?h_r=next-challenge&h_v=zen

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    if x2 > x1 and v2 > v1:
        return "NO"
    else:
        i = 1
        for i in range(1, 10000):
            if not (x1 + v1 * i) - (x2 + v2*i):
                return "YES"
                break
            else:
                continue
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
