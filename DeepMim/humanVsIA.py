import player

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



board = [7,5,3,1]
numJoueur = 0

#print ("avec ",board ,"j'aurais ce resultat", evaluate(board,False,0))
#print ("avec ",board ,"je joue ", IAMakeChoice(board))
known = {}
IA = 0
players=[]
players.append(player.IAMinMaxPlayer())
players.append(player.HumanPlayer())

while(not isFinished(board)):
        displayBoard(board)

        if IA==numJoueur:
            print ("IA Playing")
        else :
            print ("player", numJoueur, "make a choice")

        line, nbMatches = players[numJoueur].makeChoice(board)
        print ("Le joueur retire",nbMatches,"on line",line)

        drawMatches(line, nbMatches,board)

        numJoueur = changePlayer(numJoueur)

if numJoueur == IA:
    print ("IA gagne ")
else :
    print ("le joueur humain gagne")
# print ("Joueur",numJoueur,"Vous avez gagnÃ©")
