''' Estes exercícios fazem parte do curso de Introdução a Algoritmos, ministrado pelo prof. Gustavo Guanabara e podem ser encontrados no site https://www.cursoemvideo.com/wp-content/uploads/2019/08/exercicios-algoritmos.pdf 

    56) Crie um programa que leia vários números pelo teclado e mostre no final o somatório entre eles.
        Obs: O programa será interrompido quando o número 1111 for digitado '''

print("Questão 56")
num = 0
sum = 0
print("\nDigite números inteiros para calcular o seu somatório.\nO programa será interrompido quando o número 1111 for digitado.\n")
while num != 1111:
    num = int(input("Digite um número inteiro: "))
    if num == 1111:
        break
    else:
        sum += num
print("Somatório:", sum)

''' 57) Desenvolva um aplicativo que leia o salário e o sexo de vários funcionários. No final, mostre o total de salários pagos aos homens e o total pago às mulheres. O programa vai perguntar ao usuário se ele quer continuar ou não sempre que ler os dados de um funcionário. '''

# Testando se o usuário digitou a letra correta 
def test(choice):
    while True:
        if choice == "F" or choice == "M":
            break
        else:
            print("Você precisa escolher F para Feminino ou M para Masculino. Tente de novo!")
            choice = input("Qual o seu gênero? [F/M] ")
    return choice

# Testando se o usuário digitou a letra correta
def exit(choice):
    while True:
        if choice == "S" or choice == "N":
            break
        else:
            print("Você precisa escolher S para Sim ou N para Não. Tente de novo!")
            choice = input("Você deseja incluir novos dados? [S/N] ")
    return choice

print("\nQuestão 57")
answer = ""
men = 0
women = 0
while answer != "N":
    wage = float(input("Digite o salário: R$"))
    gender = input("Digite o seu gênero [F/M]: ")
    gender = test(gender)
    if gender == "F":
        women += wage
    else:
        men += wage
    answer = input("Você deseja incluir novos dados? [S/N] ")
    answer = exit(answer)
print("\nTotal pago aos homens:", men)
print("Total pago às mulheres:", women)

''' 58) Faça um algoritmo que leia a idade de vários alunos de uma turma. O programa vai parar quando for digitada a idade 999. No final, mostre quantos alunos existem na turma e qual é a média de idade do grupo. '''

print("\nQuestão 58")
num = 0
sum = 0
media = 0
print("\nDigite a idade dos alunos da turma.\nO programa será interrompido quando a idade 999 for digitada.\n")
while num != 999:
    num = int(input("Digite a idade do aluno: "))
    if num == 999:
        break
    else:
        media += num
        sum += 1
print("Total de alunos:", sum)
print("Média da idade:", round((media / sum), 2))

''' 59) Crie um programa que leia o sexo e a idade de várias pessoas. O programa vai perguntar se o usuário quer continuar ou não a cada pessoa. No final, mostre:
    a) qual é a maior idade lida
    b) quantos homens foram cadastrados
    c) qual é a idade da mulher mais jovem
    d) qual é a média de idade entre os homens '''

print("\nQuestão 59")
answer = ""
men = 0
avgMen = 0
maxAge = 0
youngerWomen = []
while answer != "N":
    age = int(input("Digite sua idade: "))
    if age > maxAge:
        maxAge = age
    gender = input("Digite o seu gênero [F/M]: ")
    gender = test(gender)
    if gender == "F":
        youngerWomen.append(age)
    else:
        men += 1
        avgMen += age
    answer = input("Você deseja incluir novos dados? [S/N] ")
    answer = exit(answer)
print("Maior idade:", maxAge)
print("Total de homens:", men)
print("Mulher mais jovem:", min(youngerWomen), "anos")
print("Média de idade dos homens:", round((avgMen / men), 2))

''' 60) Desenvolva um algoritmo que leia o nome, a idade e o sexo de várias pessoas. O programa vai perguntar se o usuário quer ou não continuar. No final, mostre:
    a) O nome da pessoa mais velha
    b) O nome da mulher mais jovem
    c) A média de idade do grupo
    d) Quantos homens tem mais de 30 anos
    e) Quantas mulheres tem menos de 18 anos '''

print("\nQuestão 60")
nomePessoas = []
idadePessoas = []
nomeMulheres = []
idadeMedia = 0
idadeMulheres = []
homens30 = 0
mulheres18 = 0
answer = ""
pessoas = 0
while answer != "N":
    nome = input("Digite seu nome: ")
    nomePessoas.append(nome)
    idade = int(input("Digite sua idade: "))
    idadePessoas.append(idade)
    idadeMedia += idade
    pessoas += 1
    gender = input("Digite o seu gênero [F/M]: ")
    gender = test(gender)
    if gender == "F":
        idadeMulheres.append(idade)
        nomeMulheres.append(nome)
        if idade < 18:
            mulheres18 += 1
    else:
        if idade > 30:
            homens30 += 1
    answer = input("Você deseja incluir novos dados? [S/N] ")
    answer = exit(answer)

print("\nNome da pessoa mais velha:", nomePessoas[idadePessoas.index(max(idadePessoas))])
print("Nome da mulher mais jovem:", nomeMulheres[idadeMulheres.index(min(idadeMulheres))])
print("Média de idade do grupo:", round((idadeMedia / pessoas), 2))
print("Homens com mais de 30 anos:", homens30)
print("Mulheres com menos de 18 anos:", mulheres18)