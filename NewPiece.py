from copy import copy 
try:
	import PriorityQueue as Q
except ImportError:
	import queue as Q

class Piece ():
	#position contains the coordinates of the piece. (as a list)

	def __init__(self, position, parent, startPoint=0, goalPosition = 0):
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

	def __int__(self,position, parent,surrounding, startPoint = 0, goalPosition = 0):
		#invoke a super constructor
		super(ConcretePiece,self).__int__(position,parent,startPoint,goalPosition)
		self.surrounding = deepcopy(surrounding)
		self.distance = self.calculateDistance()

	
	def children(self):
		#下上右左
		direction = [(0,1), (0,-1), (1,0), (-1,0)]

		#If current piece is not child
		if not self.children:
			for i in range(0,4):
				# First case, when there is no surrounding pieces around
				#i.e. it can move freely (no jumping here)
				#上下左右 都要看
				newColumn = self.position[0] + direction[i][0]
				newRow = self.position[1] + direction[i][1]
				#If out of bounds, skip the move 
				if(newColumn > 7 or newColumn < 0 
					or newRow > 7 or newRow < 0):
					continue
				if(self.surrounding[newRow][newColumn] == 'X'):
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
					self.children.append(child)
					continue
				#Reinitialise the position movement 
				# Now considering jumping 
				newNewColumn = self.position[0] + direction[i][0]
				newNewRow = self.position[1] + direction[i][1]	
				newNewPosition = (newNewColumn,newNewRow)
				# If the next of the next move is free and the next move is 
				# possessed by other pieces(no matter what color is )
				if((self.surrounding[newNewRow][newNewColumn] == '-') and 
					(surrounding[newRow][newColumn] == 'O' or '@')):
					#Similarly as above, change the original position to '- free'
					# Change the next new postion to 'O 'possessed
					newSurrounding = deepcopy(self.surrounding)
					newSurrounding[self.position[0]][self.position[1]] = '-'
					newSurroundingp[newNewPosition[0]][newNewPosition[1]] = 'O'
					child = ConcretePiece(position, self, newSurrounding)
					self.children.append(child)
				#If the next position is out of bounds or hit a conner
				#Skip move
				if((self.surrounding[newRow][newColumn] == 'O' or '@' or'X') and 
					(newNewRow> 7 or newNewRow < 0 or newNewColumn > 7 or newNewColumn < 0)):
					continue
				if((self.surrounding[newRow][newColumn] == 'O' or '@' or 'X') and
					(self.surrounding[newNewRow][newNewColumn] == 'O' or '@')):
					continue

	#This should be the priority rule(or should we call it the heuristic function ? LOL )
	def calculateDistance(self):
		distance = abs(self.position[0] - self.goalPosition[0]) + abs(self.postion[1]-self.goalPosition[1])
		if(self.position[0] == self.goalPosition[0] and self.position[1] == self.goalPosition[1]):
			return 0
		return distance

class GreedyBestSearch:
	def __init__(self, startPosition,goalPosition, surrounding):
		#
		#Might need to record the path ? Not Sure here 
		#
		self.goalPosition = goalPosition
		self.surrounding = surrounding
		self.visited = []
		self.path = []
		self.startPosition = startPosition
		self.pQueue  = Q()
	def search(self):
		startingPiece = ConcretePiece(self.startPosition,0,self.surrounding)
		#how to add the queue ?????
		# this is the question
		#Set a counter to count the move 
		i = 0 
		#Put in the queue 
		self.pQueue.put(i,startingPiece)

		# When the queue is not empty and it is not added to path yet
		while(not self.PriorityQueue.empty() and not self.path):
			#Look for the best (nearest ) child 
			#Based on its distance p
			child = pQueue.get()
			child.children()
			self.visited.append(child.position)
			for c in child.children:
				print ()


			








