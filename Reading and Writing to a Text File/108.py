names = open('Names.txt', 'a')
names.write(input("Please enter a new name: ") + "\n")
names.close()
names = open('Names.txt', 'r')
print(names.read())
names.close()