''' Estes são os exercícios sugeridos durante as aulas do curso de Introdução a Algoritmos do prof. Gustavo Guanabara. Este curso pode ser encontrado no seguinte endereço: https://www.cursoemvideo.com/course/curso-de-algoritmo/

Aula 11 - Estruturas de Repetição 3

Exercício 01: Sequência de Fibonacci ''' 

# 15 primeiros termos da sequência

print("Exercício 01:\n")
x = 0
y = 1
for i in range(15):
    z = x + y
    print(x, end=" ")
    x = y
    y = z

''' Exercício 02: Analisador de valores '''

print()
print("\nExercício 02:\n")
soma = 0
div5 = 0
nulos = 0
somaPares = 0

for i in range(1, 6, 1):
    num = int(input("Digite o " + str(i) + "º valor: "))
    soma += num
    if num % 2 == 0:
        somaPares += num
    if num % 5 == 0:
        div5 += 1
    if num == 0:
        nulos += 1

media = soma / 5

print("\nA soma entre os valores é", soma)
print("A média entre os valores é", media)
print("Valores divisíveis por 5:", div5)
print("Valores nulos:", nulos)
print("A soma dos valores pares é", somaPares)