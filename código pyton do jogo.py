from random import randint
from time import sleep

opcoes = ["Pedra", "Papel", "Tesoura"]
opNum = ['1','2','3']
print("Vamos jogar Jokenpô!")
print("Escolha uma opção:")
print("1. Pedra")
print("2. Papel")
print("3. Tesoura")

condicao = True
while condicao:
    escolha_usuario = input("Digite o número correspondente à sua escolha: ")
    if escolha_usuario in opNum:
        escolha_usuario = int(escolha_usuario)
        condicao = False
    else:
        print("Opção inválida. Por favor, escolha novamente.")

escolha_computador = randint(1, 3)

print('Jo')
sleep(1)
print('Ken')
sleep(1)
print('Pô')
sleep(2)
print('- ' * 15)
print("Computador escolheu:", opcoes[escolha_computador - 1])
print("Usuário escolheu:", opcoes[escolha_usuario -1])
print('- ' * 15)
                                                     
if escolha_usuario == escolha_computador:
    print("Empate!")
elif (escolha_usuario == 1 and escolha_computador == 3) or \
    (escolha_usuario == 2 and escolha_computador == 1) or \
    (escolha_usuario == 3 and escolha_computador == 2):
    print("Você ganhou!")
else:
    print("Computador ganhou!")
