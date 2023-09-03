import csv


def addition():
    name = input("Enter a new name: ")
    salary = input("Enter a salary: ")
    s_file = open('Salaries.csv', 'w')
    s_file.write(name + ', ' + salary + '\n')
    s_file.close()


def view():
    s_file = csv.reader(open('Salaries.csv'))
    for row in s_file:
        print(row)


def main():
    again = True
    while again:
        print("1) Add to file")
        print("2) View all records")
        print("3) Quit program\n")
        choice = int(input("Enter a number of your selection: "))
        if choice == 1:
            addition()
        elif choice == 2:
            view()
        elif choice == 3:
            again = False
        else:
            print("Incorrect selection")
        print("\n")


main()
