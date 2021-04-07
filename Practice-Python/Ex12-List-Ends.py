''' You can find this exercise at the following website: https://www.practicepython.org/

12. List Ends:

Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function. '''

def randomList(start, end, size):
    import random
    return random.sample(range(start, end), size)

def listEnds(test):
    endElements = []
    endElements.append(test[0])
    endElements.append(test[-1])
    print("List: " + str(test))
    print("The first and last elements of the list are: " + str(endElements))

# Another way to set the funcion listEnds:
''' def listEnds(test):
    return [test[0], test[len(test) - 1]] '''

print("-----LIST-ENDS-----")
print()
a = randomList(1, 101, 10)
b = listEnds(a)