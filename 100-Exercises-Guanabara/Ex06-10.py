''' Estes exercícios fazem parte do curso de Introdução a Algoritmos, ministrado pelo prof. Gustavo Guanabara e podem ser encontrados no site https://www.cursoemvideo.com/wp-content/uploads/2019/08/exercicios-algoritmos.pdf 

    6) Faça um programa que leia um número inteiro e mostre o seu antecessor e seu sucessor.
'''
print("Questão 6")
num = int(input("Digite um número inteiro: "))
print("Antecessor: " + str(num - 1))
print("Sucessor: " + str(num + 1) + "\n")

''' 7) Crie um algoritmo que leia um número real e mostre na tela o seu dobro e a sua terça parte. '''

print("Questão 7")
real = float(input("Digite um número real: "))
print("Dobro: " + str(real * 2))
print("Terça parte: " + str(round(real / 3, 2)) + "\n")

''' 8) Desenvolva um programa que leia uma distância em metros e mostre os valores relativos em outras medidas. '''

print("Questão 8")
metro = float(input("Forneça uma distância em metros: "))
print(str(metro * 1000) + " Km" + "   " + str(metro / 10) + " dm")
print(str(metro * 100) + " Hm" + "    " + str(metro / 100) + " cm")
print(str(metro * 10) + " Dam" + "    " + str(metro / 1000) + " mm\n")

''' 9) Faça um algoritmo que leia quanto dinheiro uma pessoa tem na carteira (em R$) e mostre quantos dólares ela pode comprar. Considere US$1,00 = R$3,45. '''

print("Questão 9")
valor = float(input("Quantos reais você tem na sua carteira? R$"))
print("Você possui US$" + str(round(valor / 3.45, 2)) + " na sua carteira.\n")

''' 10) Faça um algoritmo que leia a largura e altura de uma parede, calcule e mostre a área a ser pintada e a quantidade de tinta necessária para o serviço, sabendo que cada litro de tinta pinta uma área de 2metros quadrados. '''

print("Questão 10")
largura = float(input("Forneça a largura da parede em metros: "))
altura = float(input("Forneça a altura da parede em metros: "))
area = largura * altura
litros = area / 2
print("A parede possui " + str(area) + " m² de área e serão necessários " + str(litros) + " L de tinta.")