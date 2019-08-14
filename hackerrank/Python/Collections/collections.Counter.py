# Problem Link
# https://www.hackerrank.com/challenges/collections-counter

from collections import Counter


x = int(input())
shoe_size_list = list(map(int, input().split()))
no_of_cust = int(input())

s_price = []
for i in range(no_of_cust):
    a,b = tuple(map(int, input().split()))
    s_price.append([a,b])

price_dict = {}
for i in s_price:
    price_dict[i[0]] = []

for i in s_price:
    price_dict[i[0]].append(i[1])

no_of_size = Counter(shoe_size_list)

amount = 0

for key in price_dict:
    try:
        if key in no_of_size:
            for i in range(no_of_size[key]):
                amount += price_dict[key][i]
    except:
        continue

print(amount)

