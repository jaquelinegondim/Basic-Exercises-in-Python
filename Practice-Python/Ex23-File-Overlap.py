''' You can find this exercise at the following website: https://www.practicepython.org/

Given two .txt files that have lists of numbers in them, find the numbers that are overlapping. One .txt file has a list of all prime numbers under 1000, and the other .txt file has a list of happy numbers up to 1000.

(If you forgot, prime numbers are numbers that can’t be divided by any other number. And yes, happy numbers are a real thing in mathematics - you can look it up on Wikipedia. The explanation is easier with an example, which I will describe below.)
 '''

def readFile(filename):
    with open(filename) as open_file:
        result = []
        line = open_file.read()
        for number in line.split('\n'):
            result.append(int(number))
    return result

primeNumbers = readFile("prime-numbers.txt")
happyNumbers = readFile("happy-numbers.txt")

overlap = [element for element in primeNumbers if element in happyNumbers]

print(overlap)

# You can use a function to remove duplicates from overlap if necessary - see exercise 14