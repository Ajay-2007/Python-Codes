

# Proble Link
# https://www.hackerearth.com/practice/data-structures/arrays/multi-dimensional/practice-problems/algorithm/monk-and-inversions-arrays-strings/

test_case = int(input())

def Remove(duplicate): 
    final_list = [] 
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list 

for _ in range(test_case):
    """Algorithm:
            no_of_inv = no of unordered pair of cells {(i,j),(p,q)}
                        such that M[i][j] > M[p][q] and i <= p and j <= q
    """
    size_n = int(input())
    M = [[j for j in map(int, input().split())] for i in range(size_n)]
    
    t = []
    p = [i for i in range(size_n)]
    q = [i for i in range(size_n)]
    
    for i in range(size_n):
        for j in range(size_n):
                t.append((i, j))
                t.append((j, i))
    
    t = Remove(t)
    answer_pair = []
    for i in range(size_n):
        for j in range(size_n):
            for pair in t:
                a, b = pair
                if (a >= i) and (b >= j):
                    if M[i][j] > M[a][b]:
                        answer_pair.append(pair)
                        
    if len(M) > 1:
        print(len(answer_pair))
    else:
        print(0)
