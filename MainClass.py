#from ReadBoard import ReadBoard
from ValidMove import ValidMove
from Graph import Graph
from collections import defaultdict
from MakeMoves import MakeMoves
import aimapython.search

print("Enter the input, Ctrl+X to end:")
board = []
pieceList = []
n = 0
dict = {}

totalValidMoves = 0
calWhiteMove = calBlackMove = 0
while True:
    try:
         line = input()
    except EOFError:
        break
    board.append(line)



print(board)

#
#  ####记住 一点， board坐标是反着的。 如果以下面ij 为例子， 坐标应该是（j，i)。 
#

#number 8 is the maximum length of the board, recommend to use len(board)
#in case the board shrinks
if(board[8] == 'Moves'):
    for i in range(0, 8):
        for j in range(0, 8):
            #print (i)
            #print (j)
            
            #add an extral line here, dictionary for position and element save,
            #used by graph down below
            dict[(i,j)] = board[i][j]
            validMove = ValidMove(i, j, board)
            #print (validMove)
            if(board[i][j] == 'O'):
                #print ('白棋坐标，I J ', i, j,"\n")
                calWhiteMove += validMove.calMoves()
                #totalValidMoves += calWhiteMove
            if(board[i][j] == '@'):   

                #print ('黑棋坐标 I J', i, j, "\n")
                        
                calBlackMove += validMove.calMoves()
                #totalValidMoves+=calBlackMove
            else:
                continue

#print (totalValidMoves)

print(calWhiteMove)
print(calBlackMove)



#moving pieces stage
if(board[8] == 'Massacre'):
    for i in range(0,8):
        for j in range(0,8):
            if(board[i][j] == 'O'):



    '''
    for i in range(0, 8):
        for j in range(0, 8):

            #add an extral line here, dictionary for position and element save,
            #used by graph down below
            dict[(i,j)] = board[i][j]
        
    graph = Graph()
    
    #adding edges to the graph class to form the network, again, method not tested yet
    #only theoretically corret
    for key1, value1 in dict.items():
        for key2, value2 in dict.items():
            if((abs(key1[0] - key2[0])==1 or abs(key1[1] - key2[1])==1) and (abs(key1[0] - key2[0]) != abs(key1[1] - key2[1])==1)):
                Graph.addEdge(dict[key1,value1], dict[key2, value2])    
    
    for i in range(0, 8):
        for j in range(0, 8):
            if(board[i][j] == '@'):
                #BFS should stop when ever find a white piece, aka O, the point
                #hasnt been added yet, the BFS still goes through the whole
                #board, we also need the white piece position for moving stage
                graph.BFS({(i,j):board[i][j]})
                #makeMoves = MakeMoves(white piece postition)
    ''' 



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



'''build a graph for bfs, not tested yet '''
