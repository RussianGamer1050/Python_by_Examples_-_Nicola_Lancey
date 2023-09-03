num = 10
while num != 0:
    print("There are", num, "green bottles hanging on the wall,\n" + str(num),
          "green bottles hanging on the wall,\nand if 1 green bottle should accidentally fall")
    answ = int(input("how many green bottles will be hanging on the wall? "))
    if answ == num-1:
        print("There will be", num - 1, "green bottles hanging on the wall")
    else:
        while answ != num-1:
            answ = int(input("No, try again: "))
    num -= 1
print("There are no more green bottles hanging on the wall")
