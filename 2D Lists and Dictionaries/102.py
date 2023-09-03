people = {}
for i in range(0, 4):
    name = input("Please enter a name: ")
    age = input("Enter the age: ")
    size = input("Enter the shoe size: ")
    people[name] = {'Age': age, 'Shoe size': size}
name = input("Enter a name: ")
print(people[name])
