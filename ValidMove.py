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
