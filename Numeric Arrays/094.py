from array import *
arr = array('i', [1, 8, 105, 111, 1050])
for i in arr:
    print(i)
num = int(input("Please choose on of this numbers: "))
while not(num in arr):
    num = int(input("Try again: "))
print("This is in the position", arr.index(num))
