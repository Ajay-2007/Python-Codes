# Problem Link
# https://www.hackerearth.com/practice/algorithms/string-algorithm/string-searching/practice-problems/algorithm/little-monk-and-good-string/

string = input()

curr_length = 0
max_length_so_far = 0

for i in range(len(string)):
    str_char = string[i]
    if str_char is 'a' or str_char is 'e' or str_char is 'i' or str_char is 'o' or str_char is 'u':
        curr_length += 1
    else:
        curr_length = 0
    
    if curr_length > max_length_so_far:
        max_length_so_far = curr_length

print(max_length_so_far)
