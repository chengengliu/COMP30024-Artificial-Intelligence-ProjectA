#from ReadBoard import ReadBoard
from ValidMove import ValidMove

print("Enter the input, Ctrl+X to end:")
board = []
n = 0

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
                print ('白棋坐标，I J ', i, j,"\n")
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

'''build a graph for bfs, not tested yet '''
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def addEdge(self, u, v):
        self.graph[u].append(v)
    def BFS(self, startPoint):
        visited = [False]*(len(self.graph))
        queue = []
        queue.append(s)
        visited[s] = True

        while queue:
            s = queue.pop(0)
            print s
            for i in self.graph[s]:
                if visited[i] = False:
                    queue.append(i)
                    visited[i] = True

for key1, value1 in dict.items():
    for key2, value2 in dict.items():
        if((abs(key1[0] - key2[0])==1 or abs(key1[1] - key2[1])==1) and (abs(key1[0] - key2[0]) != abs(key1[1] - key2[1])==1)):
            Graph.addEdge(dict[key1,value1], dict[key2, value2])