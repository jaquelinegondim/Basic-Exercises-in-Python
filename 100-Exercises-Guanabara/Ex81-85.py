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

print("\nQuestão 82\n")
x = []
media = 0
for i in range(10):
    nota = float(input("Qual a nota do aluno? "))
    x.append(nota)
    media += nota
media = media / 10
maiorNota = max(x)
excel = 0
k = 0
position = []
for i in x:
    if i > media:
        excel += 1
    if i == maiorNota:
        place = x.index(i, k) + 1
        position.append(place)
        k = place
print("\nTodas as notas:", x)
print("Média da turma:", round(media, 2))
print("Qtd de alunos acima da média:", excel)
print("Maior nota:", maiorNota) 
print("Posições em que a maior nota aparece:", position)

''' 83) [DESAFIO] Crie uma lógica que preencha um vetor de 20 posições com números aleatórios (entre 0 e 99) gerados pelo computador. Logo em seguida, mostre os números gerados e depois coloque o vetor em ordem crescente, mostrando no final os valores ordenados. '''

print("\nQuestão 83\n")
import random
vetor = []
for i in range(20):
    vetor.append(random.randint(0, 99))
print("Números gerados:", vetor)
print("Números ordenados:", sorted(vetor))

''' 84) Crie um programa que leia o nome e a idade de 9 pessoas e guarde esses valores em dois vetores, em posições relacionadas. No final, mostre uma listagem contendo apenas os dados das pessoas menores de idade. '''

print("\nQuestão 84\n")
# https://stackoverflow.com/questions/8356501/python-format-tabular-output
from tabulate import tabulate
nomes = []
idades = []
table = []
for i in range(9):
    nomes.append(input("Digite o seu nome: "))
    idades.append(int(input("Digite a sua idade: ")))
    if idades[i] < 18:
        table.append([nomes[i], idades[i]])
if table != []:
    print("\nPessoas menores de idade:")
    print(tabulate(table))

''' 85) Faça um algoritmo que leia o nome, o sexo e o salário de 5 funcionários e guarde esses dados em três vetores. No final, mostre uma listagem contendo apenas os dados das funcionárias mulheres que ganham mais de R$5 mil. '''

# Testando se o usuário digitou a letra correta 
def test(choice):
    while True:
        if choice == "F" or choice == "M":
            break
        else:
            print("Você precisa escolher F para Feminino ou M para Masculino. Tente de novo!")
            choice = input("Qual o seu gênero? [F/M] ")
    return choice

print("\nQuestão 85\n")
nome = []
genero = []
salario = []
table = []
for i in range(5):
    nome.append(input("Digite o seu nome: "))
    resposta = input("Qual o seu gênero? [F/M] ")
    resposta = test(resposta)
    genero.append(resposta)
    salario.append(float(input("Qual o seu salário? R$")))
    if genero[i] == "F" and salario[i] > 5000:
        table.append([nome[i], genero[i], "R$" + str(round(salario[i], 2))])
if table != []:
    print("\nNome | Gênero | Salário")
    print(tabulate(table))