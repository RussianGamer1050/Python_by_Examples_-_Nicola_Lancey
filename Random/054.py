import random
ch1 = random.choice(['heads', 'tails'])
ch2 = input("Heads or tails? (h/t) ")
if ch1[0:1] == ch2:
    print("You win")
else:
    print("Bad luck")
print("The computer has chosen", ch1)
