# Problem Link
# https://www.hackerearth.com/practice/algorithms/sorting/merge-sort/practice-problems/algorithm/monk-and-modulo-based-sorting/


size_n, k = tuple(map(int, input().split()))

arr = list(map(int, input().split()))

new_arr = {}
for i in range(size_n):
    new_arr[i] = arr[i] % k

new_a = sorted(new_arr.items(), key = lambda kv:(kv[1], kv[0]))

for j in new_a:
    print(arr[j[0]], end=' ')
    
