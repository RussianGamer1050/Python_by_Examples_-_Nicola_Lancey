from array import *
arr = array('f', [11.11, 18.18, 22.22, 66.66, 99.99])
num = int(input("Please enter a number between 2 and 5: "))
while 2 > num or 5 < num:
    num = int(input("Out of range. Try again: "))
for i in arr:
    print(round(i/num, 2))
