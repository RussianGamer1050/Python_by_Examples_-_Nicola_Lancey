from array import *
arr = array('i', [1, 5, 1, 8, 8])
for i in arr:
    print(i)
num = int(input("Please enter one of the numbers from the array: "))
if arr.count(num) == 1:
    print("It appears ones")
else:
    print("It appears",arr.count(num), "times")
