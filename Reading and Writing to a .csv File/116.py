import csv

books = list(csv.reader(open("Books.csv")))
b_list = []
for row in books:
    b_list.append(row)

x = 0
for row in b_list:
    display = x, b_list[x]
    print(display)
    x = x + 1
remove = int(input("Delete: "))
del b_list[remove]

x = 0
for row in b_list:
    display = x, b_list[x]
    print(display)
    x = x + 1
change = int(input("Alter: "))
x = 0
for row in b_list[change]:
    display = x, b_list[change][x]
    print(display)
    x += 1
part = int(input("Part: "))
new = input("Data: ")
b_list[change][part] = new
print(b_list[change])

books = open("Books.csv", "w")
x = 0
for row in b_list:
    new = (b_list[x][0] + ", " + b_list[x][1] + ", " + b_list[x][2] + "\n")
    books.write(new)
    x += 1
books.close()
