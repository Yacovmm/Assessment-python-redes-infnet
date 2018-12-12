def Factorial(n):
    fat = n
    for i in range(n - 1, 1, -1):
        fat = fat * i
    return fat


def Main():
    print(Factorial(50))


if __name__ == '__main__':
    Main()
