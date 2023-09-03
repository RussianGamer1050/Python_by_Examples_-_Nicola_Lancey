from array import *
arr = array('i', [])
while len(arr) < 5:
    num = int(input("Enter a number: "))
    if 10 < num < 20:
        arr.append(num)
    else:
        print("Out of range")
print("Thank you")
for i in arr:
    print(i)
