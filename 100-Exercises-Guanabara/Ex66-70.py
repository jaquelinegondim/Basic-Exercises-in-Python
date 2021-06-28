''' Estes exercícios fazem parte do curso de Introdução a Algoritmos, ministrado pelo prof. Gustavo Guanabara e podem ser encontrados no site https://www.cursoemvideo.com/wp-content/uploads/2019/08/exercicios-algoritmos.pdf 

    66) Escreva um programa que leia um número qualquer e mostre a tabuada desse número, usando a estrutura “para”.
        Ex: Digite um valor: 5
        5 x 1 = 5
        5 x 2 = 10
        5 x 3 = 15 ... '''

print("Questão 66")
num = int(input("Digite um número inteiro para ver a sua tabuada: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

''' 67) Faça um programa usando a estrutura “para” que leia um número inteiro positivo e mostre na tela uma contagem de 0 até o valor digitado:
        Ex: Digite um valor: 9
        Contagem: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, FIM! '''

print("\nQuestão 67")
num = int(input("Digite um número inteiro positivo para ver a sua contagem: "))
print("Contagem:", end=" ")
for i in range(0, num + 1):
    print(str(i) + ",", end=" ")
print("FIM!")

''' 68) Crie um programa que leia sexo e peso de 8 pessoas, usando a estrutura “para”. No final, mostre na tela:
        a) Quantas mulheres foram cadastradas
        b) Quantos homens pesam mais de 100Kg
        c) A média de peso entre as mulheres
        d) O maior peso entre os homens '''

# Testando se o usuário digitou a letra correta 
def test(choice):
    while True:
        if choice == "F" or choice == "M":
            break
        else:
            print("Você precisa escolher F para Feminino ou M para Masculino. Tente de novo!")
            choice = input("Qual o seu gênero? [F/M] ")
    return choice

print("\nQuestão 68")
mulheres = 0
homens = []
homens100 = 0
soma = 0
for i in range(8):
    genero = input("Qual o seu gênero? [F/M] ")
    genero = test(genero)
    peso = float(input("Qual o seu peso em kg? "))
    if genero == "F":
        mulheres += 1
        soma += peso
    else:
        homens.append(peso)
        if peso > 100:
            homens100 += 1
print("\nNº de mulheres cadastradas:", mulheres)
print("Homens com mais de 100 kg:", homens100)
print("Média de peso entre as mulheres:", round(soma / mulheres, 2))
print("Maior peso entre os homens:", max(homens))

''' 69) [DESAFIO] Desenvolva um programa que leia o primeiro termo e a razão de uma PA (Progressão Aritmética), mostrando na tela os 10 primeiros elementos da PA e a soma entre todos os valores da sequência. '''