
# Problem Link
# https://www.hackerearth.com/practice/algorithms/string-algorithm/basics-of-string-manipulation/practice-problems/algorithm/monk-teaches-palindrome/

test_case = int(input())

# reversing string function
def reverse_slicing(s):
    return s[::-1]

for _ in range(test_case):
    string = input()
    # if len(string) == 1
        # print YES ODD
    if len(string) == 1:
        print("YES ODD")
        continue
    # if (len/2) is even
    if not (len(string) % 2):
        if reverse_slicing(string) == string:
            # if yes the pring YES EVEN
            print("YES EVEN")
            # else print NO
        else:
            print("NO")
                
    # else:
    else:
        if reverse_slicing(string) == string:
            # if yes then print YES ODD
            print("YES ODD")
            # else print NO
        else:
            print("NO")
