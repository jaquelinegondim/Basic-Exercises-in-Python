''' You can find this exercise at the following website: https://www.practicepython.org/

5. List Overlap:

Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

Extras:

Randomly generate two lists to test this
Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon) '''

# Input
import random
num2 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
num1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# num1 = random.sample(range(1, 100), 11)
# num2 = random.sample(range(1, 100), 13)
result = []

print("List 1: " + str(num1))
print("List 2: " + str(num2))
print()

# Processing and output
for element in num2:
    if element in num1:
        result.append(element)

# Function using set, list, and sorted
def noRepetitions(x, y):
    noRep1 = list(sorted(set(x)))
    noRep2 = list(sorted(set(y)))
    return [i for i in noRep1 if i in noRep2]

print("List of numbers in both lists:" + str([element for element in num2 if element in num1])) # Solution in one line
print("List of numbers in both lists:" + str(result))
print("List of numbers in both lists:" + str(noRepetitions(num2, num1)))

