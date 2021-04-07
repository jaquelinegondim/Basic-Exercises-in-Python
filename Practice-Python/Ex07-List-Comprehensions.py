''' You can find this exercise at the following website: https://www.practicepython.org/

7. List Comprehensions:

Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it. '''

import random
num1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
num2 = random.sample(range(0, 101), 15)
print("List 1: " + str(num1))
print("Even numbers in List 1: " + str([element for element in num1 if element % 2 == 0]))
print()
print("List 2: " + str(num2))
print("Even numbers in List 2: " + str([element for element in num2 if element % 2 == 0]))
