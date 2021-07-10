''' Estes são os exercícios sugeridos durante as aulas do curso de Introdução a Algoritmos do prof. Gustavo Guanabara. Este curso pode ser encontrado no seguinte endereço: https://www.cursoemvideo.com/course/curso-de-algoritmo/

Aula 7 - Estruturas Condicionais 1

Exercício 01: Está apto a dirigir? '''

print("-------------------------")
print("DEPARTAMENTO DE TRANSITO")
print("-------------------------")
anoAtual = int(input("Ano atual (yyyy): "))
anoNascimento = int(input("Ano de nascimento (yyyy): "))
idade = anoAtual - anoNascimento
print("\n----------STATUS----------")
print("IDADE:", idade, "ANOS")
if idade > 18:
    print("APTO A TIRAR A CARTEIRA")
else:
    print("INAPTO A TIRAR A CARTEIRA")
print("--------------------------\n")

''' Exercício 02: Aluno aprovado ou reprovado? '''

print("\n----------------------")
print("ESCOLA JAVALI CANSADO")
print("----------------------")
nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
print("----------------------")
media = (nota1 + nota2) / 2
print("MEDIA: ", media)
if media >= 7:
    print("ALUNO APROVADO")
else:
    print("ALUNO REPROVADO")
print("----------------------")