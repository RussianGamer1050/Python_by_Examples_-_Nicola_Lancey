direction = input("Which direction do you want to count? (up/down) ").lower()
if direction == 'up':
    num = int(input("Please enter the top number: "))
    for i in range(1, num+1):
        print(i)
elif direction == 'down':
    num = int(input("Please enter the number below 20: "))
    for i in range(20, num-1, -1):
        print(i)
else:
    print("I don't understand")
