''' Estes exercícios fazem parte do curso de Introdução a Algoritmos, ministrado pelo prof. Gustavo Guanabara e podem ser encontrados no site https://www.cursoemvideo.com/wp-content/uploads/2019/08/exercicios-algoritmos.pdf 

71) Faça um programa que preencha automaticamente um vetor numérico com 8 posições, conforme abaixo:
        999 999 999 999 999 999 999 999
        0   1   2   3   4   5   6   7 '''

print("Questão 71")
x = []
for i in range(8):
    x.append(999)
print(x)

''' 72) Crie um programa que preencha automaticamente (usando lógica, não apenas atribuindo diretamente) um vetor numérico com 10 posições, conforme abaixo:
        5 10 15 20 25 30 35 40 45 50
        0 1  2  3  4  5  6  7  8  9
 '''
print("\nQuestão 72")
y = []
j = 5
for i in range(10):
    y.append(j)
    j += 5
print(y)

''' 73) Crie um programa que preencha automaticamente (usando lógica, não apenas atribuindo diretamente) um vetor numérico com 10 posições, conforme abaixo:
        9 8 7 6 5 4 3 2 1 0
        0 1 2 3 4 5 6 7 8 9 '''

print("\nQuestão 73")
y = []
j = 9
for i in range(10):
    y.append(j)
    j -= 1
print(y)

''' 74) Crie um programa que preencha automaticamente (usando lógica, não apenas atribuindo diretamente) um vetor numérico com 10 posições, conforme abaixo:
        5 3 5 3 5 3 5 3 5 3
        0 1 2 3 4 5 6 7 8 9 '''

print("\nQuestão 74")
y = []
for i in range(10):
    if i % 2 == 0:
        y.append(5)
    else:
        y.append(3)
print(y)

''' 75) Crie um programa que preencha automaticamente (usando lógica, não apenas atribuindo diretamente) um vetor numérico com 15 posições com os primeiros elementos da sequência de Fibonacci:
        1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
        0 1 2 3 4 5 6  7  8  9  10 11  12  13  14  15 '''

print("\nQuestão 75")
num1 = 1
num2 = 0
y = []
for i in range(15):
    y.append(num1)
    num = num1 + num2
    num2 = num1
    num1 = num
print(y)