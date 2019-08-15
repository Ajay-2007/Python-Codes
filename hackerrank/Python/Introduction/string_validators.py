# Problem Link
# https://www.hackerrank.com/challenges/string-validators

import re

if __name__ == '__main__':
    s = input()
    print(bool(re.search(r'[a-zA-Z0-9]', s)))
    print(bool(re.search(r'[a-zA-Z]', s)))
    print(bool(re.search(r'[0-9]', s)))
    print(bool(re.search(r'[a-z]', s)))
    print(bool(re.search(r'[A-Z]', s)))
    # count = [0]*4
    # for i in s:
    #     if i.isalpha():
    #         count[0] += 1
    #     if i.isdigit():
    #         count[1] += 1
    #     if i.islower():
    #         count[2] += 1
    #     if i.isupper():
    #         count[3] += 1
    # if count[0]:print("True")
    # else:print("False")

    # if count[1]: print("True")
    # else: print("False")

    # if count[2]: print("True")
    # else : print("False")

    # if count[3]: print("True")
    # else: print("False")
