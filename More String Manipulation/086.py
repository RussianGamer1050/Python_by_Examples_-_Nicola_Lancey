password = input("Please enter a new password: ")
again = input("Enter it again: ")
if again == password:
    print("Thank you")
    true = False
elif password.lower() == again.lower():
    print("They must be in the same case")
else:
    print("Incorrect")
