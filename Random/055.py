import random
num = random.randint(1, 5)
guess = int(input("Enter a number between 1 and 5: "))
if num == guess:
    print("Well done")
else:
    if guess > num:
        print("Too high")
    else:
        print("Too low")
    guess = int(input("Enter a second number: "))
    if num == guess:
        print("Correct")
    else:
        print("You lose")
