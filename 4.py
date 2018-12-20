'''
    Escreva um programa em Python que leia um arquivo txt e apresente na tela o seu conteúdo reverso. Exemplo:

arquivo.txt

Bom dia

Você pode falar agora?

Resultado na tela:

?aroga ralaf edop êcoV

aid moB
'''
import os
def createFile():
    arq = open("exericio4.txt", "w")
    i = input("Entre com seu texto: B")
    arq.write(i)
    arq.close()

def readFile():
    arq = open("exericio4.txt", "r")
    for line in arq:
        print(line[::-1])
    arq.close()

def Main():
    print("")
    createFile()
    readFile()







if __name__ == '__main__':
    Main()