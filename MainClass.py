from ReadBoard import ReadBoard
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

if(board[9] == 'Moves'):
    for i in range(0, 8):
        for j in range(0, 8):
            validMove = ValidMove(i, j, board)
            if(board[i][j] == 'O'):
                calWhiteMove = validMove.calMoves()
            elif(board[i][j] == '@'):            
                calBlackMove = validMove.calMoves()
            else:
                continue

    print(calWhiteMove)
    print(calBlackMove)

else:
    elimMove = MakeMoves()
    fuck this shit, im out of fuking options
