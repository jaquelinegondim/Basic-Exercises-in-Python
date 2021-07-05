''' Estes exercícios fazem parte do curso de Introdução a Algoritmos, ministrado pelo prof. Gustavo Guanabara e podem ser encontrados no site https://www.cursoemvideo.com/wp-content/uploads/2019/08/exercicios-algoritmos.pdf

    86) Crie um programa que tenha um procedimento Gerador() que, quando chamado, mostre a mensagem "Olá, Mundo!" com algum componente visual (linhas)
        Ex: Ao chamar Gerador() aparece:
        +-------=======------+
        Olá, Mundo!
        +-------=======------+ '''

print("Questão 86")
def Gerador():
    print("+-------=======------+")
    print("Olá, mundo!")
    print("+-------=======------+")
print()
Gerador()

''' 87) Crie um programa que melhore o procedimento Gerador() da questão anterior para que mostre uma mensagem personalizada, passada como parâmetro.
    Ex: Ao chamar Gerador("Aprendendo Portugol") aparece:
    +-------=======------+
    Aprendendo Portugol
    +-------=======------+ '''

print("\nQuestão 87")
def GeradorPersonalizado():
    frase = input("Que frase você quer exibir? ")
    print("\n+-------=======------+")
    print(frase)
    print("+-------=======------+")

GeradorPersonalizado()

''' 88) Crie um programa que melhore o procedimento Gerador() da questão anterior para que mostre uma mensagem várias vezes.
        Ex: Ao chamar Gerador("Aprendendo Portugol", 4) aparece:
        +-------=======------+
        Aprendendo Portugol
        Aprendendo Portugol
        Aprendendo Portugol
        Aprendendo Portugol
        +-------=======------+
        '''

print("\nQuestão 88")
def Gerador(frase, num):
    print("\n+-------=======------+")
    for i in range(num):
        print(frase)
    print("+-------=======------+")
Gerador("Olá, mundo!", 3)

''' 89) Crie um programa que melhore o procedimento Gerador() da questão anterior para que o programador possa escolher uma entre três bordas:
                                +-------=======------+ Borda 1
                                ~~~~~~~~:::::::~~~~~~~ Borda 2
                                <<<<<<<<------->>>>>>> Borda 3
        Ex: Uma chamada válida seria Gerador("Portugol Studio", 3, 2)
        ~~~~~~~~:::::::~~~~~~~
        Portugol Studio
        Portugol Studio
        Portugol Studio
        ~~~~~~~~:::::::~~~~~~~ '''

print("\nQuestão 89")

def repeticao(frase, num):
    for i in range(num):
        print(frase)

def Gerador(frase, num, borda):
    if borda == 1:
        print("+-------=======------+")
        repeticao(frase, num)
        print("+-------=======------+")
    elif borda == 2:
        print("~~~~~~~~:::::::~~~~~~~")
        repeticao(frase, num)
        print("~~~~~~~~:::::::~~~~~~~")
    elif borda == 3:
        print("<<<<<<<<------->>>>>>>")
        repeticao(frase, num)
        print("<<<<<<<<------->>>>>>>")

def check(choice):
    while True:
        if choice == 1 or choice == 2 or choice == 3:
            break
        else:
            print("\nVocê precisa escolher um número entre 1 e 3. Tente novamente!")
            print("\n+-------=======------+ Borda 1")
            print("~~~~~~~~:::::::~~~~~~~ Borda 2")
            print("<<<<<<<<------->>>>>>> Borda 3")
            choice = int(input("Escolha uma borda dentre as disponíveis: "))
    return choice

print("\n+-------=======------+ Borda 1")
print("~~~~~~~~:::::::~~~~~~~ Borda 2")
print("<<<<<<<<------->>>>>>> Borda 3")
borda = int(input("Escolha uma borda dentre as disponíveis: "))
borda = check(borda)
frase = input("Qual frase você quer exibir entre as bordas: ")
num = int(input("Escolha o número de repetições: "))
print()
Gerador(frase, num, borda)

''' 90) Desenvolva um algoritmo que leia dois valores pelo teclado e passe esses valores para um procedimento Somador() que vai calcular e mostrar a soma entre eles. '''

print("\nQuestão 90")
def Somador(num1, num2):
    print("A soma entre os números é", num1 + num2)
num1 = int(input("\nDigite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
Somador(num1, num2)