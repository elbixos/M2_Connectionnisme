import player
import random
import numpy as np


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
nbGames = 1

p1=player.IADeepPlayer()
p2=player.IADeepPlayer()


for i in range(nbGames):

    board = [7 , 5, 3, 1]
    numJoueur = 0

    #print ("avec ",board ,"j'aurais ce resultat", evaluate(board,False,0))
    #print ("avec ",board ,"je joue ", IAMakeChoice(board))
    allBoards = []
    allBoards.append(sorted(board, reverse=True))


    draw = random.random()
    if draw <0.5:
        players=[p1,p2]
        IA=0
    else :
        players=[p2,p1]
        IA=1


    while(not isFinished(board)):
            line, nbMatches = players[numJoueur].makeChoice(board,train=True)
            drawMatches(line, nbMatches,board)
            numJoueur = changePlayer(numJoueur)
            allBoards.append(sorted(board, reverse=True))

    resu=-1
    if numJoueur == IA:
        victories+=1
        resu =1

    evals = []
    for i in range(len(allBoards)):

        if i%2 == IA:
            evals.append(resu)
        else:
            evals.append(-resu)


    if IA == 0:
        print ("je commence")
    else :
        print("l'autre commence")

    if resu == 1:
        print ("je gagne")
    else :
        print ("l'autre gagne")

    print ("J'ai appris ceci....")
    resu = players[IA].model.predict(np.asarray(allBoards))
    for i in range(len(allBoards)):
        print (allBoards[i],evals[i],resu[i])

    players[IA].trainOnce(allBoards,evals)

print ("IA wins in ",victories, "over ",nbGames)
