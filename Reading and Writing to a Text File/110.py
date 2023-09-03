names = open('Names.txt', 'r')
print(names.read())
names.close()

names = open('Names.txt', 'r')
name = input("Please enter one of the names: ") + '\n'
for n in names:
    if n != name:
        names2 = open('Names2.txt', 'a')
        names2.write(n)
        names2.close()
names.close()
