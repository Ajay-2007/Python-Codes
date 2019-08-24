#f = open('some_file.txt', 'r')
#file_data = f.read()

#f.close()


file_2 = open('some_file_2.txt', 'w')
file_2_data = file_2.write('Hello World New')
file_2.close()


files = []
for i in range(10000):
    files.append(open('some_file_2.txt', 'r'))
    files[i]
    #files[i].close() # good practice the always the close the file
    # after reading from it
    print(i)

# Reading and writting
