''' You can find this exercise at the following website: https://www.practicepython.org/

15. Reverse Word Order:

Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. For example, say I type the string: My name is Michele

Then I would see the string: Michele is name My

shown back to me. '''

def reverse():
    words = input("Enter a set of words: ")
    division = words.split()
    backwards = division[::-1]
    final = " ".join(backwards)
    return("Words in reverse: " + str(final))

def reverse2(): # Solving in one line
    words = input("Enter a set of words: ")
    return("Words in reverse: " + str(" ".join(words.split()[::-1])))

def reverse3(): # Using reversed() built-in function
    words = input("Enter a set of words: ")
    return("Words in reverse: " + str(" ".join(reversed(words.split()))))

# List of built-in functions in python: https://www.w3schools.com/python/python_ref_functions.asp

print(reverse())
print(reverse2())
print(reverse3())