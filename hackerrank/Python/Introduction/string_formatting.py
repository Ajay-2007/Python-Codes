# Problem Link
# https://www.hackerrank.com/challenges/python-string-formatting

def print_formatted(number):
    # your code goes here
    width = len(bin(number)[2:])
    for i in range(1, number+1):
        for base in "doXb":
            print("{0:{width}{base}}".format(i, base=base, width=width), end=' ')
        print()

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
