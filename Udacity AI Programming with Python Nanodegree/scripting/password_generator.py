import random 

#word_list = []
word = []

with open('word_list.txt') as f:
    for line in f:
        word.append(line.split()[0])
def generate_password():
    # generate password from a word_list.txt
    password = ""
    for i in range(3):
        password += word[random.randint(0, len(word) - 1)]
        #print(password)
    return password

def main():
    print(generate_password())


if __name__ == '__main__':
    main()
# print(generate_password())

# Udacity solution
def generate_password_1():
    return random.choice(word) + random.choice(word) + random.choice(word)
print(generate_password_1())
        

def generate_password_2():
    return ''.join(random.sample(word, 3))

print(generate_password_2())
