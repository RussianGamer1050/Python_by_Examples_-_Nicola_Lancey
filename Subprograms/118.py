def get_num():
    num = int(input("Please enter a number: "))
    return num


def num_count(num):
    for i in range(0, num):
        print(i + 1)


def main():
    num = get_num()
    num_count(num)


main()
