import os
import pickle
import socket


def GetFiles(dir):
    if os.path.exists(dir):
        return os.listdir(dir)
    else:
        return 'O diretório não existe.'


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host, port = (socket.gethostname(), 5000)

s.bind((host, port))
s.listen()
print(f"Listening to server %{host}, in port %{port}")

(socket_cliente, addr) = s.accept()
print("Conectado a:", str(addr))
# Recebe pedido do cliente:

msg = socket_cliente.recv(2048)  # Aqui eu recebo a mensagem codificada
mensagem = msg.decode('ascii')  # Aqui eu transformo em string para comparação

print(GetFiles(mensagem))
envio = pickle.dumps(GetFiles(mensagem))
socket_cliente.send(envio)
#    socket_cliente.close()
#    socket_servidor.close()
