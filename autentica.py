import hashlib

from pathlib import Path
from getpass import getpass

ABSOLUTO = Path(__file__).parent.resolve()
ARQUIVO_USUARIOS = ABSOLUTO / Path('contas.txt')
ARQUIVO_BLOQUEADOS = ABSOLUTO / Path('bloqueados.txt')

def mostra_info():
    print("Bem vindo!")
    print("-=-=-=-=-=-=-=-=-=-=-=-=")
    print("Digite uma opção para começar:")
    print("  1. Cadastrar")
    print("  2. Autenticar")
    print("  3. Sair")
    print("-=-=-=-=-=-=-=-=-=-=-=-=")

def carrega_dados(nome_arquivo):
    p = Path(nome_arquivo)

    # Cria arquivo se ele não existir
    if not p.exists():
        p.touch()

    with p.open('r') as fp:
        linhas = fp.readlines()
    
    if not linhas:
        return[]    
        
    # Remove quebras de linha
    linhas = [l.strip() for l in linhas]

    # Separa em [usuario, senha]
    linhas = [tuple(l.split(',')) for l in linhas]

    return linhas

def aplica_hash(texto, funcao):
    return funcao(texto.encode('utf8')).hexdigest()

def escreve_arquivo(texto, nome_arquivo):
    p = Path(nome_arquivo)

    # Cria arquivo se ele não existir
    if not p.exists():
        p.touch()

    if isinstance(nome_arquivo, str):
        nome_arquivo = Path(nome_arquivo)
    
    with nome_arquivo.open('a+') as fp:
        fp.write(texto + "\n")

def verifica_bloqueado(usuario, nome_arquivo):
    p = Path(nome_arquivo)

    # Cria arquivo se ele não existir
    if not p.exists():
        p.touch()

    if isinstance(nome_arquivo, str):
        nome_arquivo = Path(nome_arquivo)
    
    with nome_arquivo.open('r') as fp:
        linhas = fp.readlines()

    if not linhas:
        return False

    # Remove quebra de linha
    linhas = [linha.strip() for linha in linhas]

    return usuario in linhas

def cadastra_usuario(usuario, senha):
    usuarios = carrega_dados(ARQUIVO_USUARIOS)
    nome_usuarios = [u[0] for u in usuarios]

    if usuario in nome_usuarios:
        return False

    senha = aplica_hash(senha, hashlib.sha256)
    escreve_arquivo(f'{usuario},{senha}', ARQUIVO_USUARIOS)

    return True

def verifica_credencial(usuario, senha):
    usuarios = carrega_dados(ARQUIVO_USUARIOS)
    nome_usuarios = [u[0] for u in usuarios]
    senhas_usuarios = [u[1] for u in usuarios]

# Verificar se o usuário existe (verificar se ele pertence à lista nome_usuarios)
    if usuario in nome_usuarios:
        print("O usuario existe!")
        indice_usuario = nome_usuarios.index(usuario)
        
    # Verificar se a senha fornecida corresponde à do usuário
        if senha == senhas_usuarios[indice_usuario]:
            print("senha correta")
            return True
        
        elif senha != senhas_usuarios[indice_usuario]:
            print("senha incorreta")
            return False
    else: 
        print("O usuário não existe")
        return False

if __name__ == '__main__':
    while True:
        mostra_info()
        
        opt = input(">>> ")

        if opt == "1":
            usuario = input("Digite seu nome de usuário: ")
            senha = getpass(prompt="Digite sua senha: ")
            
            if cadastra_usuario(usuario, senha):
                print("Usuário", usuario, "cadastrado com sucesso!")
            else:
                print("Usuário já cadastrado")
        elif opt == "2":
            usuario = input("Digite seu nome de usuário: ")
            senha = getpass(prompt="Digite sua senha: ")
            tentativas = 0
            
            ok = verifica_credencial(usuario, senha)
            while not ok:
                usuario = input("Digite seu nome de usuário: ")
                senha = getpass(prompt="Digite sua senha: ")
                ok = verifica_credencial(usuario, senha)
                tentativas += 1 
                # Implementar mecanismo de bloqueio depois de 5 tentativas
                # Etapas:
                
                verifica_bloqueado(usuario, ARQUIVO_BLOQUEADOS)
                if tentativas == 4:
                    escreve_arquivo(usuario, ARQUIVO_BLOQUEADOS)
                    print("VOCÊ FOI BLOQUEADO, THAUZINHO !")
                    exit(1)
                    
                elif tentativas != 4:
                    verifica_bloqueado(usuario, ARQUIVO_BLOQUEADOS)
                    
                        
                #  1. Verificar se o usuário já foi bloqueado (verifica_bloqueado(usuario, ARQUIVO_BLOQUEADOS))
                #    1.1 Se estiver bloqueado, saia do programa e mostre na tela que o usuário está bloqueado
                #    1.2 Se não, continue a verificação
                #  2. Crie uma variável para armazenar a quantidade de tentativas
                #  3. Caso o número de tentativas seja igual a 5, então bloqueie 
                #     o usuário (escreve_arquivo(usuario, ARQUIVO_BLOQUEADOS)) e saia do programa (exit(1))

            else:
                print("Usuário", usuario, "autenticado! :)")
                break
                
        elif opt == "3":
            print("Tchau! :)")
            break
        else:
            print("Opção", opt, "não existe\n")