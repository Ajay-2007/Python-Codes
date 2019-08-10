"""Monk and Welcome Problem

Args: arrays(int)
    
Returns: array(int)

Algorithm:
    arr_c[i] = arr_a[i] + arr_b[i]

Problem Link: https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/monk-and-welcome-problem/
"""

class Monk_And_Welcom:
    def __init__(self, size_n, arr_a, arr_b):
        self.size_n = size_n
        self.arr_a = arr_a
        self.arr_b = arr_b
        self.arr_c = []
    
    def monk_and_welcom(self):
        
        for i in range(self.size_n):
            self.arr_c.append(self.arr_a[i] + self.arr_b[i])
        return self.arr_c

def main():        
    size_n = int(input())
    arr_a = list(map(int, input().split()))
    arr_b = list(map(int, input().split()))
    m = Monk_And_Welcom(size_n, arr_a, arr_b)
    c_arr = m.monk_and_welcom()
    for i in range(size_n):
        print(c_arr[i], end=' ')

if __name__ == "__main__":
    main()
