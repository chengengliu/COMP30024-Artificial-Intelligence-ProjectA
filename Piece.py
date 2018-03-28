
from ValidMove import ValidMove
from Stack import Stack
import aimapython.search

#from aimapython.search import search


class GoalToSolve(aimapython.search.Problem):
	board = []
	pieceList = []

	def __init__(self, initialState,pieceList, board, goal = None):
		self.initialState = initialState
		self.goal = goal
		self.board = board
		self.pieceList = pieceList
	
	###
	#initalState is the current piece(white) that we are looking at
	#It is an piece object in a pieceList
	####
	def actions(self, initialState, numberOfPieces):
		for i in range(0,4):
			if()


		checkSurrounding(numberOfPieces, initialState,nextState)
		return 

	def checkSurrounding(self,numberOfPieces, initialState,nextState):
		for i in pieceList:
			#Search for Black Piece and check the distance cost

			# if the color is black and it is not yet marked as visited(eliminated)
			# so i is the goalPosition 
			if(i.color == 0) and (i.flag == 0):
				pathCost


	def performMovement(self, initialState, goalPosition):
		explored = list()




	def pathCost(initialState, finalState, goalPosition):
		# initialState and finalState are piece object
		firstCost = [i - j for i, j in zip(initialState[0], goalPosition[0])]
		secondCost =[i - j for i, j in zip(finalState[0], goalPosition[0])]

		print (firstCost, secondCost)
		#The first movement is still better 
		if(calculateCost(firstCost[0], firstCost[1])> 
			calculateCost(secondCost[0], secondCost[1])):
			return initialState
		else:
			return finalState

	def calculateCost(point1, point2):
		dist = (point2[0] - point1[0])^2 + (point2[1]- point1[1]) ^2
		return dist

	def dfsSearch(self, pieceList):
		print ()

class Piece():

	def __init__(self, position, color, flag, pathCost = 0):
		'''
		self.row = row
		self.column = column'''
		#这里我用positio(一个坐标的list) 代替了 row， column。position = [j,i] (column, row)
		self.position = position
		
		self.color = color
		self.flag = flag
		self.pathCost = pathCost

	def checkSurrounding(self, numberOfPieces):
		print ()
	def checkChild(self):
		print ()
'''
initlaPosition = [[2,3], [3,3]]
initlaPosition.append([2,3])
print (initlaPosition)

initlaPosition[0] = [0,0]
print (initlaPosition)'''

