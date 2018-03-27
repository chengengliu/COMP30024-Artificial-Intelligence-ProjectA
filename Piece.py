
from ValidMove import ValidMove
from Stack import Stack
import aimapython.search
#from aimapython.search import search


class GoalToSolve(aimapython.search.Problem):
	def __init__(self, initialState, goal = None):
		self.initialState = initialState
		self.goal = goal
	def actions(self, initialState):

		checkSurrounding(7)

	def checkSurrounding(self, numberOfPieces):
		print ()


	def pathCost(initialState, finalState, goalPosition):
		firstCost = [i - j for i, j in zip(initialState, goalPosition)]
		secondCost =[i - j for i, j in zip(finalState, goalPosition)]
		#The first movement is still better 
		if(calculateCost(firstCost[0], firstCost[1])> 
			calculateCost(secondCost[0], secondCost[0])):
			return initialState
		else:
			return finalState

	def calculateCost(point1, point2):
		dist = (point2[0] - point1[0])^2 + (point2[1]- point1[1]) ^2
		return dist

class Piece(aimapython.search.Node):

	def __init__(self, row, column, color, state, pathCost = 0):
		self.row = row
		self.column = column
		self.color = color
		self.state = state
		self.pathCost = pathCost

	def checkSurrounding(self, numberOfPieces):
		print ()
	def checkChild(self):
		print ()

