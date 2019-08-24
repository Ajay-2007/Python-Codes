# Reading and Writting file using with keyword

with open('my_path/my_file.txt', 'r') as f:
    file_data = f.read()

# after reading the file using with, it will automatically close it after
# reading the file as f 
