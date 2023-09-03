invite = ['', '', '']
answ = 'y'
print("Enter the names of three people you want to invite to your party:")
for i in range(0, 3):
    invite[i] = input(str(i+1) + ': ')
while answ == 'y':
    answ = input("Do you want to add another person? (y/n) ")
    if answ == 'y':
        invite.append(input())
print("You have invited", len(invite), "people")
