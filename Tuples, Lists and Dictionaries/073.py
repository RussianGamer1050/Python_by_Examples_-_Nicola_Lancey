foods = {}
print("Please enter four of your favorite foods:")
for i in range(1, 5):
    foods[i] = input(str(i) + ": ")
print(foods)
del foods[int(input("Which one you want to get rid of? "))]
print(sorted(foods.values()))
