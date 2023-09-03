import csv
start = int(input("Please enter a starting year: "))
end = int(input("Enter an end year: "))
books = list(csv.reader(open('Books.csv')))
tmp = []
for row in books:
    tmp.append(row)
x = 0
for row in books:
    if start <= int(tmp[x][2]) <= end:
        print(tmp[x][0])
    x += 1
