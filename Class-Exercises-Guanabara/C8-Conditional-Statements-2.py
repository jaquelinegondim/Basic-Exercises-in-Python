''' Estes são os exercícios sugeridos durante as aulas do curso de Introdução a Algoritmos do prof. Gustavo Guanabara. Este curso pode ser encontrado no seguinte endereço: https://www.cursoemvideo.com/course/curso-de-algoritmo/

Aula 8 - Estruturas Condicionais 2 

Exercício 01: Aproveitamento de um aluno'''

print("----------------------")
print("ESCOLA JAVALI CANSADO")
print("----------------------")
nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
print("----------------------")
media = (nota1 + nota2) / 2
print("MEDIA: ", media)
if media >= 9:
    print("APROVEITAMENTO: A")
elif media >= 8:
    print("APROVEITAMENTO: B")
elif media >= 7:
    print("APROVEITAMENTO: C")
elif media >= 6:
    print("APROVEITAMENTO: D")
elif media >= 5:
    print("APROVEITAMENTO: E")
else:
    print("APROVEITAMENTO: F")
print("----------------------\n")

''' Exercício 02: Uma partida de futebol '''

print("\nBANGU X MADUREIRA")
print("--------------------")
golBangu = int(input("Quantos gols do BANGU? "))
golMadureira = int(input("Quantos gols do MADUREIRA? "))
print("--------------------")
diferenca = abs(golBangu - golMadureira)
print("DIFERENÇA:", diferenca)
if diferenca == 0:
    print("STATUS: EMPATE")
elif diferenca <= 3:
    print("STATUS: PARTIDA NORMAL")
else:
    print("STATUS: GOLEADA")