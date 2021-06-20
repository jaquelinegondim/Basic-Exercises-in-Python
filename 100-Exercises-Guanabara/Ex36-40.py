''' Estes exercícios fazem parte do curso de Introdução a Algoritmos, ministrado pelo prof. Gustavo Guanabara e podem ser encontrados no site https://www.cursoemvideo.com/wp-content/uploads/2019/08/exercicios-algoritmos.pdf 

    36) Um programa de vida saudável quer dar pontos atividades físicas que podem ser trocados por dinheiro. O sistema funciona assim:
        - Cada hora de atividade física no mês vale pontos
        - até 10h de atividade no mês: ganha 2 pontos por hora
        - de 10h até 20h de atividade no mês: ganha 5 pontos por hora
        - acima de 20h de atividade no mês: ganha 10 pontos por hora
        - A cada ponto ganho, o cliente fatura R$0,05 (5 centavos)
    Faça um programa que leia quantas horas de atividade uma pessoa teve por mês, calcule e mostre quantos pontos ela teve e quanto dinheiro ela conseguiu ganhar. '''

print("Questão 36")
horas = int(input("Quantas horas por mês você se exercitou? "))
if horas <= 10:
    pontos = horas * 2
elif horas <= 20:
    pontos = horas * 5
else:
    pontos = horas * 10
print("\nPontos no mês: " + str(pontos))
print("Dinheiro obtido: R$" + str(pontos * 0.05))

''' 37) Uma empresa precisa reajustar o salário dos seus funcionários, dando um aumento de acordo com alguns fatores. Faça um programa que leia o salário atual, o gênero do funcionário e há quantos anos esse funcionário trabalha na empresa. No final, mostre o seu novo salário, baseado na tabela a seguir:
    - Mulheres
        - menos de 15 anos de empresa: +5%
        - de 15 até 20 anos de empresa: +12%
        - mais de 20 anos de empresa: +23%
    - Homens
        - menos de 20 anos de empresa: +3%
        - de 20 até 30 anos de empresa: +13%
        - mais de 30 anos de empresa: +25% '''

# Testando se o usuário digitou a letra correta 
def test(choice):
    while True:
        if choice == "F" or choice == "M":
            break
        else:
            print("Você precisa escolher F para Feminino ou M para Masculino. Tente de novo!")
            choice = input("Qual o seu gênero? [F/M] ")
    return choice

print("\nQuestão 37")
salario = float(input("Qual o seu salário? R$"))
genero = input("Qual o seu gênero? [F/M] ")
genero = test(genero)
anos = int(input("Há quantos anos você trabalha na empresa? "))
if genero == "F":
    if anos < 15:
        salario = salario * 1.05
    elif anos <= 20:
        salario = salario * 1.12
    else:
        salario = salario * 1.23
else:
    if anos < 20:
        salario = salario * 1.03
    elif anos <= 30:
        salario = salario * 1.13
    else:
        salario = salario * 1.25
print("Salário com aumento: R$" + str(round(salario, 2)))

''' 38) Escreva um programa que mostre na tela a seguinte contagem: 6 7 8 9 10 11 Acabou! '''

print("\nQuestão 38")
i = 6
while i < 12:
    print(i, end=" ")
    i += 1
print("Acabou!")

''' 39) Faça um algoritmo que mostre na tela a seguinte contagem: 10 9 8 7 6 5 4 3 Acabou! '''

print("\nQuestão 39")
i = 10
while i > 2:
    print(i, end=" ")
    i -= 1
print("Acabou!")

''' 40) Crie um aplicativo que mostre na tela a seguinte contagem: 0 3 6 9 12 15 18 Acabou! '''

print("\nQuestão 40")
i = 0
while i < 20:
    print(i, end=" ")
    i += 3
print("Acabou!")