def displayBoard(board) :
        """
        display the board
        """
        for i in range(len(board)) :
            print(i + 1,":  ", end="")
            for j in range(board[i]) :
                print("I", end = "")
            print("")


def drawMatches (line, nbMatches,board):
    """
    Draw some matches on the current board.

    It check if the proposal is valid.
    """
    if (isValidStrategy(line, nbMatches,board)) :
        board[line]-=nbMatches
    else :
        print ("You tried something bad")

def isFinished (board):
    """
    Tell if the game is finished or not
    (finished if no matches remains)
    """
    if countMatches(board) == 0:
        return True
    return False


def countMatches (board):
    """
    Count matches on the board
    """

    nbAll =0
    for ligne in board:
        if ligne >= 0:
            nbAll+=ligne
    return nbAll

def isValidStrategy (line, nbMatches, board):
    """
    test if a strategy is valid for the current state of the Board

    One could ask if a strategy is valid for a different board. If so,
    pass the board as a parameter
    """
    if (line < 0 or line >=4):
        return False

    if nbMatches < 1 or nbMatches >3 :
        return False

    if board[line]-nbMatches < 0:
        return False

    return True


def getValidNextStrategies (board):
    """
    get an array of all possible strategy for the current state of the Board
    Each Strategy is a tuple containing (numLine, nbMatches)

    One could ask the ValidStrategies for a different board. If so,
    pass the board as a parameter
    """

    strategies = []
    for nbMatches in [1,2,3]:
        for line in [0,1,2,3]:
            if board[line] - nbMatches >= 0 :
                strategies.append((line, nbMatches))

    return strategies

def changePlayer(numJoueur):
    numJoueur = (numJoueur+1)%2
    return numJoueur


board = [7 , 5, 3, 1]
numJoueur = 0

print (getValidNextStrategies(board))
displayBoard(board)
