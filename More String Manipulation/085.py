count = 0
name = input("Please enter your name: ").lower()
vowels = ['a', 'e', 'i', 'o', 'y', 'u']
for i in name:
    if i in vowels:
        count += 1
print("Your name contains", count, "vowels")
