# Problem Link
# https://www.hackerearth.com/practice/algorithms/sorting/insertion-sort/practice-problems/algorithm/monk-and-nice-strings-3/

size_n = int(input())

arr = []
for _ in range(size_n):
    arr.append(input())
    
arr.insert(0, 0)

for i in range(1, len(arr)):
    count = 0
    for j in range(1, len(arr)):
        if j < i:
            if arr[j] < arr[i]:
                count += 1
    print(count)
    
