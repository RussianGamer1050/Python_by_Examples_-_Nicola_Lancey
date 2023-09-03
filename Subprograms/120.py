from random import randint


def addition():
    num1 = randint(5, 20)
    num2 = randint(5, 20)
    answ1 = int(input(str(num1) + " + " + str(num2) + " = "))
    answ2 = num1 + num2
    return answ1, answ2


def subtraction():
    num1 = randint(25, 50)
    num2 = randint(1, 25)
    answ1 = int(input(str(num1) + " - " + str(num2) + " = "))
    answ2 = num1 - num2
    return answ1, answ2


def check(answ1, answ2):
    if answ1 == answ2:
        print("Correct")
    else:
        print("Incorrect, the answer is", answ2)


def main():
    print("1) Addition")
    print("2) Subtraction")
    choice = int(input("Enter 1 or 2: "))
    if choice == 1:
        answ1, answ2 = addition()
        check(answ1, answ2)
    elif choice == 2:
        answ1, answ2 = subtraction()
        check(answ1, answ2)
    else:
        print("Incorrect. Try again")


main()
