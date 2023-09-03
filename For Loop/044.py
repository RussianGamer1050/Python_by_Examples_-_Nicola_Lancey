num = int(input("How many people do you want to invite to your party? "))
if num < 10:
    for i in range(0, num):
        name = input("Enter a name: ")
        print(name, "has been invited")
else:
    print("Too many people")
