#programa em Python para jogar Jokenpô (Pedra, Papel, Tesoura) com o computador:

#Importe os módulos necessários

from random import randint
import time

#opções para o jogo

opcoes = ["Pedra", "Papel", "Tesoura"]
print("Vamos jogar Jokenpô!")
print("Escolha uma opção:")
print("1. Pedra")
print("2. Papel")
print("3. Tesoura")

#Peça ao usuário para escolher uma opção

escolha_usuario = int(input("Digite o número correspondente à sua escolha: "))


#verificar escolha_computador

if escolha_usuario < 1 or escolha_usuario > 3:
    print("Opção inválida. Por favor, escolha novamente.")
else:
    escolha_computador = randint(1, 3)
    print("Computador escolheu:", opcoes[escolha_computador - 1])
    time.sleep(1)  # Aguarde 1 segundo para criar suspense

#Determinar o vencedor e exibir o resultado

    if escolha_usuario == escolha_computador:
        print("Empate!")
    elif (escolha_usuario == 1 and escolha_computador == 3) or \
            (escolha_usuario == 2 and escolha_computador == 1) or \
            (escolha_usuario == 3 and escolha_computador == 2):
        print("Você ganhou!")
    else:
        print("Computador ganhou!")
