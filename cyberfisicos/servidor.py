import socket
import sys

HOST = '127.0.0.1'  # localhost = esta máquina
PORT = 9999           # portas abaixo de 1023 exigem permissão de root

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((HOST, PORT))
except:
   print('# erro de bind')
   sys.exit()

s.listen(5) # backlog

print('aguardando conexoes em ', PORT)
conn, addr = s.accept() #chamada bloqueante

print('recebi uma conexao de ', addr)

#--------------------------
# insira aqui o codigo para tratar uma conexao
#--------------------------

while True:
    print('aguardando conexoes em ', PORT)
    conn, addr = s.accept()  # chamada bloqueante

    print('recebi uma conexao de ', addr)

    client_ip, client_port = addr
    print('Endereço IP do cliente:', client_ip)
    print('Número da porta do cliente:', client_port)


    while True:
        # Receber dados do cliente (tamanho máximo de 1024 bytes)
        data = conn.recv(100024)
        print('recebi', len(data), 'bites')
        if not data:
            print('Cliente desconectado:', addr)
            break

        # Decodificar os dados recebidos (assumindo que o cliente envia strings UTF-8)
        command = data.decode('utf-8')

        # Lógica para executar o comando e enviar a resposta
        if command == "say":
            response = "ola"
        
        elif command == "exit":
        
            response = "encerrando"
            print('Cliente desconectado:', addr)
            conn.close()
        
        elif command == 'closesv':
            print('encerrando servidor:', addr)
            s.close()
        
        else:
            response = "Comando não reconhecido"
            
        conn.send(response.encode("utf-8"))

    



