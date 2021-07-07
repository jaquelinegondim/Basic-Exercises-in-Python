''' Estes exercícios fazem parte do curso de Introdução a Algoritmos, ministrado pelo prof. Gustavo Guanabara e podem ser encontrados no site https://www.cursoemvideo.com/wp-content/uploads/2019/08/exercicios-algoritmos.pdf

    96) Crie um programa que tenha uma função Media(), que vai receber as 2 notas de um aluno e retornar a sua média para o programa principal. '''

print("Questão 96")

def Media(nota1, nota2):
    return (nota1 + nota2) / 2

nota1 = float(input("\nDigite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
print("Média:", Media(nota1, nota2))

''' 97) Refaça o exercício 91, só que agora em forma de função Maior(), mas faça uma adaptação que vai receber TRÊS números como parâmetro e vai retornar qual foi o maior entre eles. '''

print("\nQuestão 97")

def Maior(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    elif num3 >= num1 and num3 >= num2:
        return num3

num1 = float(input("\nDigite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))
print("O maior número digitado foi", Maior(num1, num2, num3))

''' 98) Crie um programa que tenha uma função SuperSomador(), que vai receber dois números como parâmetro e depois vai retornar a soma de todos os valores no intervalo entre os valores recebidos.
        Ex: SuperSomador(1, 6) vai somar 1 + 2 + 3 + 4 + 5 + 6 e vai retornar 21
            SuperSomador(15, 19) vai somar 15 + 16 + 17 + 18 + 19 e vai retornar 85 '''

print("\nQuestão 98")

def SuperSomador(inicio, fim):
    soma = 0
    for i in range(inicio, fim + 1, 1):
        soma += i
    return soma

inicio = int(input("\nDigite o valor inicial: "))
fim = int(input("Digite o valor final: "))
print("A soma dos valores contidos no intervalo fechado de [" + str(inicio) + ", " + str(fim) + "] é " + str(SuperSomador(inicio, fim)))

''' 99) Faça um programa que possua uma função chamada Potencia(), que vai receber dois parâmetros numéricos (base e expoente) e vai calcular o resultado da   exponenciação.
        Ex: Potencia(5,2) vai calcular 52 = 25  '''

print("\nQuestão 99")

def Potencia(base, expoente):
    exponenciacao = 1
    for i in range(expoente):
        exponenciacao *= base
    return exponenciacao

base = int(input("\nDigite o valor da base: "))
expoente = int(input("Digite o valor do expoente: "))
print("A exponenciação de " + str(base) + " elevado a " + str(expoente) + " é " + str(Potencia(base, expoente)))

''' 100) Melhore o exercício 96, criando além da função Media() uma outra função chamada Situacao(), que vai retornar para o programa principal se o aluno está APROVADO, em RECUPERAÇÃO ou REPROVADO. Essa nova função, vai receber como parâmetro o resultado retornado pela função Media() '''

print("\nQuestão 100")
def Situacao(resultado):
    if resultado > 7:
        return "APROVADO!"
    elif resultado >= 5:
        return "RECUPERAÇÃO"
    else:
        return "REPROVADO"

resultado = Media(nota1, nota2)
print("\nNota 1:", nota1)
print("Nota 2:", nota2)
print("O aluno está", Situacao(resultado))