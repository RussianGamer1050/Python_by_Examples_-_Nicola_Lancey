from random import randint


def val_range():
    low = int(input("Please enter a low number: "))
    high = int(input("Enter a high number: "))
    comp_num = randint(low, high)
    return comp_num


def instruction():
    print("I am thinking of a number...")
    num = int(input())
    return num


def answer(comp_num, num):
    while num != comp_num:
        if num < comp_num:
            print("Too low, try again:")
        else:
            print("Too high, try again:")
        num = int(input())
    print("Correct, you win")


def main():
    comp_num = val_range()
    num = instruction()
    answer(comp_num, num)


main()
