
# Problem Link
# https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/micro-and-array-update/
class Micro_And_Array_Update:
    def __init__(self, arr_n, k):
        self.arr_n = arr_n
        self.k = k
        # self.time_arr = []
        
    # functio to increase each element of an arr_n and increase time also
    # which was initially 0 and then check
    # each element with the value of k whether every one of them
    # are greater than or equal to k
        
        
    def micro_and_array_update(self):
        # if the elements of an arr_n are already greater than or
        # equal to k then print 0
        time_c = 0
        if self.check_greater_or_equal():
            #self.time_arr.append(time_c)
            return 0
        else:
            # else check each element of arr_n with k and 
            # increase arr_n[i] += 1 and time_c += 1
            # then finally append time_c to time list
            i = 0
            check = self.check_greater_or_equal()
            while not check:
                for i in range(len(self.arr_n)):
                    # adding 1 using bitmasking
                    self.arr_n[i] = (-(~self.arr_n[i]))
                time_c = (-(~time_c))
                check = self.check_greater_or_equal()
            #self.time_arr.append(time_c)
            return time_c
    
    # check whether elements of an arr_n are greater than 
    # or equal to k or not
    def check_greater_or_equal(self):
        count_check = 0
        for i in range(len(self.arr_n)):
            if self.arr_n[i] >= self.k:
                count_check = (-(~count_check))
            else:
                continue
        if not (count_check ^ len(self.arr_n)):
            return True
        else:
            return False


def main():
    test_case = int(input())
    time_arr1 = []
    while test_case:
        size_n, k = tuple(map(int, input().split()))
        arr_n = list(map(int, input().split()))
        m = Micro_And_Array_Update(arr_n, k)
        time_arr1.append(m.micro_and_array_update())
        test_case -= 1
    for i in time_arr1:
        print(i)
if __name__ == "__main__":
    main()
    
