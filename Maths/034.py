print("1) Square\n2) Triangle\n")
choice = input("Enter a number: ")
if choice == '1':
    length = int(input("Please enter the length of one side: "))
    print("The area of this square is", length**2)
elif choice == '2':
    base = int(input("Please enter the base: "))
    height = int(input("Enter the height of the triangle: "))
    print("The area of this triangle is", (base*height)/2)
else:
    print("You entered the wrong number")
