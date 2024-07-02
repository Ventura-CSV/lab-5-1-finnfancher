def getinput():
    x = int(input("Input a value: "))
    return x


def getsum(v1, v2):
    return v1 + v2

def printval(v1, v2, total):
    print(v1, v2, total)


def main():
    userval1 = getinput()
    userval2 = getinput()
    total = getsum(userval1, userval2)
    printval(userval1, userval2, total)


if __name__ == '__main__':
    main()
