import csv
books = open('Books.csv', 'a')
times = int(input("How many records you want to add to the list? "))
for i in range(0, times):
    new = input("Enter a new record: ")
    books.write(new + "\n")
books.close()
books = list(csv.reader(open('Books.csv')))
author = input("Enter an author: ")
count = 0
exist = False
for row in books:
    if author in str(row):
        print(row)
        exist = True
    count += 1
if exist == False:
    print("Where is no", author, "in this list")
