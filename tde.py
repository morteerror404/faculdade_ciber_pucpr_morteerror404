#código de joão pedro ferreira frota, cibersegurança turma U

import random
import time

#Boas vindas ao programa

print("Seja bem vindo(a) ao jogo de operações matemáticas.")

jogadores = 0
jogadores = input("Digite quanto jogadores irao participar. 1 ou 2 ?")
jogadores = int(jogadores)

if jogadores == 1:

    dificuldade = input("digite a dificuldade que você quer jogar. 1, 2 ou 3")
    dificuldade = int(dificuldade)
    
    if dificuldade == 1:
        numero = 0
        random.randrange(-10, 10)
        
        a = numero
        random(numero)
        b = numero

        adicao = a + b
        resultado = adicao
        print(resultado)

    elif dificuldade == 2:

        numero = 0
        numero.randrange(-10, 10)
        random.choice(numero)
        a = numero
        random(numero)
        b = numero

    elif dificuldade == 3:

        numero = 0
        numero.randrange(-10, 10)
        random.choice(numero)
        a = numero
        random(numero)
        b = numero

    else:
        jogadores = input("desculpa não entendi. qual a dificuldade? 1 ou 2")
        jogadores = int(jogadores)

elif jogadores == 2:

    dificuldade = input("digite a dificuldade que você quer jogar. 1, 2 ou 3")
    dificuldade = int(dificuldade)
    
    if dificuldade == 1:

        numero = 0
        numero.randrange(-10, 10)
        random.choice(numero)
        a = numero
        random(numero)
        b = numero

    elif dificuldade == 2:

        numero = 0
        numero.randrange(-10, 10)
        random.choice(numero)
        a = numero
        random(numero)
        b = numero

    elif dificuldade == 3:

        numero = 0
        numero.randrange(-10, 10)
        random.choice()
        a = numero
        random(numero)
        b = numero

    else:
        jogadores = input("desculpa não entendi. qual a dificuldade? 1 ou 2")
        jogadores = int(jogadores)

else:
    jogadores = input("desculpa não entendi. quantos irão jogar? 1 ou 2")
    jogadores = int(jogadores)

