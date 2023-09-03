num = int(input("Enter the number between 10 and 20: "))
while num < 10 or num > 20:
    if num < 10:
        print("Too low")
    else:
        print("Too high")
    num = int(input("Please try again: "))
print("Thank you")
