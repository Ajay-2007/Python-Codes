# Reading and Writing file quiz

# reading the integer amount of characters

with open('comelot.txt', 'r') as song:
    #song.write('We\'re the knights of the round table We dance whenever we\'re able')
    print(song.read(2))
    print(song.read(8))
    print(song.read())
