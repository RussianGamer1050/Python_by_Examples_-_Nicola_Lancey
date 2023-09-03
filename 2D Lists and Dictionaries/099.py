list_2d = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
row = int(input("Please select a row: "))
print(list_2d[row])
column = int(input("Select a column: "))
print(list_2d[row][column])
answ = input("Do you want to change the value? (y/n) ")
if answ == 'y':
    new = int(input("Enter a new item: "))
    list_2d[row][column] = new
print(list_2d[row])
