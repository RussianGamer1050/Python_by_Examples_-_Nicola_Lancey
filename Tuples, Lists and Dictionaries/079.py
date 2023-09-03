nums = []
count = 0
while count < 3:
    num = int(input("Enter a number: "))
    nums.append(num)
    print(nums)
    count += 1
answ = input("Do you still want the last number tou entered saved? (y/n) ")
if answ == 'n':
    nums.remove(num)
print(nums)
