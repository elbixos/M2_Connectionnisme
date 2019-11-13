import player
import random

aplayer = player.IAMinMaxPlayer()


board = [7,5,3,1]

print (board)
print("player turn", aplayer.evaluate(board,True,0,{}))
print("other  turn", aplayer.evaluate(board,False,0,{}))


board = [0,0,2,2]

print (board)
print("=======player  turn==========")
known = {}
print("Resu", aplayer.evaluate(board,True,0,known))
print(known)
print("=======other  turn==========")
known = {}
print("Resu",aplayer.evaluate(board,False,0,known))
print(known)


board = [0,0,0,1]

print (board)
print("=======player  turn==========")
known = {}
print("Resu", aplayer.evaluate(board,True,0,known))
print(known)
print("=======other  turn==========")
known = {}
print("Resu",aplayer.evaluate(board,False,0,known))
print(known)
