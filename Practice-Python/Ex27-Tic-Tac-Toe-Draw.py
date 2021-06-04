''' You can find this exercise at the following website: https://www.practicepython.org/

* Assume that player 1 (the first player to move) will always be X and player 2 (the second player) will always be O.

* Explain the coordinates: start from (1, 1) instead of (0, 0). To people who don’t program, starting to count at 0 is a strange concept, so it is better for the user experience if the row counts and column counts start at 1. This is not required, but whichever way you choose to implement this, it should be explained to the player.

* Ask the user to enter coordinates in the form “row,col” - a number, then a comma, then a number. Then you can use your Python skills to figure out which row and column they want their piece to be in.

* Don’t worry about checking whether someone won the game, but if a player tries to put a piece in a game position where there already is another piece, do not allow the piece to go there.

Bonus:

For the “standard” exercise, don’t worry about “ending” the game - no need to keep track of how many squares are full. In a bonus version, keep track of how many squares are full and automatically stop asking for moves when there are no more valid moves.
 '''


game = [[" ", " ", " "],
	    [" ", " ", " "],
	    [" ", " ", " "]]

# Function adapted from Practice Python solution to match my solution

def drawboard(board):
    print (' ' +str(board[0][0])+ ' | ' +str(board[0][1])+ ' | ' +str(board[0][2]) )
    print ('-----------')
    print (' ' +str(board[1][0])+ ' | ' +str(board[1][1])+ ' | ' +str(board[1][2]) )
    print ('-----------')
    print (' ' +str(board[2][0])+ ' | ' +str(board[2][1])+ ' | ' +str(board[2][2]) )


# My solution

counter = 0 # Count the number of coordinates that were filled

while counter < 9:

    print("Tic Tac Toe\nPlayer 1: X\nPlayer 2: O\n\nRows: 1, 2 or 3\nColumns: 1, 2 or 3\n")
    print("Enter your coordinates in the form of row, col. For example: 1, 2")

    # Variable player needs to be a list
    player = input("Type your coordinates here: ").replace(" ", "").split(",")

    # Check if the player gives coordinates inside the range
    while int(player[0]) < 1 or int(player[1]) < 1 or int(player[0]) > 3 or int(player[1]) > 3:
        print("The range of rows and columns varies from 1 to 3. Try again.")
        player = input("Type your coordinates here: ").replace(" ", "").split(",")

    # Check if coordinate is available and if it's the turn of player 1
    if game[int(player[0]) - 1][int(player[1]) - 1] == " " and counter % 2 == 0: 
        
        # Fill the coordinate with player 1 token (X)
        game[int(player[0]) - 1][int(player[1]) - 1] = "X"
        
        # Print player coordinates
        print("\nPlayer 1 coordinates: " + str(player[0] + ", " + player[1]) + "\n")
        
        # Print gameboard with the move
        drawboard(game)
        print()
        
        # Add 1 filled coordinate to the counter
        counter += 1

    # Repeat everything for player 2
    elif game[int(player[0]) - 1][int(player[1]) - 1] == " " and counter % 2 != 0: 
        game[int(player[0]) - 1][int(player[1]) - 1] = "O"
        print("\nPlayer 2 coordinates: " + str(player[0] + ", " + player[1]) + "\n")
        drawboard(game)
        print()
        counter += 1

    # Coordinate is not empty
    else:
        print("These coordinates are already taken, choose again.\n")

# Exit the loop
print("All coordinates were filled.")