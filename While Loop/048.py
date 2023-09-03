count = 0
y = 'y'
while y == 'y':
    name = input("Please enter the name of somebody you want to invite: ").title()
    print(name, "has been invited")
    count += 1
    y = input("Do you want to invite anybody else? (y/n) ")
print("You have invited", count, "people")
