from collections import defaultdict

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
    
    #the calculate moves method used a lot of exceptions, yet only the index
    #error is excepted, just for the case that when test the potential move
    #direction, it will not give a index error message and end the whole program
    #it also included the jumping position for every direction it test
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

#the piece class used to represent every valid piece on the board
class Piece:

    #distance between a white piece and a black piece, used to find the closest piece
    #only used to represent the closest black piece to a white piece, so this attribute 
    #is not used if the chess piece is a black piece(still under consideration)
    distance = 0

    def __init__(self, x, y, color, state):
        self.x = x
        self.y = y
        self.color = color #0 reps white piece, 1 reps black piece
        self.state = state #0 reps still on board, 1 reps being terminated

    #the direct distance between two piece, could also indicate how many steps it would take to get to the target piece
    def calDist(self, x, y):
        return abs(self.x - x) + abs(self.y - y)

    #setter and getter to get and set the values to every piece
    def get_blackx(self):
        return self.blackx
    def get_blackx(self):
        return self.blacky
    def set_blackx(self, blackx):
        self.x = blackx
    def set_blacky(self, blacky):
        self.y = blacky
    def get_dist(self):
        return self.distance
    def set_dist(self, distance):
        self.distance = distance

class MakeMove:

    #this class is used to make move towards the black piece, 
    path = []

    def __init__(self, whiteX, whiteY, blackX, blackY):
        self.whiteX = whiteX
        self.whiteY = whiteY
        self.blackX = blackX
        self.blackY = blackY

    #make move method, check the distance untill the white piece hits the black piece 
    #either horizentally or vertically, it also need to check if there is another 
    #white piece near the black piece already, so the function can make a terminating move
    def makeMove(self):
        while (abs(self.whiteX - self.blackX) != 1) or (abs(self.whiteY - self.blackY) != 1):




print("Enter the input, Ctrl+X to end:")
board = []
n = 0
whitePieces = []
blackPieces = []
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
    #should use a class rather than having the whole function down below, it need to be
    #fixed later
    #put pieces into the list first
    for i in range(0, 8):
        for j in range(0, 8):
            if(board[i][j] == 'O'):
                piece = Piece(i, j, 0, 0)
                whitePieces.append(piece)
            elif(board[i][j] == '@'):            
                piece = Piece(i, j, 0, 0)
                blackPieces.append(piece)
            else:
                continue
    #now start the loop to calculate the distance
    for wPiece in whitePieces:
        for bPiece in blackPieces:
            if(wPiece.get_dist < wPiece.calDist(bPiece.x, bPiece.y)):
                wPiece.set_dist(wPiece.calDist(bPiece.x, bPiece.y))
                wPiece.set_blackx = bPiece.x
                wPiece.set_blacky = bPiece.y

    #now after the previous loop, all the distances between the pieces are calculated
    #proceed to moving stage
    #loop through the black piece list, check the its state, so if no black piece is alive
    #on the board, game ends, print out the path(P.S. what if some of the black pieces cant be terminated? Fuckkkkkkk)
    for bPiece in blackPieces:
        if(bPiece.state != 1):
            for wPiece in whitePieces:
                makeMove = MakeMove(wPiece.x, wPiece.y, wPiece.blackX, wPiece.blackY)


