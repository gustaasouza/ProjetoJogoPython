import forca
import adivinhação
print("*********************************")
print("*******Escolha o seu Jogo!*******")
print("*********************************")


print("(1) Forca (2) Adivinhação")

jogo = int(input('Qual jogo deseja jogar?'))

if jogo == 1:
    print('Jogando Forca')
    forca.jogar()
elif jogo == 2:
    print('Jogando Adivinhação')
    adivinhação.jogar()