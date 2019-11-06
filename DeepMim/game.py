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


def getValidNextStrategies (board):
    """
    get an array of all possible strategy for a board
    Each Strategy is a tuple containing (numLine, nbMatches)

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

def humanMakeChoice(board):
    print ("entrez un num de ligne")
    line = int(input())
    print ("entrez un nb d'allumettes'")
    nbMatches = int(input())

    ok = False
    if isValidStrategy(line, nbMatches, board):
        ok=True
    while not ok:
        print ("Erreur ")
        print ("player", numJoueur, "make a choice")
        print ("entrez un num de ligne")
        line = int(input())
        print ("entrez un nb d'allumettes'")
        nbMatches = int(input())
        if isValidStrategy(line, nbMatches, board):
            ok=True

    return line, nbMatches

def IAMakeChoice(board):

    ## Il reste des allumette
    choices = getValidNextStrategies (board)

    maxResu = -2
    bestChoice = (0,0)

    known = {}
    for c in choices:
        line, nbMatches = c
        nboard = board.copy()
        drawMatches(line, nbMatches,nboard)
        resu = evaluate(nboard, False,0,known)

        if resu > maxResu:
            maxResu = resu
            bestChoice=c

        '''
        if IA and resu == 1:
            return 1
        if not IA and resu == -1:
            return -1
        '''
    if maxResu == 1:
        print ("je vais te piler")
    else :
        print ("Si tu joues bien, tu peux gagner")

    return bestChoice

def computeKey(tab):
    triee = sorted(tab, reverse=True)
    clef=0
    N = len(tab)
    for i in range(N):
        clef+= triee[i]*10**(N-i-1)

    return clef


def evaluate(board, IA,level,known):
    #print ("\t"*level,"evaluation de ", board)
    clef = computeKey(board)

    if clef in known:
        oldResu=known[clef]
        if IA:
            return oldResu
        else :
            return -oldResu

    if countMatches(board) == 0:
        known[clef]= 1
        if IA :
            return 1
        return -1

    ## Il reste des allumette
    choices = getValidNextStrategies (board)
    #print(choices)
    results =[]
    for c in choices:
        line, nbMatches = c
        #print ("\t"*level,"je teste ",line, nbMatches)
        nboard = board.copy()
        drawMatches(line, nbMatches,nboard)
        resu = evaluate(nboard, not IA,level+1,known)


        if IA and resu == 1:
            known[clef]=1
            return 1
        if not IA and resu == -1:
            known[clef]=1
            return -1

        #print ("\t"*level,"resu pour", nboard," :" , resu)
        results.append(resu)

    if IA :
        final= max(results)
    else :
        final = min(results)

    known[clef]=final
    return final


board = [7 , 5, 3, 1]
numJoueur = 0

#print ("avec ",board ,"j'aurais ce resultat", evaluate(board,False,0))
#print ("avec ",board ,"je joue ", IAMakeChoice(board))

IA = 0

while(not isFinished(board)):
        displayBoard(board)

        if numJoueur==IA:
            print ("IA Playing")
            line, nbMatches = IAMakeChoice(board)
            print ("IA retire",nbMatches,"on line",line)
        else :
            print ("player", numJoueur, "make a choice")
            line, nbMatches = humanMakeChoice(board)
            print ("Human player",numJoueur, "retire",nbMatches,"on line",line)

        drawMatches(line, nbMatches,board)

        numJoueur = changePlayer(numJoueur)

if numJoueur == IA:
    print ("IA gagne ")
else :
    print ("le joueur humain gagne")
# print ("Joueur",numJoueur,"Vous avez gagnÃ©")
