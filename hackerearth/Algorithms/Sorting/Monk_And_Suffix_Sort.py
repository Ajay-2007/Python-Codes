# Problem Link
# https://www.hackerearth.com/problem/algorithm/monk-and-suffix-sort/

string, k = tuple(map(str, input().split()))

lexi = {}
k = int(k)
temp_str = list(string)
temp_str.insert(0, '0')
string = ''.join(temp_str)

for i in range(1, len(string)):
    lexi[i] = string[i:]

lexi_sorted = sorted(lexi.items(), key = lambda kv: (kv[1], kv[0]))

lexi_sorted.insert(0, (0, '0'))
dit = {}
for i in range(len(lexi_sorted)):
    dit[i] = lexi_sorted[i]

print(dit[k][1])
