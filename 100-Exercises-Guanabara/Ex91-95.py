''' Estes exercícios fazem parte do curso de Introdução a Algoritmos, ministrado pelo prof. Gustavo Guanabara e podem ser encontrados no site https://www.cursoemvideo.com/wp-content/uploads/2019/08/exercicios-algoritmos.pdf

    91) Desenvolva um algoritmo que leia dois valores pelo teclado e passe esses valores para um procedimento Maior() que vai verificar qual deles é o maior e mostrá-lo na tela. Caso os dois valores sejam iguais, mostrar uma mensagem informando essa característica. '''

print("Questão 91")

def Maior(num1, num2):
    if num1 > num2:
        print(num1, "é maior que", num2)
    elif num2 > num1:
        print(num2, "é maior que", num1)
    else:
        print("Os números são iguais")

num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
Maior(num1, num2)

''' 92) Crie uma lógica que leia um número inteiro e passe para um procedimento ParOuImpar() que vai verificar e mostrar na tela se o valor passado como parâmetro é PAR ou ÍMPAR. '''

print("\nQuestão 92")
def ParOuImpar(num):
    if num % 2 == 0:
        print("O número é PAR.")
    else:
        print("O número é ÍMPAR.")

num = int(input("Digite um número inteiro: "))
ParOuImpar(num)

''' 93) Faça um programa que tenha um procedimento chamado Contador() que recebe três valores como parâmetro: o início, o fim e o incremento de uma contagem. O programa principal deve solicitar a digitação desses valores e passá-los ao procedimento, que vai mostrar a contagem na tela.
        Ex: Para os valores de início (4), fim (20) e incremento(3) teremos
        Contador(4, 20, 3) vai mostrar na tela 4 >> 7 >> 10 >> 13 >> 16 >> 19 >> FIM
 '''

print("\nQuestão 93")
def Contador(inicio, fim, passo):
    for i in range(inicio, fim + 1, passo):
        print(i, end=" >> ")
    print("FIM")

inicio = int(input("Digite o início da contagem: "))
fim = int(input("Digite o fim da contagem: "))
passo = int(input("Digite o passo da contagem: "))
Contador(inicio, fim, passo)

''' 94) [DESAFIO] Desenvolva um aplicativo que tenha um procedimento chamado Fibonacci() que recebe um único valor inteiro como parâmetro, indicando quantos termos da sequência serão mostrados na tela. O seu procedimento deve receber esse valor e mostrar a quantidade de elementos solicitados.
        Obs: Use os exercícios 70 e 75 para te ajudar na solução
        Ex: Fibonacci(5) vai gerar 1 >> 1 >> 2 >> 3 >> 5 >> FIM
            Fibonacci(9) vai gerar 1 >> 1 >> 2 >> 3 >> 5 >> 8 >> 13 >> 21 >> 34 >> FIM '''

print("\nQuestão 94")
def Fibonacci(termos):
    x = 1
    y = 1
    for i in range(termos):
        print(x, end=" >> ")
        aux = x + y
        x = y
        y = aux
    print("FIM")

termos = int(input("Quantos termos você deseja ter na sequência de Fibonacci? "))
Fibonacci(termos)

''' 95) Refaça o exercício 90, só que agora em forma de função Somador(), que vai receber dois parâmetros e vai retornar o resultado da soma entre eles para o programa principal. '''

print("\nQuestão 95")
def Somador(x, y):
    return x + y

x = float(input("Digite o valor de x: "))
y = float(input("Digite o valor de y: "))
print("A soma entre x e y é", Somador(x, y))