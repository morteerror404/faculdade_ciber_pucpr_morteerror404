import random, os, time

vet = []
matriz_verdadeira =[]
matriz_falsa = []

linha1 = 0
linha2 = 0
coluna1 = 0
coluna2 = 0
verificado = 0
dimensao = 0

def cria_vetor(dimensao, vet, matriz_verdadeira):
    
    print("Digite a dificuldade: [1], [2], [3]")
    dificuldade = int(input())
    
    if dificuldade == 1:
        dimensao = 4
    elif dificuldade == 2:
        dimensao = 6 
    elif dificuldade == 3:
        dimensao = 8
    else:
        print("Não entendi, por favor digite novamente:")
        dificuldade = int(input())
        
    caracteres = [chr(i) for i in range(65, 91)]
    tamanho = (dimensao * dimensao) // 2
    
    for i in range(tamanho):
        letra = random.choice(caracteres)
        
        vet.append(letra)
        vet.append(letra)
        
        random.shuffle(vet)
    
    contador = 0
    for i in range(dimensao):
        linha = []
        for j in range(dimensao):
            if contador < len(vet):
                linha.append(vet[contador])
                contador += 1
            else:
                linha.append(None)
        matriz_verdadeira.append(linha)
    
    return dimensao
    

def cria_matriz_falsa(dimensao):
    matriz_falsa = []

    for _ in range(dimensao):
        linha = ["#" for _ in range(dimensao)]
        matriz_falsa.append(linha)

    return matriz_falsa

def tentativa(linha1, linha2, coluna1, coluna2, matriz_falsa, matriz_verdadeira):
    
    print("Digite a primeira cordenada, separe por linha coluna por uma vírgula:")
    cordenada1 = input()
    print("Digite a primeira cordenada, separe por linha coluna por uma vírgula:")
    cordenada2 = input()
    
    linha1, coluna1 = map(int, cordenada1.split(',')) 
    linha2, coluna2 = map(int, cordenada2.split(','))
       
    matriz_falsa[linha1][coluna1] = matriz_verdadeira[linha1][coluna1]
    matriz_falsa[linha2][coluna2] = matriz_verdadeira[linha2][coluna2]

    elemento1 = matriz_falsa[linha1][coluna1]
    elemento2 = matriz_falsa[linha2][coluna2]

    
    if elemento1 != elemento2:
        print()
        print("resposta errada")
        print()
        printa_matriz_falsa(matriz_falsa)
        print()
        
        matriz_falsa[linha1][coluna1] = "#"
        matriz_falsa[linha2][coluna2] = "#"
    
    else:
        print()
        print("resposta correta")
        print()
        printa_matriz_falsa(matriz_falsa)
        print()
        
def printa_matriz_verdadeira(matriz_verdadeira):
    
    for p in matriz_verdadeira:
        print(p)

def printa_matriz_falsa(matriz_falsa):
    
    for p in matriz_falsa:
        print(p)
                    
def verifica_matriz_falsa(matriz_falsa, dimensao):
    
    verificado = 0
    
    for i in range(dimensao):
        for j in range(dimensao):
            
            if matriz_falsa[j] == "#":
                verificado += 1
    return verificado
    
def limpar_terminal():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')
        
        
dimensao = cria_vetor(dimensao, vet, matriz_verdadeira)
matriz_falsa = cria_matriz_falsa(dimensao)

while True:
    
    printa_matriz_verdadeira(matriz_verdadeira)
            
    time.sleep(5)

    limpar_terminal()
    print("Deseja ver novamente ? s ou n")
    resposta = input()

    if resposta == "n":
        print("Então vamos começar =)")
        limpar_terminal()
        break

while verificado == 0:

    tentativa(linha1, linha2, coluna1, coluna2,matriz_falsa, matriz_verdadeira)
    print(" ")
    verifica_matriz_falsa(matriz_falsa, dimensao)
    
    