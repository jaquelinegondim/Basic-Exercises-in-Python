''' Estes são os exercícios sugeridos durante as aulas do curso de Introdução a Algoritmos do prof. Gustavo Guanabara. Este curso pode ser encontrado no seguinte endereço: https://www.cursoemvideo.com/course/curso-de-algoritmo/

Aula 14 - Vetores

Exercício 01: Torneio de Futebol '''

# https://stackoverflow.com/questions/8356501/python-format-tabular-output
# from tabulate import tabulate

print("----------------------")
print("  TORNEIO DE FUTEBOL")
print("----------------------\n")
times = []
largura = 12
for i in range(1, 4, 1):
    times.append(input("Nome do " + str(i) + "° time: "))
print()
for i in times:
    for j in times:
        if i != j:
            print("{} [ ] X [ ] {}".format(i.ljust(largura), j.ljust(largura)))

# Formatação sem importar o tabulate
# print "{}| {}".format(item.ljust(width),bar(item).ljust(width))

''' Exercício 02: Corrigindo provas '''

print("\nPASSO 1: CADASTRO DE GABARITO")
print("-----------------------------")
gabarito = []
alunos = []
respostas = []
nota = 0
notas = []
for i in range(1, 6, 1):
    gabarito.append(input("Questão " + str(i) + ": "))

for i in range(1, 4, 1):
    print("\n-------------")
    print("   ALUNO " + str(i))
    print("-------------")
    alunos.append(input("Nome: "))
    print("\nRESPOSTAS DADAS")
    for j in range(1, 6, 1):
        respostas.append(input("Questão " + str(j) + ": "))
    for k in range(5):
        if respostas[k] == gabarito[k]:
            nota += 2
    notas.append(nota)
    nota = 0
    respostas = []

soma = 0
cont = 0
for i in notas:
    soma += i
    cont += 1
media = soma / cont

print("\n   NOTAS FINAIS")
print("------------------")
for j in range(3):
    print("{} {}".format(alunos[j].ljust(largura + 3), str(notas[j]).ljust(largura + 3)))

print("--------------------")
print("Média da turma: " + str(round(media, 2)))

''' Exercício 03: Reservar espaço no cinema '''

# Funções

# Checar se o número da reserva está entre 1 e 10
def Check(reserva):
    while True:
        if reserva < 1 or reserva > 10:
            print("Assento não existe. Escolha um número entre 1 e 10.")
            reserva = int(input("Reservar a cadeira: B"))
        else:
            break
    return reserva

# Checar se o assento está ocupado
def Teste(reserva):
    while True:
        if reservas[reserva - 1] == "---":
            print("Assento já está ocupado. Escolha outro.")
            reserva = int(input("Reservar a cadeira: B"))
            reserva = Check(reserva)
        else:
            reservas[reserva - 1] = "---"
            break

# Checar se quer reservar outro assento
def Continuar(escolha):
    while True:
        if escolha == "S" or escolha == "N":
            break
        else:
            print("Você precisa digitar S para Sim ou N para Não. Tente novamente.")
            escolha = input("Deseja continuar? [S/N] ")
    return escolha

reservas = ["B 1", "B 2", "B 3", "B 4", "B 5", "B 6", "B 7", "B 8", "B 9", "B10"]

print("\nRESERVAS NO CINEMA\n")

for i in range(10):
    print("[" + reservas[i] + "]", end=" ")
print("\n------------------------------------------------------------")

while True:
    cadeira = int(input("Reservar a cadeira: B"))
    cadeira = Check(cadeira)
    cadeira = Teste(cadeira)
    print()
    for i in range(10):
        print("[" + reservas[i] + "]", end=" ")
    print("\n------------------------------------------------------------")
    exit = input("Deseja continuar? [S/N] ")
    exit = Continuar(exit)
    if exit == "N":
        break