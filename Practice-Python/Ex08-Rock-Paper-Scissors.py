''' You can find this exercise at the following website: https://www.practicepython.org/

8. Rock Paper Scissors:

Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock '''

while True:
    print("-----ROCK PAPER SCISSORS-----")
    print()
    print("Enter the name of the player")
    name1 = input("Player 1: ")
    name2 = input("Player 2: ")
    print()
    print("Please type:\n 1. Rock\n 2. Paper\n 3. Scissors\n")

    choice1 = int(input("Player 1: "))
    while choice1 < 1 or choice1 > 3:
        print("Please type a number between 1 and 3")
        choice1 = int(input("Player 1: "))

    choice2 = int(input("Player 2: "))
    while choice2 < 1 or choice2 > 3:
        print("Please type a number between 1 and 3")
        choice2 = int(input("Player 2: "))
    print()

    if choice1 == choice2:
        print("It was a draw!")
    elif choice1 == 1 and choice2 == 2:
        print("Congratulations, " + name2 + "! Paper beats rock, you have won!")
    elif choice1 == 1 and choice2 == 3:
        print("Congratulations, " + name1 + "! Rock beats scissors, you have won!")
    elif choice1 == 2 and choice2 == 3:
        print("Congratulations, " + name2 + "! Scissors beats paper, you have won!")
    elif choice1 == 2 and choice2 == 1:
        print("Congratulations, " + name1 + "! Paper beats rock, you have won!")
    elif choice1 == 3 and choice2 == 1:
        print("Congratulations, " + name2 + "! Rock beats scissors, you have won!")
    else:
        print("Congratulations, " + name1 + "! Scissors beats paper, you have won!")

    print()
    playAgain = input("Would you like to play another game? [Y/N]\n")
    if playAgain == "Y":
        print()
        continue
    else:
        print("Game Over")
        break