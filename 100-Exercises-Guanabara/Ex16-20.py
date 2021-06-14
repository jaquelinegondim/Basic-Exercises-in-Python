''' Estes exercícios fazem parte do curso de Introdução a Algoritmos, ministrado pelo prof. Gustavo Guanabara e podem ser encontrados no site https://www.cursoemvideo.com/wp-content/uploads/2019/08/exercicios-algoritmos.pdf 

    16) [DESAFIO] Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dias e quantos anos ele já fumou. Considere que um fumante perde 10 min de vida a cada cigarro. Calcule quantos dias de vida um fumante perderá e exiba o total em dias.
'''

print("Questão 16")
cigarros = int(input("Quantos cigarros você fuma por dia? "))
anos = int(input("Por quantos anos você já fumou? "))
minutos = cigarros * 365 * anos * 10
dias = int(minutos / 60 / 24)
print("Ao fumar " + str(cigarros) + " cigarros por dia durante " + str(anos) + " anos, vocês perderá " + str(dias) + " dias da sua vida!\n")

''' 17) Escreva um programa que pergunte a velocidade de um carro. Caso ultrapasse 80Km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$5 por cada Km acima da velocidade permitida. '''

print("Questão 17")
velocidade = float(input("Qual a velocidade do seu carro em Km/h? "))
if velocidade > 80:
    print("Você foi multado!")
    multa = round((velocidade - 80) * 5, 2)
    print("Valor da multa: R$" + str(multa))

''' 18) Faça um programa que leia o ano de nascimento de uma pessoa, calcule a idade dela e depois mostre se ela pode ou não votar. '''

print("\nQuestão 18")
from datetime import date
anoAtual = date.today().year
anoNasc = int(input("Em que ano você nasceu? "))
idade = anoAtual - anoNasc
if idade >= 16:
    print("Você já pode votar!\n")
else:
    print("Você precisa ter no mínimo 16 anos para votar!\n")

''' 19) Crie um algoritmo que leia o nome e as duas notas de um aluno, calcule a sua média e mostre na tela. No final, analise a média e mostre se o aluno teve ou não um bom aproveitamento (se ficou acima da média 7.0). '''

print("Questão 19")
nome = input("Qual é o seu nome? ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = round((nota1 + nota2) / 2, 2)
print("Média de " + nome + ": " + str(media))
if media > 7:
    print("Você foi aprovado! Parabéns!!")
else:
    print("Você ainda não foi aprovado, tente novamente!")

''' 20) Desenvolva um programa que leia um número inteiro e mostre se ele é PAR ou ÍMPAR. '''

print("\nQuestão 20")
num = int(input("Digite um número inteiro: "))
if num % 2 == 0:
    print("O número é PAR!")
else:
    print("O número é ÍMPAR!")