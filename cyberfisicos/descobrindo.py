import socket
import sys
import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#s.setsockopt( socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
#s.bind(('127.0.0.1',0))

while True:
    ip = input('IP de destino: ')
    porta = int(input('Porta de destino: '))
    msg = 'DISCOVERY'
    try:
        s.sendto(msg.encode(), (ip, porta))
        s.setblocking(0)
        print('aguardando resposta')
        time.sleep(5)
        while True:
            data, addr = s.recvfrom(1024)
            print('DESCOBRI sensor {} em {}'.format( data.decode(),addr ) )

    except:
        print('não há mais respostas')
        s.setblocking(1)

s.close()