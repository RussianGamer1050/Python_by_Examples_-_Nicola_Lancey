sub = ['Math', 'IT', 'Russian Language', 'English Language', 'Literature', 'Physics']
print(sub)
delete = sub.index(input("Which subject you don't like? "))
del sub[delete]
print(sub)
