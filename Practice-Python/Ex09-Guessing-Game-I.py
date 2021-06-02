''' You can find this exercise at the following website: https://www.practicepython.org/

9. Guessing Game One:

Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out. '''

import random

exit = ""
while exit != "Y":
    num = random.randint(1, 9)
    guess = 0
    counter = 0
    print("-----GUESSING-GAME-----")
    print("Guess the secret number")
    print("It is a number between 1 and 9.")

    while guess!= num:
        guess = int(input("Enter your guess: "))
        counter += 1
        
        if guess > num:
            print("You guessed too high! Try again.")
        elif guess < num:
            print("You guessed too low! Try again")
        else:
            print("Congratulations!! You guessed the code!")
            print("You guessed " + str(counter) + " time(s)!")
        print()
    exit = input("Would you like to exit the game? [Y/N]\n")
    if exit == "Y":
        print("Game over!")
        break
    else:
        print()
        continue
    