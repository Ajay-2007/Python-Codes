tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

# if tokens[i].
for index in range(len(tokens)):
    str_len = int(len(tokens[index]) - 1)
    if tokens[index][0] == '<' and tokens[index][str_len] == '>':
        print("valid xml token")
        count += 1
    else:
        print("invalid xml token")
        
print(count)

# Udacity Solution
count = 0
for index in tokens:
    if index[0] == '<' and index[-1] == '>':
        count += 1
print(count)
