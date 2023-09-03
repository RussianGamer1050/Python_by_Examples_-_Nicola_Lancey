books = open('Books.csv', 'r')
n = 0
for row in books:
    print(str(n) + ". " + str(row))
    n += 1
