''' Estes exercícios fazem parte do curso de Introdução a Algoritmos, ministrado pelo prof. Gustavo Guanabara e podem ser encontrados no site https://www.cursoemvideo.com/wp-content/uploads/2019/08/exercicios-algoritmos.pdf 

    31) [DESAFIO] Crie um jogo de JoKenPo (Pedra-Papel-Tesoura) '''

# Testando se o usuário digitou o número correto 
def test(player):
    while True:
        if player == 1 or player == 2 or player == 3:
            break
        else:
            print("Você precisa escolher um número entre 1 e 3. Tente de novo!")
            player = int(input("Escolha sua opção: "))
    return player

# Testando se o usuário digitou a letra correta 
def playAgain(choice):
    while True:
        if choice == "S" or choice == "N":
            break
        else:
            print("Você precisa escolher S para Sim ou N para Não. Tente de novo!")
            choice = input("Deseja jogar novamente? [S/N] ")
    return choice

while True:
    print("PEDRA - PAPEL - TESOURA")
    print("-----------------------")
    print("1 - Pedra")
    print("2 - Papel")
    print("3 - Tesoura\n")
    player1 = int(input("Escolha sua opção: "))
    player1 = test(player1)
    player2 = int(input("Escolha sua opção: "))
    player2 = test(player2)
    if (player1 == 1 and player2 == 2) or (player2 == 3 and player1 == 2) or (player2 == 1 and player1 == 3):
        print("Jogador 2 venceu!")
    elif (player2 == 1 and player1 == 2) or (player1 == 3 and player2 == 2) or (player1 == 1 and player2 == 3):
        print("Jogador 1 venceu!")
    else: 
        print("Houve um empate.")
    exit = input("\nDeseja jogar novamente? [S/N] ")
    exit = playAgain(exit)
    if exit == "S":
        print("")
        continue
    else:
        print("O jogo acabou!")
        break

''' 32) [DESAFIO] Crie um jogo onde o computador vai sortear um número entre 1 e 5 o jogador vai tentar descobrir qual foi o valor sorteado. '''

print("\nQuestão 32")
import random
while True:
    print("\nQual o número sorteado?")
    num = random.randint(1, 5)
    while True:
        guess = int(input("Escolha um número entre 1 e 5: "))
        if guess == num:
            print("Parabéns!! Você acertou o valor sorteado!")
            break
        else:
            print("Não foi dessa vez. Tente novamente!")
    # Checando se o usuário deseja repetir o jogo
    exit = input("\nDeseja jogar novamente? [S/N] ")
    exit = playAgain(exit)
    if exit == "S":
        continue
    else:
        print("O jogo acabou!")
        break

''' 33) Escreva um programa para aprovar ou não o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado. '''

print("\nQuestão 33")
casa = float(input("Qual o valor da casa? R$"))
salario = float(input("Qual o seu salário? R$"))
anos = int(input("Em quantos anos você pretende pagar? "))
mensalidade = casa / (anos * 12)
if mensalidade > salario * 0.3:
    print("O empréstimo foi negado.")
else:
    print("Parabéns! Seu empréstimo foi aprovado!")

''' 34) O Índice de Massa Corpórea (IMC) é um valor calculado baseado na altura e no peso de uma pessoa. De acordo com o valor do IMC, podemos classificar o indivíduo dentro de certas faixas.
 - abaixo de 18.5: Abaixo do peso
 - entre 18.5 e 25: Peso ideal
 - entre 25 e 30: Sobrepeso
 - entre 30 e 40: Obesidade
 - acima de 40: Obseidade mórbida
Obs: O IMC é calculado pela expressão peso/altura² (peso dividido pelo quadrado da altura) '''

print("\nQuestão 34")
altura = float(input("Digite sua altura [m]: "))
peso = float(input("Qual o seu peso? [kg]: "))
IMC = peso / altura ** 2
if IMC < 18.5:
    print("Abaixo do peso")
elif IMC < 25:
    print("Peso ideal")
elif IMC < 30:
    print("Sobrepeso")
elif IMC < 40:
    print("Obesidade")
else:
    print("Obesidade mórbida")

''' 35) Uma empresa de aluguel de carros precisa cobrar pelos seus serviços. O aluguel de um carro custa R$90 por dia para carro popular e R$150 por dia para carro de luxo. Além disso, o cliente paga por Km percorrido. Faça um programa que leia o tipo de carro alugado (popular ou luxo), quantos dias de aluguel e quantos Km foram percorridos. No final mostre o preço a ser pago de acordo com a tabela a seguir:
 - Carros populares (aluguel de R$90 por dia)
 - Até 100Km percorridos: R$0,20 por Km
 - Acima de 100Km percorridos: R$0,10 por Km
 - Carros de luxo (aluguel de R$150 por dia)
 - Até 200Km percorridos: R$0,30 por Km
 - Acima de 200Km percorridos: R$0,25 por Km '''

print("\nQuestão 35")

# Testando se o usuário digitou o número correto 
def check(car):
    while True:
        if car == 1 or car == 2:
            break
        else:
            print("Você precisa escolher o número 1 ou 2. Tente de novo!")
            car = int(input("Escolha sua opção: "))
    return car

print("\nTipo de carro:\n 1 - Popular\n 2 - Luxo")
carro = int(input("\nEscolha 1 ou 2 para sua opção de carro: "))
carro = check(carro)
dias = int(input("Por quantos dias você alugou o carro? "))
dist = float(input("Quantos Km você percorreu? "))
if carro == 1:
    if dist <= 100:
        total = 0.2 * dist + 90 * dias
    else:
        total = 0.1 * dist + 90 * dias
else:
    if dist <= 200:
        total = 0.3 * dist + 150 * dias
    else:
        total = 0.25 * dist + 150 * dias
print("Total a pagar: R$" + str(round(total, 2)))