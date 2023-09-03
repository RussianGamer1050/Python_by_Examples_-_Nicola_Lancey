nums = [105, 111, 666, 999]
for i in nums:
    print(i)
num = int(input("Please enter a three-digit number: "))
if num in nums:
    print(num, "is in position -", nums.index(num))
else:
    print("That is not in the list")
