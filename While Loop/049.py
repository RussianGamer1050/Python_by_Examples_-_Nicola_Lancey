compnum = 50
num = int(input("Can you guess the number? "))
count = 1
while num != compnum:
    if num > 50:
        print("Too high")
    else:
        print("Too low")
    num = int(input("Enter another number: "))
    count += 1
print("Well done, you took", count, "attempts")
