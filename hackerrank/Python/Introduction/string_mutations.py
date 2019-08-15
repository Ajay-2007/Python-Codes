# Problem Link
# https://www.hackerrank.com/challenges/python-mutations

def mutate_string(string, position, character):
    return string[:position]+character+string[position+1:]
    # alternatively 
    # l = list(string)
    # l[position] = chracter
    # return ''.join(l)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
