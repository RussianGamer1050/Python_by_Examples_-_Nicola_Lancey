total = int(input("Please enter the first number: "))
y = 'y'
while y == 'y':
    num = int(input("Enter another number: "))
    total += num
    y = input("Do you want to add another number? (y/n) ").lower()
print("The total is", total)
