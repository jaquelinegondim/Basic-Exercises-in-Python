''' You can find this exercise at the following website: https://www.practicepython.org/

10. List Overlap Comprehensions:

This week’s exercise is going to be revisiting an old exercise (see Exercise 5), except require the solution in a different way.

Take two lists, say for example these two:

	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

Extra:
Randomly generate two lists to test this '''

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
resultRepetitions = [element for element in a if element in b]

noRepetitions = []
for i in resultRepetitions:
    if i not in noRepetitions:
        noRepetitions.append(i) 

# Same thing in one line:
# [noRepetitions.append(i) for i in resultRepetitions if i not in noRepetitions]

# See Exercise 14 for functions to remove duplicates!

print("List 1: " + str(a))
print("List 2: " + str(b))
print("List of numbers in both lists with repetitions:" + str(resultRepetitions))
print("List of numbers in both lists without repetitions:" + str(noRepetitions))

# To see how to randomly generate lists, refer to exercise 5 - List Overlap