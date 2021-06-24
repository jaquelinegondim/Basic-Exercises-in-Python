''' Estes exercícios fazem parte do curso de Introdução a Algoritmos, ministrado pelo prof. Gustavo Guanabara e podem ser encontrados no site https://www.cursoemvideo.com/wp-content/uploads/2019/08/exercicios-algoritmos.pdf 

    51) Faça um aplicativo que leia o preço de 8 produtos. No final, mostre na tela qual foi o maior e qual foi o menor preço digitados. '''

print("Questão 51\n")
j = 0
answer = []
while j < 8:
    num = float(input("Digite o preço do produto: R$"))
    answer.append(num)
    j += 1

print("\nValor máximo: " + str(max(answer)))
print("Valor mínimo: " + str(min(answer)))

''' 52) Crie um algoritmo que leia a idade de 10 pessoas, mostrando no final:
        a) Qual é a média de idade do grupo
        b) Quantas pessoas tem mais de 18 anos
        c) Quantas pessoas tem menos de 5 anos
        d) Qual foi a maior idade lida '''

print("\nQuestão 52")
i = 0
maior = 0
maior18 = 0
menor5 = 0
media = 0
while i < 10:
    idade = int(input("Digite uma idade: "))
    media += idade
    if idade > maior:
        maior = idade
    if idade > 18:
        maior18 += 1
    if idade < 5:
        menor5 += 1
    i += 1
media = media / i
print("\nMaior idade: " + str(maior))
print("Maior que 18 anos: " + str(maior18))
print("Menor que 5 anos: " + str(menor5))
print("Média das idades: " + str(media))

''' 53) Faça um programa que leia a idade e o sexo de 5 pessoas, mostrando no final:
        a) Quantos homens foram cadastrados
        b) Quantas mulheres foram cadastradas
        c) A média de idade do grupo
        d) A média de idade dos homens
        e) Quantas mulheres tem mais de 20 anos '''

# Testando se o usuário digitou a letra correta 
def test(choice):
    while True:
        if choice == "F" or choice == "M":
            break
        else:
            print("Você precisa escolher F para Feminino ou M para Masculino. Tente de novo!")
            choice = input("Qual o seu gênero? [F/M] ")
    return choice

print("\nQuestão 53")
i = 0
media = 0
mediahomens = 0
homens = 0
mulheres = 0
mulheres20 = 0
while i < 5:
    idade = int(input("Digite a sua idade: "))
    media += idade
    genero = input("Qual o seu gênero? [F/M] ")
    genero = test(genero)
    if genero == "F":
        mulheres += 1
        if idade > 20:
            mulheres20 += 1
    else:
        homens += 1
        mediahomens += idade
    i += 1
media = media / i
if homens != 0:
    mediahomens = mediahomens / homens
print("\nHomens: " + str(homens))
print("Mulheres: " + str(mulheres))
print("Média de idade do grupo: " + str(media))
print("Média de idade dos homens: " + str(mediahomens))
print("Mulheres com mais de 20 anos: " + str(mulheres20))

''' 54) Desenvolva um aplicativo que leia o peso e a altura de 7 pessoas, mostrando no final:
        a) Qual foi a média de altura do grupo
        b) Quantas pessoas pesam mais de 90Kg
        c) Quantas pessoas que pesam menos de 50Kg tem menos de 1.60m
        d) Quantas pessoas que medem mais de 1.90m pesam mais de 100Kg. '''

print("\nQuestão 54")
i = 0
media = 0
peso90 = 0
peso50 = 0
peso100 = 0
while i < 7:
    peso = float(input("Digite o seu peso em kg: "))
    altura = float(input("Digite sua altura em m: "))
    media += altura
    if peso > 90:
        peso90 += 1
    if peso < 50 and altura < 1.6:
        peso50 += 1
    if peso > 100 and altura > 1.9:
        peso100 += 1
    i += 1
media = media / i
print("\nMédia de altura [m]: " + str(media))
print("Pessoas com mais de 90 kg: " + str(peso90))
print("Pessoas com mais de 100 kg e altura maior que 1.90 m: " + str(peso100))
print("Pessoas com menos de 50 kg e altura menor que 1.60 m: " + str(peso50))

''' 55) [DESAFIO] Vamos melhorar o jogo que fizemos no exercício 32. A partir de agora, o computador vai sortear um número entre 1 e 10 e o jogador vai ter 4 tentativas para tentar acertar. '''

print("\nQuestão 55\n")
print("Adivinhe um número entre 1 e 10 sorteado pelo computador\nVocê tem 4 tentativas!\n")
import random
num = random.randint(1, 10)
i = 0
chance = 3
while i < 4:
    guess = int(input("Digite um número entre 1 e 10: "))
    if guess == num:
        print("Parabéns! Você acertou o número!")
        break
    else:
        if i < 3:
            print("Não foi dessa vez, você tem mais " + str(chance) + " tentativa(s).")
        else:
            print("O jogo acabou!")
    i += 1
    chance -= 1