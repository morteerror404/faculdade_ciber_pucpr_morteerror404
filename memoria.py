import random 
     
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

    printa_memorize(dimensao, matriz_verdadeira)
    

def printa_memorize(dimensao, matriz_verdadeira):

    for p in range(dimensao):
        print(matriz_verdadeira[p])
        
cria_vetor()