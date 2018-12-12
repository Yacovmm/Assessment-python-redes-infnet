'''
Escreva um programa em Python que leia dois arquivos, a.txt e b.txt, como a seguir:
a.txt
b.txt
1 15 -42 33 -7 -2 39 8

19 56 -43 23 -7 -11 33 21 61 9

Seu programa deve somar elemento por elemento de cada arquivo e imprimir o resultado na tela.
 Isto é, o primeiro elemento de a.txt deve ser somado ao primeiro elemento de b.txt, segundo elemento de a.txt
 deve ser somado ao segundo elemento de b.txt, e assim sucessivamente.
Caso um arquivo tenha mais elementos que o outro, os elementos que sobrarem do maior devem ser somados a zero.
'''


def Main():
    createFile("a.txt", "1 15 -42 33 -7 -2 39 8")
    createFile("b.txt", "19 56 -43 23 -7 -11 33 21 61 9")

    a = open('a.txt', 'r')
    b = open('b.txt', 'r')

    list_a = []
    list_b = []

    for i in a:
        number = i.split()
        for d in range(len(number)):
            list_a.append(int(number[d]))
    print("*" * 30)
    print("A.txt:  ", list_a)
    a.close()

    for i in b:
        number = i.split()

        for d in range(len(number)):
            list_b.append(int(number[d]))
    print("B.txt: ", list_b)
    print("*" * 30)
    b.close()

    Sum(list_a, list_b)


def createFile(fileName, content):
    try:
        arq = open(fileName, "w")
        i = content
        arq.write(i)
    finally:
        arq.close()


def ReadFiles(fileName):
    try:
        arq = open(fileName, "r")
        line = arq.readline()
        cnt = 1
        list = []
        while line:
            list.append(arq.readline().strip())
            line = arq.readline()
            cnt += 1
    finally:
        arq.close()
    return list


def Sum(a, b):
    if len(a) > len(b):
        while len(b) < len(a):
            b.append(0)
    else:
        while len(a) < len(b):
            a.append(0)

    for x in zip(a, b):
        print("Number:  {:<2} + {:<2} = {}".format(x[0], x[1], x[0] + x[1]))


if __name__ == '__main__':
    Main()
