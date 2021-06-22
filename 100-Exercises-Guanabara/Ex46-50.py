''' Estes exercícios fazem parte do curso de Introdução a Algoritmos, ministrado pelo prof. Gustavo Guanabara e podem ser encontrados no site https://www.cursoemvideo.com/wp-content/uploads/2019/08/exercicios-algoritmos.pdf 

    46) Crie um programa que calcule e mostre na tela o resultado da soma entre 6 + 8 + 10 + 12 + 14 + ... + 98 + 100. '''

print("Questão 46")
i = 6
sum = 0
while i <= 100:
    sum += i
    i += 2
print("Soma: " + str(sum))

''' 47) Desenvolva um aplicativo que mostre na tela o resultado da expressão 500 + 450 + 400 + 350 + 300 + ... + 50 + 0 '''

print("\nQuestão 47")
i = 500
sum = 0
while i >= 0:
    sum += i
    i -= 50
print("Soma: " + str(sum))

''' 48) Faça um programa que leia 7 números inteiros e no final mostre o somatório entre eles. '''

print("\nQuestão 48")
sum = 0
i = 0
while i < 7:
    num = int(input("Digite um número inteiro: "))
    sum += num
    i += 1
print("Soma: " + str(sum))

''' 49) Crie um programa que leia 6 números inteiros e no final mostre quantos deles são pares e quantos são ímpares. '''

print("\nQuestão 49")
par = 0
impar = 0
i = 0
while i < 6:
    num = int(input("Digite um número inteiro: "))
    if num % 2 == 0:
        par += 1
    else:
        impar += 1
    i += 1
print("Pares: " + str(par))
print("Ímpares: " + str(impar))

''' 50) Desenvolva um programa que faça o sorteio de 20 números entre 0 e 10 e mostre na tela:
        a) Quais foram os números sorteados
        b) Quantos números estão acima de 5
        c) Quantos números são divisíveis por 3 '''

print("\nQuestão 50")
import random
i = 0
maior = 0
div = 0
print("Números sorteados:", end=" ")
while i < 20:
    num = random.randint(1, 11)
    if num > 5:
        maior += 1
    elif num % 3 == 0:
        div += 1
    print(num, end=" ")
    i += 1
print("\nMaiores que 5: " + str(maior))
print("Divisíveis por 3: " + str(div))