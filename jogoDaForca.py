#código de joão pedro ferreira frota

from pathlib import Path

# globais
segredo = ""
rodada = 0
caractere = ""
resultado = ""
underlines = ""
palavra = ""
erros = 0

# variáveis de arquivos


# escolher uma palavra em uma bliblioteca 
def buscarPalavra():
    global segredo, rodada
    
    print("DIGITE UMA PALAVRA:")
    segredo = input()
    rodada = 0
# função para o usúario chutar uma letra
def digite():
    global caractere, rodada
    caractere = ""
    print("DIGITE UMA LETRA")
    caractere = input()
    quantDigi = len(caractere)
    while quantDigi > 1:
        limpaTela()
        digite()
    else:
        rodada += 1
        verifica_caractere()
        
# função para localizar caractere
def localiza_caractere():
    global resultado, palavra, underlines, erros, caractere
    
    for elemento in range(len(palavra)):
        if caractere == palavra[elemento]:
            resultado[elemento] = caractere
            return True
        else:
            return False
        
# cria _ e imprime
def cria_underline():
    global resultado, palavra, underlines, segredo, rodada
    if rodada == 0:
        underlines = "_" * len(segredo)
        print(underlines)

        resultado = [resultado for resultado in underlines]

        palavra = [palavra for palavra in segredo]

    else:
        print(underlines)
        resultado = [resultado for resultado in underlines]

        palavra = [palavra for palavra in segredo]
        
# localiza o caractere e retorna a posição     
def verifica_caractere():
    global resultado, palavra, underlines, erros, caractere
    localiza_caractere()
    
    if localiza_caractere == False:
        erros += 1
        criar_boneco()
    elif localiza_caractere == True:
        print(resultado)
        
# cria o boneco 
def criar_boneco():
    global erros
    if erros == 1:
        print("     |")
        print("    0|")
        print("       ")
        print("       ")
        print("       ")
        print("  _____")
        print(" |     |")
        print(" |     |")
        print(" |     |")
        print("_|_____|_")
    elif erros == 2:
        print("     |")
        print("    0|")
        print("    |  ")
        print("       ")
        print("       ")
        print("  _____")
        print(" |     |")
        print(" |     |")
        print(" |     |")
        print("_|_____|_")
    elif erros == 3:
        print("     |")
        print("    0|")
        print("   /|  ")
        print("       ")
        print("       ")
        print("  _____")
        print(" |     |")
        print(" |     |")
        print(" |     |")
        print("_|_____|_")
    elif erros == 4:
        print("     |")
        print("    0|")
        print("   /|\ ")
        print("       ")
        print("       ")
        print("  _____")
        print(" |     |")
        print(" |     |")
        print(" |     |")
        print("_|_____|_")
    elif erros == 5:
        print("     |")
        print("    0|")
        print("   /|\ ")
        print("   /   ")
        print("       ")
        print("  _____")
        print(" |     |")
        print(" |     |")
        print(" |     |")
        print("_|_____|_")
    elif erros == 6:
        print("     |")
        print("    0|")
        print("   /|\ ")
        print("   / \ ")
        print("       ")
        print("  _____")
        print(" |     |")
        print(" |     |")
        print(" |     |")
        print("_|_____|_")
        print()
        print("VOCÊ PERDEU!")
        

# limpa a tela 
def limpaTela():
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    
# --------------------------------------------------------------------------------------------------------------- #

buscarPalavra()
cria_underline()
while "_" in resultado:
    digite()
else:
    limpaTela()
    print("VOCE VENCEU!")