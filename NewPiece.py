from copy import copy 
from queue import PriorityQueue

class Piece ():
	def __init__(self, dist, parent, startPoint=0, goalPoi = 0):
		self.children = []
		self.parent = parent
		self.dist = dist
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

	def __int__(self,dist, parent,surrounding, startPoint = 0, goalPoi = 0):
		#invoke a super constructor
		super(ConcretePiece,self).__int__(dist,parent,startPoint,goalPoi)
		self.surrounding = deepycopy(surrounding)

	
	def children(self):

		if not self.children:
			for i in range(0,4):
				# First case, when there is no surrounding pieces around
				#i.e. it can move freely (no jumping here)
