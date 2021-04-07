''' You can find this exercise at the following website: https://www.practicepython.org/

4. Divisors:

Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.) '''


# Input
num = int(input("Enter a number: "))
print()

possibleDivisors = list(range(1, num + 1))
divisors = []

# Processing and Output
print("The divisor(s) for " + str(num) + " are:")
for element in possibleDivisors:
    if num % element == 0:
        divisors.append(element)
print(divisors)
print()

if len(divisors) == 2:
    print("It is a prime number!")
else:
    print("Total: " + str(len(divisors)) + " divisor(s).")