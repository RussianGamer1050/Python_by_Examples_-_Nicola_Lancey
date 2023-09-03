import random
colour = random.choice(['white', 'black', 'gray', 'red', 'blue'])
chosen = input("Please choice one colour (white, black, gray, red or blue): ").lower()
correct = False
while correct == False:
    if chosen == colour:
        print("Well done")
        correct = True
    else:
        if colour == 'blue':
            print("I think you are feeling blue now")
        elif colour == 'red':
            print("I bet you are red with angry")
        elif colour == 'gray':
            print("Are you feeling good? You are gray as a deadman")
        elif colour == 'black':
            print("I like black colour")
        elif colour == 'white':
            print("Are you scared? You are white as a sheet of paper")
        chosen = input("Please choose another colour: ")
