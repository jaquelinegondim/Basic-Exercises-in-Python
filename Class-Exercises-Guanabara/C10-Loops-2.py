''' Estes são os exercícios sugeridos durante as aulas do curso de Introdução a Algoritmos do prof. Gustavo Guanabara. Este curso pode ser encontrado no seguinte endereço: https://www.cursoemvideo.com/course/curso-de-algoritmo/

Aula 10 - Estruturas de Repetição 2

Exercício 01: Super Contador '''

def Teste(choice):
    while True:
        if choice == 1 or choice == 2 or choice == 3:
            break
        else:
            print("Você precisa escolher um número entre 1 e 3.")
            choice = int(input("Digite sua escolha: "))
    return choice

while True:
    print("\n===============")
    print("|   M E N U   |")
    print("===============")
    print("| [1] 1 a 10  |")
    print("| [2] 10 a 1  |")
    print("| [3] Sair    |")
    print("===============")
    num = int(input("\nDigite sua escolha: "))
    num = Teste(num)
    if num == 1:
        for i in range(1, 11, 1):
            print(i, end=".. ")
    elif num == 2:
        for i in range(10, 0, -1):
            print(i, end=".. ")
    else:
        break
    print()

''' Exercício 02: Seletor de pessoas '''

def Check(choice):
    while True:
        if choice == "F" or choice == "M":
            break
        else:
            print("Você precisa escolher F para Feminino ou M para Masculino.")
            choice = input("Digite sua escolha: ")
    return choice

def Exit(choice):
    while True:
        if choice == "S" or choice == "N":
            break
        else:
            print("Você precisa escolher S para Sim ou N para Não.")
            choice = input("Digite sua escolha: ")
    return choice

def TesteCor(choice):
    while True:
        if choice == 1 or choice == 2 or choice == 3 or choice == 4:
            break
        else:
            print("Você precisa escolher um número entre 1 e 4.")
            choice = int(input("Digite sua escolha: "))
    return choice

homens = 0
mulheres = 0

while True:
    print("\n======================")
    print("| SELETOR DE PESSOAS |")
    print("======================")
    genero = input("\nQual é o seu gênero? [F/M] ")
    genero = Check(genero)
    idade = int(input("Qual é a sua idade? "))
    print("Qual é a cor do seu cabelo?")
    print("---------------------------")
    print("[1] Preto")
    print("[2] Castanho")
    print("[3] Loiro")
    print("[4] Ruivo")
    cor = int(input("\nDigite sua escolha: "))
    cor = TesteCor(cor)
    if genero == "M" and idade > 18 and cor == 2:
        homens += 1
    elif genero == "F" and idade >= 25 and idade <= 30 and cor == 3:
        mulheres += 1
    exit = input("Deseja continuar? [S/N] ")
    exit = Exit(exit)
    if exit == "N":
        break

print("\n-----------------------")
print("    Resultado Final    ")
print("-----------------------")
print("Total de homens com mais de 18 e cabelos castanhos:", homens)
print("Total de mulheres entre 25 e 30 e cabelos loiros:", mulheres)