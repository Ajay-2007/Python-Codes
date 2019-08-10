
# Problem Link
# https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/range-query-2/


n,q = tuple(map(int, input().split()))

arr = list(map(int, input().split()))

arr.insert(0, 0)

q_arr = [list(map(int, input().split())) for _ in range(q)]

for i in range(len(q_arr)):
    # if q_arr[i] is 0 L R then perform ODD, EVEN checking
    if not q_arr[i][0]:
        L = q_arr[i][1]
        R = q_arr[i][2]
        if arr[R] == 1:
            print("ODD")
        else:
            print("EVEN")
    
    # if q_arr[i] is 1 X then perform bit Flip operation on arr
    # at index X
    else:
        X = q_arr[i][1] # 2
        # Flip the arr[X] bit
        arr[X] = int(not arr[X])
