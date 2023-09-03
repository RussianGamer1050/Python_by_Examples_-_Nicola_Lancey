print("1) Create a new file")
print("2) Display the file")
print("3) Add a new item to the file")
s = input("Make a selection 1, 2 or 3: ")
if s == '1':
    sub = open('Subject.txt', 'w')
    sub.write(input("Enter a school subject: ") + "\n")
    sub.close()
elif s == '2':
    sub = open('Subject.txt', 'r')
    print(sub.read())
    sub.close()
elif s == '3':
    sub = open('Subject.txt', 'a')
    sub.write(input("Enter a new subject: " + "\n"))
else:
    print("Please choose 1, 2 or 3")
