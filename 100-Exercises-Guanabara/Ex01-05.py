''' Estes exercícios fazem parte do curso de Introdução a Algoritmos, ministrado pelo prof. Gustavo Guanabara e podem ser encontrados no site https://www.cursoemvideo.com/wp-content/uploads/2019/08/exercicios-algoritmos.pdf 

    1) Escreva um programa que mostre na tela a mensagem "Olá, Mundo!"
'''
print("Questão 1")
print("Olá, Mundo!\n")

''' 2) Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boasvindas para ela: '''

print("Questão 2")
nome = input("Qual é o seu nome? ")
print("Olá, " + nome + "! É um prazer te conhecer!\n")

''' 3) Crie um programa que leia o nome e o salário de um funcionário, mostrando no final uma mensagem. '''

print("Questão 3")
nomeFunc = input("Nome do funcionário: ")
salarioFunc = float(input("Salário do funcionário: "))
print("O funcionário " + nomeFunc + " tem um salário de R$" + str(round(salarioFunc, 2)) + " em Junho.\n")

''' 4) Desenvolva um algoritmo que leia dois números inteiros e mostre o somatório entre eles. '''

print("Questão 4")
num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))
print("A soma entre " + str(num1) + " e " + str(num2) + " é igual a " + str(num1 + num2) + ".\n")

''' 5) Faça um programa que leia as duas notas de um aluno em uma matéria e mostre na tela a sua média na disciplina. '''

print("Questão 5")
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
media = round((nota1 + nota2) / 2, 2)
print("A média entre " + str(nota1) + " e " + str(nota2) + " é igual a " + str(media) + ".")