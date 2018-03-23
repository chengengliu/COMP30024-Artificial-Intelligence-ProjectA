#from ReadBoard import ReadBoard
from ValidMove import ValidMove

print("Enter the input, Ctrl+X to end:")
board = []
n = 0
while True:
    try:
         line = input()
    except EOFError:
        break
    board.append(line)
print(board)
#这里range应该是0 到7 
if(board[8] == 'Moves'):
    for i in range(0, 7):
        for j in range(0, 7):
            validMove = ValidMove(i, j, board)
            if(board[i][j] == 'O'):
                print ('I J ', i, j,"\n")
                calWhiteMove = validMove.calMoves()
            elif(board[i][j] == '@'):   
                        
                calBlackMove = validMove.calMoves()
            else:
                continue

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
