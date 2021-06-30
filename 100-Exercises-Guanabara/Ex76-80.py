''' Estes exercícios fazem parte do curso de Introdução a Algoritmos, ministrado pelo prof. Gustavo Guanabara e podem ser encontrados no site https://www.cursoemvideo.com/wp-content/uploads/2019/08/exercicios-algoritmos.pdf 

76) Crie um programa que preencha automaticamente um vetor numérico com 7 números gerados aleatoriamente pelo computador e depois mostre os valores
gerados na tela. '''

print("Questão 76")
import random
x = []
for i in range(7):
    x.append(random.randint(1, 100))
print(x)

''' 77) Faça um programa que leia 7 nomes de pessoas e guarde-os em um vetor. No final, mostre uma listagem com todos os nomes informados, na ordem inversa daquela em que eles foram informados. '''

print("\nQuestão 77")
nomes = []
for i in range(7):
    nomes.append(input("Digite o seu nome: "))
print("\nNomes em ordem inversa:")
for j in range(6, -1, -1):
    print(nomes[j])

''' 78) Escreva um programa que sorteie 15 números e guarde-os em um vetor. No final, mostre o vetor inteiro na tela e em seguida mostre em que posições foram digitados valores que são múltiplos de 10. '''

print("\nQuestão 78\n")
x = []
position = []
for i in range(15):
    x.append(random.randint(1, 1000))
print(x)
for i in range(15):
    if x[i] % 10 == 0:
        x[i] = "(" + str(x[i]) + ")"
        position.append(x.index(x[i]))
print(x)
print("\nPosição dos múltiplos de 10:", end=" ")
if position == []:
    print("Sem múltiplos de 10")
else:
    for i in position:
        print(i + 1, end=" ")

''' 79) Desenvolva um programa que leia 10 números inteiros e guarde-os em um vetor. No final, mostre quais são os números pares que foram digitados e em que posições eles estão armazenados. '''