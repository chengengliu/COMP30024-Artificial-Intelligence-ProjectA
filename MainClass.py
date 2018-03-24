#from ReadBoard import ReadBoard
from ValidMove import ValidMove

print("Enter the input, Ctrl+X to end:")
board = []
n = 0
totalValidMoves = 0

while True:
    try:
         line = input()
    except EOFError:
        break
    board.append(line)



print(board)

if(board[8] == 'Moves'):
    for i in range(0, 8):
        for j in range(0, 8):
            #print (i)
            #print (j)
            validMove = ValidMove(i, j, board)
            #print (validMove)
            if(board[i][j] == 'O'):
                print ('白棋坐标，I J ', i, j,"\n")
                calWhiteMove = validMove.calMoves()
                totalValidMoves += calWhiteMove
            if(board[i][j] == '@'):   

                print ('黑棋坐标 I J', i, j, "\n")
                        
                calBlackMove = validMove.calMoves()
                totalValidMoves+=calBlackMove
            else:
                continue

print (totalValidMoves)

#print(calWhiteMove)
#print(calBlackMove)
'''
else:
    elimMove = MakeMoves()'''

'''
X------X 
-------- 
-----O-- 
----@O-- 
------O- 
-----O@- 
-------@ 
X------X
Moves'''
