import random
score = 0
for i in range(0, 5):
    num1 = random.randint(1, 1000)
    num2 = random.randint(1, 1000)
    print(num1, "+", num2, "equals to...")
    answ = int(input())
    if answ == num1+num2:
        score += 1
print("You have got", score, "out of 5 points")
