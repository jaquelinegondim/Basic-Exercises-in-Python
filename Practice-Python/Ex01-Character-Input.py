''' You can find this exercise at the following website: https://www.practicepython.org/

1. Character Input

Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:

Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button) '''

name = input("Enter your name: ")
age = int(input("Enter your age: "))
number = int(input("Enter a number between 1 and 10: "))
print()

from datetime import date
currentYear = date.today().year
answer = currentYear - age + 100
print(number * ("Hi, " + name + "! You will be 100 yrs old in " + str(answer) + "!\n"))