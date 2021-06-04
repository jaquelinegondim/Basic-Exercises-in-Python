''' You can find this exercise at the following website: https://www.practicepython.org/

Your task this week: given a 3 by 3 list of lists that represents a Tic Tac Toe game board, tell me whether anyone has won, and tell me which player won, if any. A Tic Tac Toe win is 3 in a row - either in a row, a column, or a diagonal. Don’t worry about the case where TWO people have won - assume that in every board there will only be one winner.
'''

# My solution
def Winner(matrix):
    countDiagOne = 0
    countDiagTwo = 0
    transposed = []
    # checking rows
    for i in range(3):
        if matrix[i] == [1, 1, 1]:
            return "Winner is 1!"
            break
        elif matrix[i] == [2, 2, 2]:
            return "Winner is 2!"
            break
    # checking columns - see how to transpose a matrix without using list comprehension below
    for x in range(3):
        transposed.append([row[x] for row in matrix])
    for y in range(3):
        if transposed[y] == [1, 1, 1]:
            return "Winner is 1!"
            break
        elif transposed[y] == [2, 2, 2]:
            return "Winner is 2!"
            break
    # checking diagonals
    for j in range(3):
        if matrix[j][j] == 1:
            countDiagOne += 1
        elif matrix[j][j] == 2:
            countDiagTwo += 1
    if countDiagOne == 3:
        return "Winner is 1!"
    elif countDiagTwo == 3:
        return "Winner is 2!"
    else:
        return "There are no winners."

# Another solution:
def checkGrid(grid):

	# rows
	for x in range(3):
		row = set([grid[x][0],grid[x][1],grid[x][2]])
		if len(row) == 1 and grid[x][0] != 0:
			return grid[x][0]

	# columns
	for x in range(3):
		column = set([grid[0][x],grid[1][x],grid[2][x]])
		if len(column) == 1 and grid[0][x] != 0:
			return grid[0][x]

	# diagonals
	diag1 = set([grid[0][0],grid[1][1],grid[2][2]])
	diag2 = set([grid[0][2],grid[1][1],grid[2][0]])
	if len(diag1) == 1 or len(diag2) == 1 and grid[1][1] != 0:
		return grid[1][1]

	return 0

if __name__=="__main__":
    winner_is_2 = [[2, 2, 0],
	           [2, 1, 0],
	           [2, 1, 1]]

    winner_is_1 = [[1, 2, 0],
                [2, 1, 0],
                [2, 1, 1]]

    winner_is_also_1 = [[0, 1, 0],
                        [2, 1, 0],
                        [2, 1, 1]]

    no_winner = [[1, 2, 0],
                [2, 1, 0],
                [2, 1, 2]]

    also_no_winner = [[1, 2, 0],
                    [2, 1, 0],
                    [2, 1, 0]]

    print(Winner(winner_is_2))
    print(Winner(winner_is_1))
    print(Winner(winner_is_also_1))
    print(Winner(no_winner))
    print(Winner(also_no_winner))
    print(checkGrid(winner_is_2))
    print(checkGrid(winner_is_1))
    print(checkGrid(winner_is_also_1))
    print(checkGrid(no_winner))
    print(checkGrid(also_no_winner))

''' How to transpose a matrix without using list comprehension:

    for i in range(3):

        # the following 3 lines implement the nested listcomp

        transposed_row = []

        for row in matrix: # First row

            transposed_row.append(row[i]) # First column of first row, then second row, then third row

        transposed.append(transposed_row) # Now i = 1 and we move on to the second column'''