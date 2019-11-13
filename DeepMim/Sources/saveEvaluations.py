import player
import random
import csv

def key2board(key):
    board = []
    for i in range(4):
        temp = int(key/(10**(4-i-1)))
        board.append(temp%10)
    return board


aplayer = player.IAMinMaxPlayer()


board = [7,5,3,1]

print (board)

known = {}
print("Resu", aplayer.evaluate(board,True,0,known,prune=False))
print("nbKeys",len(known))
#print(known)

f = open('evalMim.csv', 'w')

with f:
    writer = csv.writer(f)

    for key in known:
        board = key2board(key)
        value = known[key]
        board.append(value)
        #chaine=",".join(map(str, board))
        #print(chaine)
        writer.writerow(board)
