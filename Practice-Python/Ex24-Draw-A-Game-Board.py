''' You can find this exercise at the following website: https://www.practicepython.org/

Time for some fake graphics! Let’s say we want to draw game boards that look like this:

 --- --- --- 
|   |   |   | 
 --- --- ---  
|   |   |   | 
 --- --- ---  
|   |   |   | 
 --- --- --- 
This one is 3x3 (like in tic tac toe). Obviously, they come in many other sizes (8x8 for chess, 19x19 for Go, and many more).

Ask the user what size game board they want to draw, and draw it for them to the screen using Python’s print statement.
 '''

# My solution
def GameBoard(size):
    for x in range(size):
        for i in range(size - 1):
            print(" ---", end = "")
        print(" ---", end = "\n")
        for j in range(size):
            print("|   ", end = "")
        print("|   ", end = "\n")
    for k in range(size - 1):
        print(" ---", end = "")
    print(" ---", end = "\n")

# Easier solution
def HorizLine():
    return(" ---" * choice)

def VertLine():
    return("|   " * (choice + 1))

if __name__=="__main__":
    choice = int(input("What size game board would you like to draw? Type an integer greater than 0: "))
    print(" ")
    # Calling my solution
    GameBoard(choice)
    # Calling easier solution:
    ''' for i in range(choice):
        print(HorizLine())
        print(VertLine())
    print(HorizLine()) '''