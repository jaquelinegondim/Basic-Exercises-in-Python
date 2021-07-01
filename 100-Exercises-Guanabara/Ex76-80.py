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

print()
print("\nQuestão 79\n")
x = []
pares = []
position = []
for i in range(10):
    x.append(random.randint(1, 1000))
print(x)
for i in range(10):
    if x[i] % 2 == 0:
        pares.append(x[i])
        position.append(x.index(x[i]))
if position == []:
    print("Sem múltiplos de 2")
else:
    print("Números pares:", pares)
    print("Posição dos múltiplos de 2:", end=" ")
    for i in position:
        print(i + 1, end=" ")

''' 80) Faça um algoritmo que preencha um vetor de 30 posições com números entre 1 e 15 sorteados pelo computador. Depois disso, peça para o usuário digitar um número (chave) e seu programa deve mostrar em que posições essa chave foi encontrada. Mostre também quantas vezes a chave foi sorteada. '''

print()
print("\nQuestão 80\n")
x = []
soma = 0
position = []
# Sorteando os números
for i in range(30):
    x.append(random.randint(1, 15))
chave = int(input("Digite um número entre 1 e 15: "))

# Testando resposta do usuário
def test(choice):
    while True:
        if choice >= 1 and choice <= 15:
            break
        else:
            print("Você precisa digitar um número entre 1 e 15. Tente novamente.")
            choice = int(input("Digite um número entre 1 e 15: "))
    return choice

chave = test(chave)
print("Números sorteados:", x)
# Obtendo a posição da chave e quantas vezes ela foi sorteada
j = 0
for i in x:
    if i == chave:
        value = x.index(i, j) + 1 # posição da chave
        position.append(value) # add posição na lista
        j = value # alterando valor de j para que a função index conte a partir da posição seguinte
        soma += 1

if chave not in x:
    print("A chave não foi sorteada.")
else:
    print("A chave foi sorteada", soma, "vezes.")
    print("Posição da(s) chave(s):", end=" ")
    print(position)