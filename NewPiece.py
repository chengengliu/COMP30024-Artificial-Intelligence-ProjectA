from copy import copy 
from queue import PriorityQueue

class Piece ():
	#position contains the coordinates of the piece. (as a list)

	def __init__(self, position, parent, startPoint=0, goalPoi = 0):
		self.children = []
		self.parent = parent
		self.position = position
		self.cost = 0
		if not parent:
			self.path = [value]
			self.start = start
			self.goal = goal 
		else:
			self.path = parent.path[:]
			self.start = parent.start
			self.goal = parent.goal
			self.path.append(value)

class ConcretePiece(Piece):

	def __int__(self,position, parent,surrounding, startPoint = 0, goalPoi = 0):
		#invoke a super constructor
		super(ConcretePiece,self).__int__(position,parent,startPoint,goalPoi)
		self.surrounding = deepcopy(surrounding)

	
	def children(self):
		#下上右左
		direction = [(0,1), (0,-1), (1,0), (-1,0)]

		if not self.children:
			for i in range(0,4):
				# First case, when there is no surrounding pieces around
				#i.e. it can move freely (no jumping here)
				#上下左右 都要看
				newColumn = self.position[0] + direction[i][0]
				newRow = self.position[1] + direction[i][1]
				if(newColumn > 7 or newColumn < 0 
					or newRow > 7 or newRow < 0):
					continue
				#New position
				newPosition = (newColumn, newRow)

				#if the new position is empty(ie.free to move )
				if(self.surrounding[newRow][newColumn] == '-'):
					newSurrounding = deepcopy(self.surrounding)
					#The piece has moved so the original position become unocupied. 
					#Move to the new position and posess the position as 'O'
					# I have to switch 0 and 1 order because the oder of the board
					# is the reverse of the coordinates
					newSurrounding[self.position[1]][self.position[0]] = '-'
					newSurrounding[newPosition[1]][newPosition[0]] = 'O'
					#Make the child node
					#Add it to child list
					child = ConcretePiece(position, self, newSurrounding)
					self.child.append(child)
					continue
				#Reinitialise the position movement 
				# Now considering jumping 
				newNewColumn = self.position[0] + direction[i][0]
				newNewRow = self.position[1] + direction[i][1]	
				newNewPosition = (newNewColumn,newNewRow)
				if(self.surrounding[newNewRow][newNewColumn] == '-') and 








