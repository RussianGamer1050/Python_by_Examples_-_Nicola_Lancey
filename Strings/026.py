word = (input("Please enter any word: ")).lower()
if word[0] == ('a' or 'e' or 'i' or 'o' or 'y' or 'u'):
    print(word+"way")
else:
    print(word[1:]+word[0]+"ay")
