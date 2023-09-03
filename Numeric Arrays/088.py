from array import *
nums = array('i', [])
print("Please enter five numbers: ")
for i in range(0, 5):
    nums.append(int(input("Enter a number: ")))
nums = sorted(nums)
nums.reverse()
print(nums)
