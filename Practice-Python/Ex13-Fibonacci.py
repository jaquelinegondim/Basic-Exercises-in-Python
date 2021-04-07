''' You can find this exercise at the following website: https://www.practicepython.org/

13. Fibonacci:

Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, ...) '''

# First solution adapted from Gustavo Guanabara's course of Algorithms (Aula 12)

def Fibonacci(num):
    a = 0
    b = 1
    if num == 0:
        print("Enter a number greater than zero to generate values.")
    elif num == 1:
        print(a, end = " ")
    elif num == 2:
        print(a, end = " ")
        print(b, end = " ")
    else:
        print(a, end = " ")
        print(b, end = " ")
        for i in range(num - 2):
            c = a + b
            print(c, end = " ")
            i += 1
            a = b
            b = c
        

print("---------FIBONACCI--SEQUENCE--GENERATOR---------")
number = int(input("How many values would you like in your sequence? "))
print("Here is your Fibonacci sequence with " + str(number) + " terms.")
Fibonacci(number)

# Another way to solve by using lists:

''' def fibonacci():
    num = int(input("How many numbers that generates?:"))
    i = 1
    if num == 0:
        fib = []
    elif num == 1:
        fib = [1]
    elif num == 2:
        fib = [1,1]
    elif num > 2:
        fib = [1,1]
        while i < (num - 1):
            fib.append(fib[i] + fib[i-1])
            i += 1
    return fib 
print(fibonacci()) '''