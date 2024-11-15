from copy import copy 
try:
	from queue import PriorityQueue as Q
except ImportError:
	import queue as Q




class Board():
	def __init__(self, blackList, whiteList):
		self.board = None
		self.pieces = ['O', '@', 'X', '-']
		self.blackList = blackList
		self.whiteList = whiteList

	def getPiece(self, postion):
		if(position[0] > 7 or position[0] < 0 or position[1] >7 or position[1] < 0):
			return ''
		piece = self.board[position[0],position[1]]
		return piece
	# sort the black List based on the sum of distance 
	def sortPieceList(self, blackList, whiteList):
		pQueue = PriorityQueue()
		for blakcPiece in blackList:
			sumOfDistance  = 0
			if(len(whiteList) == 0):
				sumOfDistance = -1
			for whitePiece in whiteList:
				sumOfDistance+=abs(whitePiece[0] - blakcPiece[0])+abs(whitePiece[1]-blakcPiece[1])
				pQueue.put([sumOfDistance, blackList])
		return pQueue





class Piece ():
	#position contains the coordinates of the piece. (as a list)

	def __init__(self, position, parent, startPoint=0, goalPosition = 0):
		self.children = []
		self.parent = parent
		self.position = position
		self.cost = 0
		if parent:
			self.path = [position]
			self.startPoint = startPoint
			self.goalPosition = goalPosition
		else:
			self.path = parent.path[:]
			self.startPoint = parent.startPoint
			self.goalPosition = parent.goalPosition
			self.path.append(self.position)

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
		#Reach the goalPosition 
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
		#Set a counter to count the move order 
		i = 0 
		#Put in the queue 

		##### Not quite sure what should be put in the queue
		##### position must be there. Hwo about the order?
		self.pQueue.put(startingPiece, i)

		# When the queue is not empty and it is not added to path yet
		while(not self.PriorityQueue.empty() and not self.path):
			#Look for the best (nearest ) child 
			#Based on its distance p
			child = pQueue.get()[0]
			child.children()
			self.visited.append(child.position)
			for c in child.children:
				if(c.position not in self.visited):
					count +=1
					pass
				# If reach the goal postiion ie. distance is 0 
				if(c.distance == 0 ):
					self.path = c.path
					print ("Hello")
					break
				self.pQueue.put(c.position, i)

		return self.path

class Eliminate():

	def __init__(self,board, whiteList, blackList):
		self.board = board
		self.pieceList = pieceList


	def EliminatePairFirst(self):
		# pairList will restore the (priority, [dest position], [block piece position ])
		# i.e 2 means second priority to check()
		# i means the blakc piece should be checked first
		pair = []
		for piece in self.blackList:
			column = piece.position[0]
			row = piece.position[1]

			pairList = []
			#Check up and down 
			if(self.board.getPiece(column, row+1) == '-' and self.board.getPiece(column, row-1) == '-'):
				pairList.append(2, [(column,row+1), (column,row-1)],piece)
			#Check if the up side has been possessed by a white/black/corner
			if((self.board.getPiece(colum,row+1) == 'X' or '@ ' or 'O') and self.board.getPiece(column,row-1)=='-'):
				pairList.append(1,[(column,row-1), (column, row+1)], piece)
			#Check if the down side has been possessed by a white/blakc/corner
			if((self.board.getPiece(colum,row-1) == 'X' or '@ ' or 'O') and self.board.getPiece(column,row+1)=='-'):
				pairList.append(1,[(column,row+1), (column, row-1)], piece)
			#Similarly check left and right 
			if(self.board.getPiece(column-1, row) == '-' and self.board.getPiece(column+1, row) == '-'):
				pairList.append(2, [(column-1,row), (column+1,row)],piece)
			#Check if the left side has been possessed by a white/black/corner
			if((self.board.getPiece(colum-1,row) == 'X' or '@ ' or 'O') and self.board.getPiece(column+1,row)=='-'):
				pairList.append(1,[(column+1,row), (column-1, row+1)], piece)
			#Check if the right side has been possessed by a white/blakc/corner
			if((self.board.getPiece(colum+1,row) == 'X' or '@ ' or 'O') and self.board.getPiece(column-1,row)=='-'):
				pairList.append(1,[(column-1,row), (column+1, row)], piece)

			if(len(pairList)>0):
				pair.append(pairList)

		return pair

	def solveForWhitePieces(self):
		piecePairList = self.EliminatePairFirst()
		for piecePair in piecePairList:

			for piece in piecePair:

				weight = 0;
				#Most priority need to eliminate first 
				if(piece[0] == 1):
					position = piece[1][0]
					possessedPiece = pair[1][1]





			








