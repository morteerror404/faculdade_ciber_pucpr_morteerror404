import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    ip = input('Entre com o IP de destino: ')
    porta = int(input('Entre com a porta de destino: '))
    msg = input('Entre com a mensagem: ')
    s.sendto(msg.encode(), (ip, porta))


# s.close()
