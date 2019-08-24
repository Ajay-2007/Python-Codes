start_num = 5#provide some start number
end_num = 40#provide some end number that you stop when you hit
count_by = 2 #provide some number to count by 

if start_num > end_num:
    result = "Oops Looks like you start value is greater than \
the end value. Please try again"
else:
    break_num = start_num
    while break_num < end_num:
        break_num += count_by
        print(break_num)
    result = break_num

print(result)
