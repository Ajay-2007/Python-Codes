
# Challange Link
# https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/memorise-me/
# Write your code here

arr_size = int(input())
arr = list(map(int, input().split()))
q_size = int(input())
q_arr = [int(input()) for _ in range(q_size)]
count_arr = {}
arr_set = set(arr)
for i in range(len(q_arr)):
    count_arr[q_arr[i]] = 0
    
for i in range(len(arr)):
    try:
        if arr[i] in arr_set:
            count_arr[arr[i]] += 1
    except :
        continue

for i in q_arr:
    if count_arr[i] == 0:
        print("NOT PRESENT")
    else:
        print(count_arr[i])
