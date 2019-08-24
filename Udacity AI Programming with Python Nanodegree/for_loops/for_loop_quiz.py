names = ['Joey Tribbiani',
         'Monica Geller',
         'Chandler Bing',
         'Phoebe Buffay']

usernames = []

for name in names:
    usernames.append(name.replace(' ', '_').lower())

for username in usernames:
    print(username)

usernames2 = names

for index in range(len(usernames2)):
    usernames2[index] = usernames2[index].replace(' ', '_').lower()
    print(usernames2[index])
