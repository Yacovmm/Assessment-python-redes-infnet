'''
Escreva um programa que obtenha um nome de um arquivo texto do usuário e crie um processo para
executar o programa do sistema Windows bloco de notas (notepad) para abrir o arquivo.
'''
import os


def Main():
    startFile(input("Entre como o nome do arquivo que deseja abrir: ") + ".txt")


def startFile(file):
    if not os.path.exists(file):
        createFile(str(file))
        os.startfile(file)
    os.startfile(file)

def createFile(fileName):
    try:
        arq = open(fileName, "w")
        arq.write(f"Nome do arquivo: ")
    finally:
        arq.close()


if __name__ == '__main__':
    Main()
