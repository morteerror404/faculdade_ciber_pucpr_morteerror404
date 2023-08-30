import socket
import RSALib as RSA
import AESLib as AES
from base64 import b64decode

ipServidor = '127.0.0.1'
portaServidor = 9999
destino = (ipServidor, portaServidor)

print('ESTA TELA PERTENCE A BOB')

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

s.sendto('HELLO'.encode(), destino )
   
print('Aguardando chave pública ...')


# 1) BOB RECEBE A CHAVE PÚBLICA DE ALICE
#   -- é preciso converter a chave de base64 para o objeto do Python
chavePubPEM, addr = s.recvfrom(1024) 
print('RECEBI uma chave pública')
chavePubObj2 = AES.decifraMensagem(chavePubPEM)

# 2) BOB GERA UMA CHAVE SECRETA ALEATÓRIA
chavesecreta, chavePEM = AES.geraChave(128)

# 3) BOB CRIPTOGRAFA A CHAVE SECRETA (EM BYTES) COM A CHAVE PÚBLICA DA ALICE
#  -- observe que nesse caso, a opção é text=False
AES.cifraMensagem(chavesecreta, chavePubObj2, text= True)

# 4) BOB ENVIA A CHAVE SECRETA CRIPTOGRAFADA PARA ALICE
#    -- é preciso trocar a string CHAVE SECRETA pela chave secreta criptografada em formato base64 (remova o encode())

s.sendto(RSA.converteChavePublica(chavesecreta), destino )

# 5) BOB DESCRIPTOGRAFA UMA MENSAGEM CIFRADA DA ALICE
# -- é preciso descriptografar o ciphertext e salvar em plain text!!!
ciphertext, addr = s.recvfrom(1024) 
print('RECEBI uma mensagem cifrada')

AES.decifraMensagem(ciphertext)

plaintext = 'EU NAO FIZ O EXERCICIO'

#------------------------------------------------
# SE VOCE FEZ TUDO CERTO A MENSAGEM DA ALICE VAI SER IMPRESSA AQUI
print(plaintext)




