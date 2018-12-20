'''
Escreva um programa cliente e servidor sobre TCP em Python em que:

O cliente envia para o servidor o nome de um diretório e recebe a lista de arquivos (apenas arquivos) existente nele.
O servidor recebe a requisição do cliente, captura o nome dos arquivos no diretório em questão e envia a resposta ao cliente de volta.

'''
import pickle
import socket



def Print_Status(bytes, tam):
    kb = bytes/1024
    tam_bytes = tam/1024
    txt = 'Baixando... '
    txt = txt + '{:<.2f}'.format(kb) + ' KB '
    txt = txt + 'de ' + '{:<.2f}'.format(tam_bytes) + ' KB'
    print(txt)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 5000))
# Tenta se conectar ao servidor

choice = ''
while not choice == 's':
    choice = input('choice um diretório: ')
    # Envia a requisição:
    s.send(choice.encode('ascii'))
    # Recebe o tamanho do arquivo:
    msg = s.recv(65535)
    res = pickle.loads(msg)
    for i in res:
        print(i)
    choice = ''
    print("Digite 's' para sair")
    s.close()


