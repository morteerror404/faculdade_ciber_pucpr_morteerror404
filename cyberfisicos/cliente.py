import socket
import sys

HOST = '127.0.0.1'  # IP do servidor
PORT = 9999           # Porta do servidor

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((HOST, PORT))
except:
   print('# erro de conexao')
   sys.exit()

print('digite o texto a ser transmitido:')

while True:
    try:
        line = input("digite ENTER para transmitir")
        if not line:
            print('linha vazia encerra o programa')
            break
        
    except:
        print('programa abortado com CTRL+C')
        break

    data = bytes(line, 'utf-8')  # converte string para bytes
    tam = s.send(data)

    print('enviei ', tam, 'bytes')
    print(data)

