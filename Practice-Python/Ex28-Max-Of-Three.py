''' You can find this exercise at the following website: https://www.practicepython.org/

Implement a function that takes as input three variables, and returns the largest of the three. Do this without using the Python max() function!

The goal of this exercise is to think about some internals that Python normally takes care of for us. All you need is some variables and if statements!
'''

def maxOfThree(x, y, z):
    if x > y and x > z:
        return "X is the largest: " +  str(x)
    elif z > y and z > x:
        return "Z is the largest: " +  str(z)
    else:
        return "Y is the largest: " +  str(y)

# Tests
print(maxOfThree(10, 15, 12))
print(maxOfThree(12, 10, 15))
print(maxOfThree(15, 10, 12))