import socket, pickle, time

# Função que Print a list formatada
def Print(l):
    texto = ''
    for i in l:
        texto = texto + '{:>8.2f}'.format(i)
    print(texto)


try:
    udpClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    dest = (socket.gethostname(), 9991)

    for i in range(0, 5):
        udpClient.sendto(f'Pedido {i}'.encode('utf-8'), dest)
        print(f"Pedido {i}")
        (msg, host) = udpClient.recvfrom(1024)
        list = pickle.loads(msg)
        print('{:>8}'.format('Free') + '{:>8}'.format('Total'))
        print(list)
        time.sleep(5)


except Exception as error:
    print(error)




