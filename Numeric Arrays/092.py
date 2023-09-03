from array import *
import random
arr_rand = array('i', [])
arr_user = array('i', [])
for i in range(0, 5):
    arr_rand.append(random.randint(-999, 999))
print("Please enter three numbers:")
for i in range(0, 3):
    arr_user.append(int(input(str(i+1) + ". ")))
arr_user.extend(arr_rand)
arr_user = sorted(arr_user)
for x in arr_user:
    print(x)
