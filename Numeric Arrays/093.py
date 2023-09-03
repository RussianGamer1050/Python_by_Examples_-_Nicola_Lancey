from array import *
arr = array('i', [])
print("Please enter five numbers:")
for i in range(0, 5):
    arr.append(int(input(str(i+1) + ". ")))
for i in arr:
    print(i)
num = int(input("Choose one number: "))
if num in arr:
    arr.remove(num)
    arr_new = array('i', [num])
else:
    print("That is not a value in the array")
