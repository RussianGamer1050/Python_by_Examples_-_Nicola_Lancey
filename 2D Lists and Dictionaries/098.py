list_2d = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
row = int(input("What row you would like displayed? "))
print(list_2d[row])
list_2d[row].append(int(input("Enter a new item: ")))
print(list_2d[row])
