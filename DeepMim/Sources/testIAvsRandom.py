import player
import random

def displayBoard(board) :
        """
        display the board
        """
        for i in range(len(board)) :
            print(i ,":  ", end="")
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

def changePlayer(numJoueur):
    numJoueur = (numJoueur+1)%2
    return numJoueur


victories=0
nbGames = 100

for i in range(nbGames):

    board = [7 , 5, 3, 1]
    numJoueur = 0

    #print ("avec ",board ,"j'aurais ce resultat", evaluate(board,False,0))
    #print ("avec ",board ,"je joue ", IAMakeChoice(board))


    p1=player.IADeepPlayer()
    p2=player.IARandomPlayer()

    draw = random.random()
    if draw <0.5:
        players=[p1,p2]
        IA=0
    else :
        players=[p2,p1]
        IA=1


    while(not isFinished(board)):
            line, nbMatches = players[numJoueur].makeChoice(board)
            drawMatches(line, nbMatches,board)
            numJoueur = changePlayer(numJoueur)

    if numJoueur == IA:
        victories+=1

print ("IA wins in ",victories, "over ",nbGames)
