''' Estes exercícios fazem parte do curso de Introdução a Algoritmos, ministrado pelo prof. Gustavo Guanabara e podem ser encontrados no site https://www.cursoemvideo.com/wp-content/uploads/2019/08/exercicios-algoritmos.pdf 

    61) Crie um programa que mostre na tela a seguinte contagem, usando a estrutura “faça enquanto”:
        0 3 6 9 12 15 18 21 24 27 30 Acabou! '''

# Não existe a estrutura do-while no python. Usamos o while com if e break
print("Questão 61")
i = 0
while True:
    print(i, end=" ")
    i += 3
    if i > 30:
        break
print("Acabou!")

''' 62) Faça um programa usando a estrutura “faça enquanto” que leia a idade de várias pessoas. A cada laço, você deverá perguntar para o usuário se ele quer ou não continuar a digitar dados. No final, quando o usuário decidir parar, mostre na tela:
    a) Quantas idades foram digitadas
    b) Qual é a média entre as idades digitadas
    c) Quantas pessoas tem 21 anos ou mais. '''

# Testando se o usuário digitou a letra correta
def exit(choice):
    while True:
        if choice == "S" or choice == "N":
            break
        else:
            print("Você precisa escolher S para Sim ou N para Não. Tente de novo!")
            choice = input("Você deseja incluir novos dados? [S/N] ")
    return choice

print("\nQuestão 62")
media = 0
total = 0
pessoas = 0
answer = ""
while True:
    idade = int(input("Digite a sua idade: "))
    total += 1
    media += idade
    if idade >= 21:
        pessoas += 1
    answer = input("Deseja inserir uma nova idade? [S/N] ")
    answer = exit(answer)
    if answer == "N":
        break
print("\nTotal de idades inseridas:", total)
print("Média das idades:", round(media / total, 2))
print("Número de pessoas com 21 anos ou mais:", pessoas)

''' 63) Crie um programa usando a estrutura “faça enquanto” que leia vários números. A cada laço, pergunte se o usuário quer continuar ou não. No final, mostre na tela:
    a) O somatório entre todos os valores
    b) Qual foi o menor valor digitado
    c) A média entre todos os valores
    d) Quantos valores são pares '''

print("\nQuestão 63")
soma = 0
menor = []
total = 0
pares = 0
while True:
    num = float(input("Digite um número: "))
    soma += num
    menor.append(num)
    total += 1
    if num % 2 == 0:
        pares += 1
    answer = input("Deseja inserir um novo valor? [S/N] ")
    answer = exit(answer)
    if answer == "N":
        break
print("\nSoma de todos os valores:", soma)
print("Menor valor inserido:", min(menor))
print("Média dos valores:", round(soma / total, 2))
print("Número de valores pares:", pares)

''' 64) Desenvolva um programa usando a estrutura “para” que mostre na tela a seguinte contagem:
        0 5 10 15 20 25 30 35 40 Acabou! '''

print("\nQuestão 64")
for i in range(0, 41, 5):
    print(i, end=" ")
print("Acabou!")

''' 65) Desenvolva um programa usando a estrutura “para” que mostre na tela a seguinte contagem:
        100 90 80 70 60 50 40 30 20 10 0 Acabou! '''

print("\nQuestão 65")
for i in range(100, -1, -10):
    print(i, end=" ")
print("Acabou!")