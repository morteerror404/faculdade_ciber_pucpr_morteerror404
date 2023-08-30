# 1. Acessar https://tinyurl.com/hashcripto23
# 2. Aceitar o convite no link (canto inferior esquerdo)

# Funções hash
import hashlib

# Hash Message Authentication Code
import hmac

import json

# OS lib

import os

"""
ITEM 1
Desenvolva um programa que implemente uma aplicaçao que possui 
duas funcionalidades: cadastrar e autenticar usuario.
Um usu ́ario possui os seguintes atributos:
• Nome (string de 4 caracteres)
• Senha (string de 4 caracteres)
Al ́em disso, o cadastro dos usu ́arios deve ser armazenado em um arquivo (TXT, CSV,
JSON ou XML). A aplicac ̧  ̃ao deve utilizar o algoritmo MD5 para realizar a func ̧  ̃ao hash para
armazenamento da senha.
"""


def carrega_usuarios() -> list:
    # Abro o arquivo 'usuarios.csv' no modo de leitura
    with open('usuarios.json', 'r') as arquivo:

        # Leio todas as linhas do arquivo 'usuarios.csv'
        linhas = json.loads(arquivo.read())
        hashlib.md5(linhas['senha'])
        
    return linhas['usuarios']

def salva_usuario(usuario: str, senha: str) -> None:
    # Carrego toda a minha base de usuários
    usuarios = carrega_usuarios()

    # Concatena novo usuário na base
    usuarios.append({'nome': usuario, 'senha': senha})

    # Converto para o formato do JSON esperado
    usuarios = {'usuarios': usuarios}

    # Abro o arquivo 'usuarios.csv' no modo de escrita
    with open('usuarios.json', 'w') as arquivo:

        # Converto os dados em dicionário para JSON
        dados = json.dumps(usuarios)

        # Salva no disco
        arquivo.write(dados)

def autenticar(usuario: str, senha: str) -> bool:
    usuarios = carrega_usuarios()

    for user in usuarios:
        if user['nome'] == usuario and user['senha'] == senha:
            return True

    return False

def cadastrar(usuario: str, senha: str) -> bool:
    usuarios = carrega_usuarios()

    existe = False
    for user in usuarios:
        if user['nome'] == usuario:
            existe = True
            break

    if existe:
        print(f"Usuário {usuario} já existe na base!")
        return False
    else:
        salva_usuario(usuario, senha)
        print(f'Usuário {usuario} cadastrado com sucesso!')
        return True
    
#-------------------------------------------------------------------------#

def limpa_tela():
    
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')



      
