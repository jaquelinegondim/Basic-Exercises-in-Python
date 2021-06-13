''' Estes exercícios fazem parte do curso de Introdução a Algoritmos, ministrado pelo prof. Gustavo Guanabara e podem ser encontrados no site https://www.cursoemvideo.com/wp-content/uploads/2019/08/exercicios-algoritmos.pdf 

    11) Desenvolva uma lógica que leia os valores de A, B e C de uma equação do segundo grau e mostre o valor de Delta.
'''

print("Questão 11")
print("Considerando uma equação do 2° grau como ax² + bx + c = 0, forneça valores para os coeficientes a, b, c.")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
delta = b ** 2 - 4 * a * c
print("O delta da equação " + str(a) + "x² + " + str(b) + "x + " + str(c) + " = 0 é igual a " + str(delta) + "\n")

''' 12) Crie um programa que leia o preço de um produto, calcule e mostre o seu PREÇO PROMOCIONAL, com 5% de desconto. '''

print("Questão 12")
preco = float(input("Digite o preço do produto: R$"))
promo = preco * 0.95
print("O preço promocional com 5% de desconto será R$" + str(round(promo, 2)) + "\n")

''' 13) Faça um algoritmo que leia o salário de um funcionário, calcule e mostre o seu novo salário, com 15% de aumento. '''

print("Questão 13")
salario = float(input("Digite o seu salário: R$"))
aumento = salario * 1.15
print("O novo salário com aumento de 15% será de R$" + str(round(aumento, 2)) + "\n")

''' 14) A locadora de carros precisa da sua ajuda para cobrar seus serviços. Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço total a pagar, sabendo que o carro custa R$90 por dia e R$0,20 por Km rodado. '''

print("Questão 14")
km = float(input("Digite a quantidade de Km percorridos: "))
dias = float(input("Digite o número de dias em que o carro esteve alugado: "))
total = 90 * dias + 0.2 * km
print("Total a pagar: R$" + str(round(total, 2)) + "\n")

''' 15) Crie um programa que leia o número de dias trabalhados em um mês e mostre o salário de um funcionário, sabendo que ele trabalha 8 horas por dia e ganha R$25 por hora trabalhada. '''

print("Questão 15")
diasDeTrabalho = float(input("Digite o número de dias trabalhados no mês: "))
pagamento = diasDeTrabalho * 8 * 25
print("Salário total: R$" + str(round(pagamento, 2)) + "\n")