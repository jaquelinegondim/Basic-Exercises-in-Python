''' You can find this exercise at the following website: https://www.practicepython.org/

11. Check Primality Functions

Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions, described below. '''

def primeNumber(num):
    # Creating a list of all possible divisors for the number
    possibleDivisors = list(range(1, num + 1))
    divisors = []
    print("The divisor(s) for " + str(num) + " are:")
    # Checking which element from that list is a divisor for num
    for element in possibleDivisors:
        if num % element == 0:
            divisors.append(element)
    print(divisors)
    print()
    # Checking the number of divisors to identify prime numbers
    if len(divisors) == 2:
        print("It is a prime number!")
    else:
        print("Total: " + str(len(divisors)) + " divisor(s).")
        print("It is not a prime number!")

print("-----CHECKING-DIVISORS-----")
print()
check = primeNumber(int(input("Enter a number: ")))