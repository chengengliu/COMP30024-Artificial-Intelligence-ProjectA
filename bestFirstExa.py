from collections import deque
import copy
import math

OBSTACLE_COL = ["@", "O", "X"]

class BoardAnalyser():
    def __init__(self, board):
        self.board = board
        self.whitePieces = []
        self.blackPieces = []
        self.whiteMoves = 0
        self.blakcMoves = 0
    def readBoard(self):
        #print (self.board)
        for i in range(0,8):
            for j in range(0,8):
                #print (len(board))
                #print (board[i][j])
                if(self.board[i][j] == 'O'):
                    #print (self.board[i][j])
                    self.whitePieces.append([i,j])
                    #print (self.whitePieces)
                if(self.board[i][j] == '@'):
                    self.blackPieces.append([i,j])
        #print (self.whitePieces)
        return self.whitePieces, self.blackPieces

    def analyseMoves(self):
        if board[8] == 'Moves':
            #print (board)
            for i in range(0,8):
                for j in range(0,8):
                    #dict[(i,j)] = board[i][j]
                    validMove = ValidMove(i, j, board)
                    #print (validMove)
                    if(board[i][j] == 'O'):
                        #print ("Hello")
                        #print ('白棋坐标，I J ', i, j,"\n")
                        self.whiteMoves += validMove.calMoves()
                        #print (self.whiteMoves)
                        #totalValidMoves += calWhiteMove
                    if(board[i][j] == '@'):   

                        #print ('黑棋坐标 I J', i, j, "\n")
                        
                        self.blakcMoves += validMove.calMoves()
                        #print (self.blakcMoves)
                        #print ("HEllo")
                        #print (blakcMoves)
                        #totalValidMoves+=calBlackMove
                    else:
                        continue
            #print (self.whiteMoves, self.blakcMoves)
            return [self.whiteMoves,self.blakcMoves]

    def getPiece(self, position):
        if(position[0] > 7 or position[0] < 0 or position[1] >7 or position[1] < 0):
            return ' '
        #Default position[0] is i i.e row number and position[j] is j i.e column number
        piece = self.board[position[0]][position[1]]
        return piece

    def countMoves(self,lists):
        totalValidMoves = 0
        #print ("Hello")
        if(len(self.board)==0):
            return 0
        ##print (self.board)
        for piece in lists:
            #print ("Hello")
            column = piece[1]
            row = piece[0]
            #print(piece)
            directions = [(row,column+1), (row,column-1), (row+1,column),(row-1,column)]
            for i in range(0,4):
                #print ("Hello")
                if(self.getPiece(directions[i])=='-'):
                    totalValidMoves+=1
                    #print ("Hello")
                if(self.getPiece(directions[i])=='O' or self.getPiece(directions[i])=='@'):
                    newColumn = directions[i][1]
                    newRow = directions[i][0]

                    if(i == 0 and self.getPiece((newRow, newColumn+1))== '-'):
                        #print ("Jump1")
                        totalValidMoves+=1
                        continue
                    if(i==1 and self.getPiece((newRow, newColumn-1))=='-'):
                        #print ("Jump2")
                        totalValidMoves+=1
                        continue
                    if(i==2 and self.getPiece((newRow+1, newColumn))=='-'):
                        #print ("Jump 3")
                        totalValidMoves+=1
                        continue
                    if(i==3 and self.getPiece((newRow-1, newColumn))== '-'):
                        #print("Jump4")
                        totalValidMoves+=1
                        continue
        #print (totalValidMoves)
        return totalValidMoves

class ValidMove:
    'used to justify the available move for one chess piece'
    x = 0
    y = 0
    board = []
    validMoves = 0
    def __init__(self, x, y, board):
        self.x = x
        self.y = y
        self.board = board
        #print (board)
    
    def calMoves(self):
        try: 
            if(self.board[self.x-1][self.y] == '-'):
                self.validMoves += 1
            elif(self.board[self.x-2][self.y] == '-'):
                self.validMoves += 1
        except IndexError:
            pass

        try:    
            if(self.board[self.x+1][self.y] == '-'):
                self.validMoves += 1
            elif(self.board[self.x+2][self.y] == '-'):
                self.validMoves += 1
        except IndexError:
            pass

        try:    
            if(self.board[self.x][self.y-1] == '-'):
                self.validMoves += 1
            elif(self.board[self.x][self.y-2] == '-'):
                self.validMoves += 1        
        except IndexError:
            pass

        try:    
            if(self.board[self.x][self.y+1] == '-'):
                self.validMoves += 1
            elif(self.board[self.x][self.y+2] == '-'):
                self.validMoves += 1
        except IndexError:
            pass
            
        return self.validMoves

def find_path(start, end, came_from):
    #make the shortest path
    path = [end]

    current = end
    while current != start:
        current = came_from[current]
        path.append(current)

    # reverse to have Start -> Target
    # just looks nicer
    path.reverse()

    return path

def get_neighbors(grid, row, col):
    height = len(grid)
    width = len(grid[0])

    neighbors = [(row + 1, col), (row, col - 1), (row - 1, col), (row, col + 1)]

    # make path nicer
    if (row + col) % 2 == 0:
        neighbors.reverse()

    # check borders
    neighbors = filter(lambda t: (0 <= t[0] < height and 0 <= t[1] < width), neighbors)
    # check other pieces
    neighbors = filter(lambda t: (grid[t[0]][t[1]] not in OBSTACLE_COL), neighbors)

    return neighbors

def scan_grid(grid, start=(0, 0)):
    #scan the whole board, so every time we can find a path for the piece put in

    q = deque()
    q.append(start)
    came_from = {start: None}
    while len(q) > 0:
        current_pos = q.popleft()
        neighbors = get_neighbors(grid, current_pos[0], current_pos[1])
        for neighbor in neighbors:
            if neighbor not in came_from:
                q.append(neighbor)
                came_from[neighbor] = current_pos

    return came_from


def init(board):
    whitePieces = []
    blackPieces = []
    initial_grid = board
    terminated = []
    for i in range(8):
        for j in range(8):
            if board[i][j] == 'O':
                whitePieces.append((i, j))
            if board[i][j] == '@':
                blackPieces.append((i, j))
    
    #to generate path, found out the surrouding enviroment, is it next to a corner or next to a white piece already,
    #or is the piece already at the edge
    for wPiece in whitePieces:
        for bPiece in blackPieces:
            start_pos = wPiece
            directions = scan_grid(initial_grid, start_pos)
            if bPiece[1] == 7 and board[bPiece[0]][bPiece[1]-1] == 'O':
                terminated.append(bPiece)
            elif board[bPiece[0]-1][bPiece[1]] == 'O' and bPiece[0] == 7:
                terminated.append(bPiece)
            elif board[bPiece[0]+1][bPiece[1]] == 'O'  and bPiece[0] == 0:
                terminated.append(bPiece)
            elif board[bPiece[0]][bPiece[1]-1] == 'O' and bPiece[1] == 0:
                terminated.append(bPiece)        
            elif bPiece[0] != 0 and bPiece[0] != 7 and (board[bPiece[0]-1][bPiece[1]] == 'O' or board[bPiece[0]-1][bPiece[1]] == 'X') and (board[bPiece[0]+1][bPiece[1]] == 'O' or board[bPiece[0]+1][bPiece[1]] == 'X'):
                terminated.append(bPiece)
            elif bPiece[1] != 0 and bPiece[1] != 7 and (board[bPiece[0]][bPiece[1]+1] == 'O' or board[bPiece[0]][bPiece[1]+1] == 'X') and (board[bPiece[0]][bPiece[1]-1] == 'O' or board[bPiece[0]][bPiece[1]-1] == 'X'):
                terminated.append(bPiece)
            
            if bPiece not in terminated:
                if bPiece[1] == 7 or board[bPiece[0]][bPiece[1]+1] == 'O' or board[bPiece[0]][bPiece[1]+1] == 'X' :
                    path = find_path(start_pos, (bPiece[0], bPiece[1]-1), directions)
                    terminated.append(bPiece)
                    board[wPiece[0]][wPiece[1]] == '-'
                    wPiece = (bPiece[0], bPiece[1]-1)
                    board[wPiece[0]][wPiece[1]] == 'O'
                    for pos in path:
                        print(pos[::-1] + '->')

                elif bPiece[1] == 0 or board[bPiece[0]][bPiece[1]-1] == 'O' or board[bPiece[0]][bPiece[1]-1] == 'X' :
                    path = find_path(start_pos, (bPiece[0], bPiece[1]+1), directions)
                    terminated.append(bPiece)
                    board[wPiece[0]][wPiece[1]] == '-'
                    wPiece = (bPiece[0], bPiece[1]-1)
                    board[wPiece[0]][wPiece[1]] == 'O'
                    for pos in path:
                        print(pos[::-1], end = '->')
                        
                elif bPiece[0] == 7 or board[bPiece[0]+1][bPiece[1]] == 'O' or board[bPiece[0]+1][bPiece[1]] == 'X' :
                    path = find_path(start_pos, (bPiece[0]-1, bPiece[1]), directions)
                    terminated.append(bPiece)
                    board[wPiece[0]][wPiece[1]] == '-'
                    wPiece = (bPiece[0], bPiece[1]-1)
                    board[wPiece[0]][wPiece[1]] == 'O'
                    for pos in path:
                        print(pos[::-1], end = '->')
                        
                elif bPiece[0] == 0 or board[bPiece[0]-1][bPiece[1]] == 'O' or board[bPiece[0]-1][bPiece[1]] == 'X' :
                    path = find_path(start_pos, (bPiece[0]+1, bPiece[1]), directions)
                    terminated.append(bPiece)
                    board[wPiece[0]][wPiece[1]] == '-'
                    wPiece = (bPiece[0], bPiece[1]-1)
                    board[wPiece[0]][wPiece[1]] == 'O'
                    for pos in path:
                        print(pos[::-1], end = '->')
                        
                else:
                    path = find_path(start_pos, (bPiece[0]+1, bPiece[1]), directions)
                    board[wPiece[0]][wPiece[1]] == '-'
                    wPiece = (bPiece[0], bPiece[1]-1)
                    board[wPiece[0]][wPiece[1]] == 'O'
                    for pos in path:
                        print(pos[::-1], end = '->')

if __name__ == "__main__":
    print("Enter the input, Ctrl+X to end:")
    board = []
    chessBoard = []
    whitePieces = []
    blackPieces = []
    n = 0
    while True:
        try:
             line = input()
        except EOFError:
            break
        board.append(line)
    n = 0
    for line in board:
        if line != "Move" and line != "Massacre":
            #print(line)
            chessBoard.append(line.split(' '))
            n+=1
    if(board[8] == 'Massacre'):
        init(chessBoard)
    else:
        boardAnalyser = BoardAnalyser(chessBoard)
        whitePieces,blackPieces = boardAnalyser.readBoard()
        print(boardAnalyser.countMoves(whitePieces))
        print(boardAnalyser.countMoves(blackPieces))


