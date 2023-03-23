#código de joão pedro ferreira frota, cibersegurança turma U

import random
import time
import math

#Boas vindas ao programa

print("Seja bem vindo(a) ao jogo de operações matemáticas.")
print()
print()
print("AVISO ! ESSE CÓDIGO TRABALHA COM RESPOSTA TRUNCADAS")
print()
print()

# variaveis 
placar1 = 0
placar2 = 0
rodada = 1
punicao = 0
resposta = 0
tipo_operacao = 0
min = 0
max = 0
i = 0

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
    
# placar single player 

def resposta_single():
    global tipo_operacao
    global placar1
    global placar2
    global rodada
    global punicao
    global resposta
    
    if tipo_operacao == resposta:
        placar1 = placar1 + 10 + punicao

        print("Parabéns! jogador 1 marcou um ponto.")
        print()
        print("PLACAR :", placar1, "X", placar2)
        rodada = rodada + 1
    
    else:
        placar2 += 10

        print("Que pena! jogador 2 marcou um ponto.")
        print()
        print("PLACAR :", placar1, "X", placar2)
        rodada = rodada + 1

# placar multi player 

def resposta_multi():
    global placar1
    global placar2
    global rodada
    global punicao
    global resposta
    global tipo_operacao
        
    if rodada % 2 == 0:
        if tipo_operacao == resposta:
            placar2 = placar2 + 10 + punicao

            print("Parabéns! jogador 1 marcou um ponto.")
            print()
            print("PLACAR :", placar1, "X", placar2)
            rodada = rodada + 1
    
        else:
            placar1 += 10

            print("Que pena! jogador 2 marcou um ponto.")
            print()
            print("PLACAR :", placar1, "X", placar2)
            rodada = rodada + 1
    else:
        if tipo_operacao == resposta:
            placar1 = placar1 + 10 + punicao

            print("Parabéns! jogador 1 marcou um ponto.")
            print()
            print("PLACAR :", placar1, "X", placar2)
            rodada = rodada + 1
    
        else:
            placar2 += 10

            print("Que pena! jogador 2 marcou um ponto.")
            print()
            print("PLACAR :", placar1, "X", placar2)
            rodada = rodada + 1

# operação de adição 

def addition():
    
    global placar1
    global placar2
    global rodada
    global punicao
    global resposta
    global tipo_operacao
    
    numero = random.randint(min, max)
    a = numero

    numero = random.randint(min, max)
    b = numero

    tempo1 = time.time()
    tipo_operacao = a + b
    resposta = print(a, "+", b, "= ")
    resposta = input()
    resposta = int(resposta)

    tempo2 = time.time()
    tempo = tempo1 - tempo2
    tempo = int(tempo)
    punicao = tempo * 0.05
                        
# operação de subtração 

def subtraction():
    
    global placar1
    global placar2
    global rodada
    global punicao
    global resposta
    global tipo_operacao
    
    numero = random.randint(min, max)
    a = numero

    numero = random.randint(min, max)
    b = numero

    tempo1 = time.time()
    tipo_operacao = a - b
    resposta = print(a, "-", b, "= ")
    resposta = input()
    resposta = int(resposta)

    tempo2 = time.time()
    tempo = tempo1 - tempo2
    tempo = int(tempo)
    punicao = tempo * 0.05
        
# operação de multiplicação

def multiplication():

    global placar1
    global placar2
    global rodada
    global punicao
    global resposta
    global tipo_operacao
    
    numero = random.randint(min, max)
    a = numero

    numero = random.randint(min, max)
    b = numero

    tempo1 = time.time()
    tipo_operacao = a * b
    resposta = print(a, "*", b, "= ")
    resposta = input()
    resposta = int(resposta)

    tempo2 = time.time()
    tempo = tempo1 - tempo2
    tempo = int(tempo)
    punicao = tempo * 0.05
        
# operação de divisão

def division():
    
    global placar1
    global placar2
    global rodada
    global punicao
    global resposta
    global tipo_operacao
    
    numero = random.randint(min, max)
    a = numero

    numero = random.randint(min, max)
    b = numero
    
    while (a == 0 or b == 0):
            numero = random.randint(min, max)
            a = numero

            numero = random.randint(min, max)
            b = numero
        
    else:
           
        tempo1 = time.time()
        tipo_operacao = a / b
        resposta = print(a, "/", b, "= ")
        resposta = input()
        resposta = float(resposta)
        math.trunc(resposta)

        tempo2 = time.time()
        tempo = tempo1 - tempo2
        tempo = int(tempo)
        punicao = tempo * 0.05

# operação para definir o final da partida single player

def fim_partida():
    
    global placar1
    global placar2
    global rodada

    if placar1 > placar2 and rodadas == 5:
        print("Parabéns jogador você venceu!")
        
    elif placar2 > placar1 and rodadas == 5:
        print("Não foi dessa vez. Vitória do computador!")
        
    elif placar1 == placar2 and rodadas == 5:
        print("Temos um empate")
        
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
    rodadas = 5
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
        
        for i in "rodada":
            
            print("RODADA ", rodada)
            print()
            print()
            
            
            operacao = random.randint(1, 4)
            
            if operacao == 1:
                addition()
                resposta_single()
            elif operacao == 2:
                subtraction()
                resposta_single()
            elif operacao == 3:
                multiplication()
                resposta_single()
            elif operacao == 4:
                division()
                resposta_single()

            if rodada == 6:
                if placar1 > placar2 and rodada == 6:
                    print("Parabéns jogador você venceu!")
                    break
                elif placar2 > placar1 and rodada == 6:
                    print("Não foi dessa vez. Vitória do computador!")
                    break
                elif placar1 == placar2 and rodada == 6:
                    print("Temos um empate")
                    break
    
    elif dificuldade == 2:
        
        min = -100
        max = 100
        
        for i in "rodada":
            
            print("RODADA ", rodada)
            print()
            print()
            
            operacao = random.randint(1, 4)
            
            if operacao == 1:
                addition()
                resposta_single()
            elif operacao == 2:
                subtraction()
                resposta_single()
            elif operacao == 3:
                multiplication()
                resposta_single()
            elif operacao == 4:
                division()
                resposta_single()

            if rodada == 6:
                if placar1 > placar2 and rodada == 6:
                    print("Parabéns jogador você venceu!")
                    break
                elif placar2 > placar1 and rodada == 6:
                    print("Não foi dessa vez. Vitória do computador!")
                    break
                elif placar1 == placar2 and rodada == 6:
                    print("Temos um empate")
                    break
                
            
    elif dificuldade == 3:
        
        min = -1000
        max = 1000
        
        for i in "rodada":
            
            print("RODADA ", rodada)
            print()
            print()
            
            operacao = random.randint(1, 4)
            
            if operacao == 1:
                addition()
                resposta_single()
            elif operacao == 2:
                subtraction()
                resposta_single()
            elif operacao == 3:
                multiplication()
                resposta_single()
            elif operacao == 4:
                division()
                resposta_single()
            
            if rodada == 6:
                if placar1 > placar2 and rodada == 6:
                    print("Parabéns jogador você venceu!")
                    break
                elif placar2 > placar1 and rodada == 6:
                    print("Não foi dessa vez. Vitória do computador!")
                    break
                elif placar1 == placar2 and rodada == 6:
                    print("Temos um empate")
                    break


elif jogadores == 2:
    rodadas = 10
    dificuldade = difficulty()

    if (dificuldade != 1 and dificuldade != 2 and dificuldade != 3):
        while (True):
            print()
            print()
            print()
            print("Desculpa não entendi digite novamente")
            print()
            difficulty()

    elif dificuldade == 1:

        min = -10
        max = 10

        for i in "rodada":

            print("RODADA ", rodada)
            print()
            print()

            operacao = random.randint(1, 4)

            if operacao == 1:
                addition()
                resposta_multi()
            elif operacao == 2:
                subtraction()
                resposta_multi()
            elif operacao == 3:
                multiplication()
                resposta_multi()
            elif operacao == 4:
                division()
                resposta_multi()

            if rodada == 6:
                if placar1 > placar2 and rodada == 11:
                    print("Parabéns jogador você venceu!")
                    break
                elif placar2 > placar1 and rodada == 11:
                    print("Não foi dessa vez. Vitória do computador!")
                    break
                elif placar1 == placar2 and rodada == 11:
                    print("Temos um empate")
                    break

    elif dificuldade == 2:

        min = -100
        max = 100

        for i in "rodada":

            print("RODADA ", rodada)
            print()
            print()

            operacao = random.randint(1, 4)

            if operacao == 1:
                addition()
                resposta_multi()
            elif operacao == 2:
                subtraction()
                resposta_multi()
            elif operacao == 3:
                multiplication()
                resposta_multi()
            elif operacao == 4:
                division()
                resposta_multi()

            if rodada == 6:
                if placar1 > placar2 and rodada == 11:
                    print("Parabéns jogador você venceu!")
                    break
                elif placar2 > placar1 and rodada == 11:
                    print("Não foi dessa vez. Vitória do computador!")
                    break
                elif placar1 == placar2 and rodada == 11:
                    print("Temos um empate")
                    break

    elif dificuldade == 3:

        min = -1000
        max = 1000

        for i in "rodada":

            print("RODADA ", rodada)
            print()
            print()

            operacao = random.randint(1, 4)

            if operacao == 1:
                addition()
                resposta_multi()
            elif operacao == 2:
                subtraction()
                resposta_multi()
            elif operacao == 3:
                multiplication()
                resposta_multi()
            elif operacao == 4:
                division()
                resposta_multi()

            if rodada == 6:
                if placar1 > placar2 and rodada == 11:
                    print("Parabéns jogador você venceu!")
                    break
                elif placar2 > placar1 and rodada == 11:
                    print("Não foi dessa vez. Vitória do computador!")
                    break
                elif placar1 == placar2 and rodada == 11:
                    print("Temos um empate")
                    break
