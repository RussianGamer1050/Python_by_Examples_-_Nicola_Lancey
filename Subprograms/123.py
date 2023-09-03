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


def delete():
    temp = csv.reader(open('Salaries.csv'))
    t_list = []
    for row in temp:
        t_list.append(row)
    d = int(input("Which row you want to delete? "))
    del t_list[d - 1]
    temp = open('Salaries.csv', 'w')
    for row in t_list:
        temp = row[0] + ', ' + row[1]
    temp.close()


def main():
    again = True
    while again:
        print("1) Add to file")
        print("2) View all records")
        print("3) Delete a record")
        print("4) Quit program\n")
        choice = int(input("Enter a number of your selection: "))
        if choice == 1:
            addition()
        elif choice == 2:
            view()
        elif choice == 3:
            delete()
        elif choice == 4:
            again = False
        else:
            print("Incorrect selection")
        print("\n")


main()
