#código de joão pedro ferreira frota, cibersegurança turma U

import random
import time

#Boas vindas ao programa

print("Seja bem vindo(a) ao jogo de operações matemáticas.")

# variaveis globais

placar1 = 0
placar2 = 0
rodada = 0
min = 0


#definir quantos jogadores irão participar

def players():
    print("Digite quanto jogadores irao participar. 1 ou 2 ?")
    jogadores = int(input())
    return jogadores

#define a dificuldade

def difficulty():
        
    dificuldade = print("digite a dificuldade que você quer jogar. 1, 2 ou 3")
    dificuldade = input()
    dificuldade = int(dificuldade)
    return dificuldade
    
#define operação

def operation():
    operacao = random.randint(1, 4)
    
    if operacao == 1:
        addition()
    elif operacao == 2:
        subtraction()
    elif operacao == 3:
        multiplication()
    elif operacao == 4:
        division()

# operação de adição

def addition():
    numero = random.randint(min, max)
    a = numero

    numero = random.randint(min, max)
    b = numero

    tempo1 = time.time()
    adicao = a + b
    resposta = print(a, "+", b, "= ")
    resposta = input()
    resposta = int(resposta)

    tempo2 = time.time()
    tempo = tempo1 - tempo2
    tempo = int(tempo)
    punicao = tempo * 0.05
    
    if resposta == adicao:

        placar1 = placar1 + 10 + punicao

        print("Parabéns! jogador 1 marcou um ponto.")
        print()
        print("PLACAR :", placar1, "X", placar2)
        rodada = rodada + 1
    else:
        placar2 = placar2 + 10

        print("Que pena! jogador 2 marcou um ponto.")
        print()
        print("PLACAR :", placar1, "X", placar2)
        rodada = rodada + 1
                        
                        
# operação de subtração 

def subtraction():
    
    numero = random.randint(min, max)
    a = numero

    numero = random.randint(min, max)
    b = numero

    tempo1 = time.time()
    subtracao = a - b
    resposta = print(a, "-", b, "= ")
    resposta = input()
    resposta = int(resposta)

    tempo2 = time.time()
    tempo = tempo1 - tempo2
    tempo = int(tempo)
    punicao = tempo * 0.05
             
    if resposta == subtracao:
    
        placar1 = placar1 + 10 + punicao

        print("Parabéns! jogador 1 marcou um ponto.")
        print()
        print("PLACAR :", placar1, "X", placar2)
        rodada = rodada + 1
    else:
        placar2 = placar2 + 10

        print("Que pena! jogador 2 marcou um ponto.")
        print()
        print("PLACAR :", placar1, "X", placar2)
        rodada = rodada + 1            
            
# operação de multiplicação

def multiplication():

    numero = random.randint(min, max)
    a = numero

    numero = random.randint(min, max)
    b = numero

    tempo1 = time.time()
    multiplicacao = a * b
    resposta = print(a, "*", b, "= ")
    resposta = input()
    resposta = int(resposta)

    tempo2 = time.time()
    tempo = tempo1 - tempo2
    tempo = int(tempo)
    punicao = tempo * 0.05

    if resposta == multiplicacao:

        placar1 = placar1 + 10 + punicao

        print("Parabéns! jogador 1 marcou um ponto.")
        print()
        print("PLACAR :", placar1, "X", placar2)
        rodada = rodada + 1
        partida_single()
    else:
        placar2 = placar2 + 10

        print("Que pena! jogador 2 marcou um ponto.")
        print()
        print("PLACAR :", placar1, "X", placar2)
        rodada = rodada + 1
        partida_single()

# operação de divisão

def division():
    
    numero = random.randint(min, max)
    a = numero

    numero = random.randint(min, max)
    b = numero

    if a == 0 or b == 0:
        numero = random.randint(min, max)
        a = numero

        numero = random.randint(min, max)
        b = numero
        
    else:

        tempo1 = time.time()
        divisao = a / b
        resposta = print(a, "/", b, "= ")
        resposta = input()
        resposta = int(resposta)

        tempo2 = time.time()
        tempo = tempo1 - tempo2
        tempo = int(tempo)
        punicao = tempo * 0.05

        if resposta == divisao:

            placar1 = placar1 + 10 + punicao

            print("Parabéns! jogador 1 marcou um ponto.")
            print()
            print("PLACAR :", placar1, "X", placar2)
            rodada = rodada + 1
            partida_single()
        else:
            placar2 = placar2 + 10

            print("Que pena! jogador 2 marcou um ponto.")
            print()
            print("PLACAR :", placar1, "X", placar2)
            rodada = rodada + 1
            partida_single()

# operação para definir o final da partida single player


def partida_single():
    if placar1 > placar2 and rodada == 6:
        print("Parabéns jogador você venceu!")
        return True
    elif placar2 > placar1 and rodada == 6:
        print("Não foi dessa vez. Vitória do computador!")
        return True
    elif placar1 == placar2 and rodada == 6:
        print("Temos um empate")
        return True 

# operação para definir o final da partida multi player 

def partida_multi():
    if placar1 > placar2 and rodada == 11:
        print("Parabéns jogador você venceu!")
        return True
    elif placar2 > placar1 and rodada == 11:
        print("Não foi dessa vez. Vitória do computador!")
        return True
    elif placar1 == placar2 and rodada == 11:
        print("Temos um empate")
        return True
# ------------------------------------------------------------------------------------------------------------ #
jogadores = players()
if jogadores != 1 and jogadores != 2:
    while(True):
        print()
        print()
        print()
        print("Desculpa não entendi digite novamente")
        print()
        players()
        
elif jogadores == 1:
   
    dificuldade = difficulty()
            
    if (dificuldade != 1 and dificuldade != 2 and dificuldade != 3):
        while(True):
                print()
                print()
                print()
                print("Desculpa não entendi digite novamente")
                print()
                difficulty()
            
    elif dificuldade == 1:
        min = -10
        max = 10
                
    elif dificuldade == 2:
        min = -100
        max = 100
                
    elif dificuldade == 3:
        min = -1000
        max = 1000

elif jogadores == 2:
    
     print("jogadores = 2")          