from itertools import product

k, m = tuple(map(int, input().split()))

n = []
for i in range(k):
    s = list(map(int, input().split()))[1:]
    n.append(s)

all_product = list(product(*n))

def sqrt(iterable):
    temp = []
    for i in iterable:
        a = i % m
        temp.append((a*a)%m)
    return sum(temp)%m

# if k>1:
max_so_far = 0
max_value = 0
for it in all_product:
    max_value = sqrt(it)
    if max_value > max_so_far:
        max_so_far = max_value
print(max_so_far)
# else:
#     if len(n[0]) == 1:
#         print((n[0][0]**2)%m)
#     else:
#         max_so_far = 0
#         max_value = 0
#         for i in n[0]:
#             max_value = i**2 % m
#             if max_value > max_so_far:
#                 max_so_far = max_value
#         print(max_so_far)

