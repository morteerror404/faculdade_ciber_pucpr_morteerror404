import random, os, time

     
def cria_vetor():
    
    vet = []
    
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
    tamanho = (dimensao * dimensao) / 2
    tamanho = int(tamanho)
    for i in range(tamanho):
        letra = random.choice(caracteres)
        
        vet.append(letra)
        vet.append(letra)
        
        random.shuffle(vet)

    vetor_matriz(dimensao, vet)

def vetor_matriz(dimensao, vet):
    matriz_verdadeira = []
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
        
    cria_matriz_falsa(dimensao)
    ver_novamente(dimensao, matriz_verdadeira)

def printa_memorize(dimensao, matriz_verdadeira):

    for p in range(dimensao):
        print(matriz_verdadeira[p])
        
        
def cria_matriz_falsa(dimensao):
    matriz_falsa = []
    
    for i in range(dimensao):
        for j in range(dimensao):
            matriz_falsa.append("#")         
            
def tentativa():
    print("Digite a primeira cordenada, separe por linha coluna por uma vírgula:")
    cordenada1 = input()
    print("Digite a primeira cordenada, separe por linha coluna por uma vírgula:")
    cordenada2 = input()
    
    linha1, coluna1 = map(int, cordenada1.split(',')) 
    linha2, coluna2 = map(int, cordenada2.split(','))
    

def atualiza_matriz_falsa(linha1, linha2, coluna1, coluna2, matriz_falsa, matriz_verdadeira):
    
    matriz_falsa[linha1][coluna1] = matriz_verdadeira[linha1][coluna1]
    matriz_falsa[linha2][coluna2] = matriz_verdadeira[linha2][coluna2]

    elemento1 = matriz_falsa[linha1][coluna1]
    elemento2 = matriz_falsa[linha2][coluna2]

    printa_matriz_falsa(matriz_falsa)
    
    if elemento1 != elemento2:
        matriz_falsa[linha1][coluna1] = "#"
        matriz_falsa[linha2][coluna2] = "#"

def printa_matriz_falsa(matriz_falsa, dimensao):
    
    for p in range(dimensao):
        print(matriz_falsa[p])
                    
def verifica_matriz_falsa(matriz_falsa, dimensao):
    
    verificado = 0
    
    for i in range(dimensao):
        for j in range(dimensao):
            
            if matriz_falsa[j] == "#":
                verificado += 1
                
def roda_jogo(verificado):
    while verificado == 0:
        tentativa()
        atualiza_matriz_falsa()
        verifica_matriz_falsa()
        printa_matriz_falsa()
        
def ver_novamente(dimensao, matriz_verdadeira):
    while True:
        printa_memorize(dimensao, matriz_verdadeira)
        
        time.sleep(3)
        
        limpar_terminal()
        print("Deseja ver novamente ? s ou n")
        resposta = input()

        if resposta == "n":
            print("Então vamos começar =)")
            limpar_terminal()
            roda_jogo()
            break
            
def limpar_terminal():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')
        
        
cria_vetor()
