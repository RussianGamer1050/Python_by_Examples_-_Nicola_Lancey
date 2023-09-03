f_name = input("Please enter your first name: ")
if len(f_name) < 5:
    s_name = input("Please enter your surname: ")
    up = f_name+s_name
    print(up.upper())
else:
    print(f_name.lower())
