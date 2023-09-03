def add():
    names.append(input("Enter new name: "))
    return names


def change():
    cg = int(input("Which name you want to change: "))
    names[cg - 1] = input("Enter new name: ")
    return names


def delete():
    d = int(input("Which item you want to delete: "))
    del names[d - 1]


def view():
    count = 1
    for i in names:
        print(str(count) + ". " + i)
        count += 1


def main():
    ch = 0
    while ch != 5:
        print("1) Addition")
        print("2) Change")
        print("3) Delete")
        print("4) View the list")
        print("5) End the program")
        ch = int(input("Enter a number: "))
        print("\n")

        if ch == 1:
            add()
        elif ch == 2:
            change()
        elif ch == 3:
            delete()
        elif ch == 4:
            view()
        elif ch != 5:
            print("Wrong number")
        print("\n")


names = []
main()
