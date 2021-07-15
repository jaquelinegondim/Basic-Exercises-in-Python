''' Estes são os exercícios sugeridos durante as aulas do curso de Introdução a Algoritmos do prof. Gustavo Guanabara. Este curso pode ser encontrado no seguinte endereço: https://www.cursoemvideo.com/course/curso-de-algoritmo/

Aula 9 - Estruturas de Repetição 1

Exercício 01: Contagem Inteligente ''' 

print("CONTAGEM INTELIGENTE")
print("--------------------")
inicio = int(input("Início: "))
fim = int(input("Fim: "))
print("-------------------")
print("  C O N T A N D O")
print("-------------------")
if inicio > fim:
    for i in range(inicio, fim - 1, -1):
        print(str(i) + "..", end=" ")
else:
    for i in range(inicio, fim + 1, 1):
        print(str(i) + "..", end=" ")

''' Exercício 02: Melhor aluno da turma '''

print()
print("\n----------------------")
print("ESCOLA JAVALI CANSADO")
print("----------------------")
aluno = ""
maiorNota = 0
qtdAlunos = int(input("Quantos alunos a turma tem? "))
for i in range(1, qtdAlunos + 1, 1):
    print("----------------------")
    print("ALUNO", i)
    nome = input("Nome do aluno: ")
    nota = float(input("Nota de " + nome + ": "))
    if nota > maiorNota:
        maiorNota = nota
        aluno = nome
print("----------------------")
print("O melhor aproveitamento foi de", aluno, "com a nota", maiorNota)

# Para considerar casos em que haja empate na melhor nota, seria necessário criar e imprimir uma lista de nomes e notas.
# Ver questões 84 e 85 da lista de 100 exercícios que mostra um método para imprimir tabelas