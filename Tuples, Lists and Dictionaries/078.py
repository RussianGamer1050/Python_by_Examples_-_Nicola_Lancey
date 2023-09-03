tv = ['Sherlock', 'Black Mirror', 'Breaking Bad', 'News']
for i in tv:
    print(i)
show = input("Please enter another show: ")
pos = int(input("Enter the position for this show: "))
tv.insert(pos, show)
for i in tv:
    print(i)
