''' You can find this exercise at the following website: https://www.practicepython.org/

14. List Remove Duplicates:

Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

Extras:

Write two different functions to do this - one using a loop and constructing a list, and another using sets.
Go back and do Exercise 5 using sets, and write the solution for that in a different function. '''

# First 100 values of Fibonacci Sequence
def Fibonacci():
    series = [1, 1]
    for i in range(2, 100):
        previous1 = series[i - 1]
        previous2 = series[i - 2]
        new = previous1 + previous2
        series.append(new)
    return(series)

# Uses list comprehensions
def removeDuplicates(original):
    unique = []
    [unique.append(n) for n in original if n not in unique]
    return(unique)

# Uses list, set, and sorted
def removeDuplicates2(original):
    return(list(sorted(set(original))))


firstHundred = Fibonacci()
print("First 100 values of Fibonacci sequence: ")
print(firstHundred)
print()
print("List above with no repetitions: ")
print(removeDuplicates2(firstHundred))
print()
