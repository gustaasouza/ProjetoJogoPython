import random

def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)
    tentativas = 0
    pontos = 1000

    print("Qual nivel de dificuldade você gostaria?")
    nivel = int(input("(1) Fácil, (2) Médio (3) Difícil  \n Defina o nível: "))

    if nivel == 1:
        tentativas = 20
    elif nivel == 2:
        tentativas = 10
    else:
        tentativas = 5

    for rodada in range(1, tentativas + 1):
        chute = int(input('Digite um numero entre 1 e 100: '))

        print(f"Tentativa {rodada} de {tentativas}")
        print(f"Voce digitou {chute}")

        if(chute < 1 or chute > 100):
            print("Voce deve digitar um número entre 1 e 100!")
            continue


        if chute > numero_secreto:
            aproximacao = "Maior"
        elif chute < numero_secreto:
            aproximacao = "Menor"
        else:
            aproximacao = "Acertou"



        if numero_secreto == chute:
            print(f"Você acertou!!!!! e fez {pontos}")
            break
            
        else:
            print(f"Você errou, seu chute foi {aproximacao}")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print('FIM DE JOGO!')

if(__name__ == "__main__"):
    jogar()