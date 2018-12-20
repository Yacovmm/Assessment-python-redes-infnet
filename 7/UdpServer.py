''''
Escreva um programa cliente e servidor sobre UDP em Python que:
O cliente envia para o servidor o pedido de obtenção da quantidade total e disponível de memória no servidor e espera
 receber a resposta durante 5s. Caso passem os 5s, faça seu programa cliente tentar novamente mais 5 vezes
 (ainda esperando 5s a resposta) antes de desistir.
O servidor repetidamente recebe a requisição do cliente, captura a informação da quantidade total e d
isponível de memória há no servidor e envia a resposta ao cliente de volta.
'''
import pickle
import psutil
import socket


def toGB(v):
    return round(v / 1073741824, 2)


def Avalaible():
    return toGB(psutil.disk_usage(path='C:').free)

def Total():
    return toGB(psutil.disk_usage(path='C:').total)

resposta = ""
try:
    udpServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    dest = (socket.gethostname(), 9991)
    udpServer.bind(dest)

    for i in range(0, 5):
        (msg, host) = udpServer.recvfrom(1024)
        print(msg.decode())
        resposta = '{:>8}'.format(str(Avalaible())) + '{:>8}'.format(str(Total())) + "\n"
        bytes_resp = pickle.dumps(resposta)
        udpServer.sendto(bytes_resp, host)

except Exception as error:
    print(error)

udpServer.close()

