''' Estes exercícios fazem parte do curso de Introdução a Algoritmos, ministrado pelo prof. Gustavo Guanabara e podem ser encontrados no site https://www.cursoemvideo.com/wp-content/uploads/2019/08/exercicios-algoritmos.pdf

    81) Crie um programa que leia a idade de 8 pessoas e guarde-as em um vetor. No final, mostre:
        a) Qual é a média de idade das pessoas cadastradas
        b) Em quais posições temos pessoas com mais de 25 anos
        c) Qual foi a maior idade digitada (podem haver repetições)
        d) Em que posições digitamos a maior idade '''

print("Questão 81\n")
x = []
media = 0
position = []
position25 = []
for i in range(8):
    x.append(int(input("Digite sua idade: ")))
print("\nIdades inseridas:", x)
maiorIdade = max(x)
j = 0
k = 0
for i in x:
    media += i
    if i > 25:
        value = x.index(i, j) + 1 # posição de valores > 25
        position25.append(value) # add posição na lista
        j = value # alterando valor de j para que a função index conte a partir da posição seguinte
    if i == maiorIdade:
        place = x.index(i, k) + 1
        position.append(place)
        k = place

media = media / 8
print("Média das idades cadastradas:", media)
print("Posições com idades acima de 25 anos:", position25)
print("Maior idade digitada:", maiorIdade)
print("Posições com a maior idade:", position)

''' 82) Faça um algoritmo que leia a nota de 10 alunos de uma turma e guarde-as em um vetor. No final, mostre:
        a) Qual é a média da turma
        b) Quantos alunos estão acima da média da turma
        c) Qual foi a maior nota digitada
        d) Em que posições a maior nota aparece '''