''' Estes exercícios fazem parte do curso de Introdução a Algoritmos, ministrado pelo prof. Gustavo Guanabara e podem ser encontrados no site https://www.cursoemvideo.com/wp-content/uploads/2019/08/exercicios-algoritmos.pdf 

    21) Faça um algoritmo que leia um determinado ano e mostre se ele é ou não BISSEXTO.
'''

print("Questão 21")
ano = int(input("Digite um ano: "))
if (ano % 4 == 0 and ano % 100 != 100) or (ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0):
    print("O ano é BISSEXTO!")
else:
    print("O ano NÃO é bissexto!")

''' 22) Escreva um programa que leia o ano de nascimento de um rapaz e mostre a sua situação em relação ao alistamento militar.
        - Se estiver antes dos 18 anos, mostre em quantos anos faltam para o alistamento.
        - Se já tiver depois dos 18 anos, mostre quantos anos já se passaram do alistamento. '''

print("\nQuestão 22")
from datetime import date
anoAtual = date.today().year
anoNasc = int(input("Em que ano você nasceu? "))
idade = anoAtual - anoNasc
if idade < 18:
    print("Faltam " + str(18 - idade) + " anos para o alistamento.")
else:
    print("Já se passaram " + str(idade - 18) + " anos desde que você se alistou.")

''' 23) Numa promoção exclusiva para o Dia da Mulher, uma loja quer dar descontos para todos, mas especialmente para mulheres. Faça um programa que leia nome, sexo e o valor das compras do cliente e calcule o preço com desconto. Sabendo que:
    - Homens ganham 5% de desconto
    - Mulheres ganham 13% de desconto '''

print("\nQuestão 23")
nomeCliente = input("Qual é o seu nome? ")
generoCliente = input("Qual é o seu gênero? [F/M] ")

# Testing customer's answer for gender
while True:
    if generoCliente == "F" or generoCliente == "M":
        break
    else:
        print("Você precisa informar o seu gênero digitando F para feminino ou M para masculino. Tente novamente!")
        generoCliente = input("Qual é o seu gênero? [F/M] ")

valorCompra = float(input("Qual o valor das suas compras? R$"))

if generoCliente == "F":
    print("Preço com desconto: R$" + str(round(valorCompra - valorCompra * 0.13, 2)))
else:
    print("Preço com desconto: R$" + str(round(valorCompra - valorCompra * 0.05, 2)))

''' 24) Faça um algoritmo que pergunte a distância que um passageiro deseja percorrer em Km. Calcule o preço da passagem, cobrando R$0.50 por Km para viagens até 200Km e R$0.45 para viagens mais longas. '''

print("\nQuestão 24")
distancia = float(input("Qual a distância que você pretende percorrer em Km? "))
if distancia > 200:
    print("Preço da passagem: R$" + str(round(distancia * 0.45, 2)))
else:
    print("Preço da passagem: R$" + str(round(distancia * 0.5, 2)))

''' 25) [DESAFIO] Crie um programa que leia o tamanho de três segmentos de reta. Analise seus comprimentos e diga se é possível formar um triângulo com essas retas. Matematicamente, para três segmentos formarem um triângulo, o comprimento de cada lado deve ser menor que a soma dos outros dois.
 '''

print("\nQuestão 25")
reta1 = float(input("Reta 1 [cm]: "))
reta2 = float(input("Reta 2 [cm]: "))
reta3 = float(input("Reta 3 [cm]: "))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print("É possível formar um triângulo!")
else:
    print("Não é possível formar um triângulo!")