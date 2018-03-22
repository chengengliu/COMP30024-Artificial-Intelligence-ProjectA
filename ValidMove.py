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
    '''   x 上下  y 左右'''
    def calMoves(self):
        
        try: 
            if(self.board[self.x-1][self.y] == '-'):
                self.validMoves += 1
            elif(self.board[self.x-2][self.y] == '-') :
                self.validMoves += 1
            
            if(self.board[self.x+1][self.y] == '-'):
                self.validMoves += 1
            elif(self.board[self.x+2][self.y] == '-') :
                
                print (self.board[self.x+2][self.y])   
                print (self.x+2, self.y)
                print (self.board)
                self.validMoves += 1
                #print ("HHHHHH2333\n") 
            
            if(self.board[self.x][self.y-1] == '-'):
                self.validMoves += 1
            elif(self.board[self.x][self.y-2] == '-') :
                print (self.board[self.x][self.y])   
                print (self.x, self.y)
                print (self.board)
                


                self.validMoves += 1        
            
            if(self.board[self.x][self.y+1] == '-'):
                self.validMoves += 1
            elif(self.board[self.x][self.y+2] == '-') and self.y < 6:
                self.validMoves += 1
        except IndexError:
            print ("Out of bounds")

        return self.validMoves
