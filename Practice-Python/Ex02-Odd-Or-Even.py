''' You can find this exercise at the following website: https://www.practicepython.org/

2. Odd or Even:

Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message. '''

number = int(input("Enter a number: "))

if number % 4 == 0 and number != 0:
    print("The number is even and it is a multiple of 4.")
else:
    if number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")
print()

num = int(input("Enter a numerator: "))
check = int(input("Enter a denominator: "))

if check == 0:
    print("A number cannot be divided by zero!")
else:
    if num % check == 0:
        print("The numerator is divisible by the denominator.")
    else:
        print("The numerator is not divisible by the denominator.")