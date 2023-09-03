import random
num = random.randint(1, 10)
guess = 0
while guess != num:
    guess = int(input("Please enter a number: "))
