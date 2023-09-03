total = 0
for i in range(0, 5):
    num = int(input("Enter the number: "))
    incl = (input("Do you want to include this number? ")).lower()
    if incl == 'yes':
        total += num
print(total)
