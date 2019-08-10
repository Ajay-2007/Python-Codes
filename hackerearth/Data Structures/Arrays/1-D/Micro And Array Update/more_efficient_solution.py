# Problem Link
# https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/micro-and-array-update/

def main():
    test_case = int(input())
    # time_arr = []
    while test_case:
        size_n, k = tuple(map(int, input().split()))
        arr_n = list(map(int, input().split()))
        # adding only elements which are less than k
        min_value = min(arr_n)
        time_value = 0
        if min_value >= k:
            # time_arr.append(time_value)
            print(0)
        else:
            while not (min_value == k):
                min_value = (-(~min_value))
                time_value = (-(~time_value))
            # time_arr.append(time_value)
            print(time_value)
        test_case -= 1

if __name__ == "__main__":
    main()
