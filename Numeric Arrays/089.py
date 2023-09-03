from array import *
import random
arr = array('i', [])
for i in range(0, 5):
    arr.append(random.randint(-999, 999))
for x in arr:
    print(x)
