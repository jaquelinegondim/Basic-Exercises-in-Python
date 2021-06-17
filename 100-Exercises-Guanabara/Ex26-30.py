''' Estes exercícios fazem parte do curso de Introdução a Algoritmos, ministrado pelo prof. Gustavo Guanabara e podem ser encontrados no site https://www.cursoemvideo.com/wp-content/uploads/2019/08/exercicios-algoritmos.pdf 

    26) Escreva um algoritmo que leia dois números inteiros e compare-os, mostrando na tela uma das mensagens abaixo:
        - O primeiro valor é o maior
        - O segundo valor é o maior
        - Não existe valor maior, os dois são iguais
'''

print("Questão 26")
num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))
if num1 > num2:
    print("O número " + str(num1) + " é maior que o número " + str(num2) + ".")
elif num1 == num2:
    print("Os números são iguais.")
else:
    print("O número " + str(num2) + " é maior que o número " + str(num1) + ".")

''' 27) Crie um programa que leia duas notas de um aluno e calcule a sua média, mostrando uma mensagem no final, de acordo com a média atingida:
 - Média até 4.9: REPROVADO
 - Média entre 5.0 e 6.9: RECUPERAÇÃO
 - Média 7.0 ou superior: APROVADO '''

print("\nQuestão 27")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
if media < 5:
    print("REPROVADO")
elif media < 7:
    print("RECUPERAÇÃO")
else:
    print("APROVADO")

''' 28) Faça um programa que leia a largura e o comprimento de um terreno retangular, calculando e mostrando a sua área em m². O programa também
deve mostrar a classificação desse terreno, de acordo com a lista abaixo:
 - Abaixo de 100m² = TERRENO POPULAR
 - Entre 100m² e 500m² = TERRENO MASTER
 - Acima de 500m² = TERRENO VIP '''

print("\nQuestão 28")
largura = float(input("Digite a largura [m]: "))
comprimento = float(input("Digite o comprimento [m]: "))
area = round(largura * comprimento, 2)
if area < 100:
    print("TERRENO POPULAR")
elif area <= 500:
    print("TERRENO MASTER")
else:
    print("TERRENO VIP")

''' 29) Desenvolva um programa que leia o nome de um funcionário, seu salário, quantos anos ele trabalha na empresa e mostre seu novo salário, reajustado de acordo com a tabela a seguir:
 - Até 3 anos de empresa: aumento de 3%
 - entre 3 e 10 anos: aumento de 12.5%
 - 10 anos ou mais: aumento de 20% '''

print("\nQuestão 29")
nome = input("Digite o nome do funcionário: ")
salario = float(input("Digite o salário: R$"))
anos = int(input("Há quantos anos trabalha na empresa? "))
aumento = 0
if anos < 3:
    aumento = salario * 1.03
elif anos < 10:
    aumento = salario * 1.125
else:
    aumento = salario * 1.2
print("Novo salário: R$" + str(round(aumento, 2)))

''' 30) [DESAFIO] Refaça o algoritmo 25, acrescentando o recurso de mostrar que tipo de triângulo será formado:
 - EQUILÁTERO: todos os lados iguais
 - ISÓSCELES: dois lados iguais
 - ESCALENO: todos os lados diferentes '''

print("\nQuestão 30")
reta1 = float(input("Reta 1 [cm]: "))
reta2 = float(input("Reta 2 [cm]: "))
reta3 = float(input("Reta 3 [cm]: "))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print("É possível formar um triângulo!")
    if reta1 == reta2 == reta3:
        print("O triângulo é EQUILÁTERO")
    elif reta1 == reta2 or reta2 == reta3 or reta1 == reta3:
        print("O triângulo é ISÓCELES")
    else:
        print("O triângulo é ESCALENO")
else:
    print("Não é possível formar um triângulo!")