''' Estes exercícios fazem parte do curso de Introdução a Algoritmos, ministrado pelo prof. Gustavo Guanabara e podem ser encontrados no site https://www.cursoemvideo.com/wp-content/uploads/2019/08/exercicios-algoritmos.pdf 

    41) Desenvolva um programa que mostre na tela a seguinte contagem: 100 95 90 85 80 ... 0 Acabou! '''

print("Questão 41")
i = 100
while i >= 0:
    print(i, end=" ")
    i -= 5
print("Acabou!")

''' 42) Faça um algoritmo que pergunte ao usuário um número inteiro e positivo qualquer e mostre uma contagem até esse valor:
        Ex: Digite um valor: 35
        Contagem: 1 2 3 4 5 6 7 ... 33 34 35 Acabou! '''

print("\nQuestão 42")
i = 1
num = int(input("Digite um número inteiro positivo: "))
while i <= num:
    print(i, end=" ")
    i += 1
print("Acabou!")

''' 43) Desenvolva um algoritmo que mostre uma contagem regressiva de 30 até 1, marcando os números que forem divisíveis por 4, exatamente como mostrado abaixo:
        30 29 [28] 27 26 25 [24] 23 22 21 [20] 19 18 17 [16]... '''

print("\nQuestão 43")
i = 30
while i >= 1:
    if i % 4 == 0:
        print("[" + str(i) + "]", end=" ")
    else:
        print(i, end=" ")
    i -= 1

''' 44) Crie um algoritmo que leia o valor inicial da contagem, o valor final e o incremento, mostrando em seguida todos os valores no intervalo:
        Ex: Digite o primeiro Valor: 3
        Digite o último Valor: 10
        Digite o incremento: 2
        Contagem: 3 5 7 9 Acabou! '''

print(" ")
print("\nQuestão 44")
inicio = int(input("Digite um número inteiro inicial: "))
final = int(input("Digite um número inteiro final: "))
passo = int(input("Digite um número inteiro para incremento: "))
while inicio <= final:
    print(inicio, end=" ")
    inicio += passo
print("Acabou!")

''' 45) O programa acima vai ter um problema quando digitarmos o primeiro valor maior que o último. Resolva esse problema com um código que funcione em qualquer situação. '''

print("\nQuestão 45")
inicio = int(input("Digite um número inteiro inicial: "))
final = int(input("Digite um número inteiro final: "))
passo = int(input("Digite um número inteiro para incremento: "))
if inicio > final:
    temp = inicio
    inicio = final
    final = temp
while inicio <= final:
    print(inicio, end=" ")
    inicio += passo
print("Acabou!")