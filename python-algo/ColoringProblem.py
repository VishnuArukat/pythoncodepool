class ColoringProblem:

	def __init__(self, numofColors, graphMatrix):
		self.numofVerices = len(graphMatrix)
		self.numofColors  = numofColors
		self.colors = [0]* self.numofVerices
		self.graphMatrix = graphMatrix

	def solveColoringProblem(self):
		if not self.solve(0):
			print "There is no feasible solution to the given problem"
		else:
			self.showResult()

	def solve(self, nodeIndex):
			if nodeIndex == self.numofVerices:  #here nodeIndex will be 5 after the incriment in the below code and it will exit the loop not executing down
				return True

			# trying all colors

			for colorIndex in xrange(1, self.numofColors+1):  # we use the numofColors+1 becoz range() doesnt print the upperbound
				if self.isColorValid(nodeIndex, colorIndex):
					# assign the color and proceed with the next vertex
					self.colors[nodeIndex] = colorIndex

					if self.solve(nodeIndex+1):	 	
						return True		#recursion calling the same function inside the function
			return False

	def isColorValid(self, nodeIndex, colorIndex):
		for i in xrange(self.numofVerices):
			if self.graphMatrix[nodeIndex][i] == 1 and colorIndex == self.colors[i]:
				return False
		return True

	def showResult(self):
		for i in xrange(self.numofVerices):
			print "Node {0} has color index :  {1} .".format(i, self.colors[i])


if __name__ == '__main__':

	# (0)--------------(1)------(2)
	# |\
	# | --------
	# |			\
	# |				\
	# (3)-------------(4)
	graphMatrix = [[0,1,0,1,1], [1,0,1,0,1], [0,1,0,0,0], [1,0,0,0,1], [1,1,0,1,0]]  # these is an adjacency matrix that we are passing
	numofColors = 3
	# numofVerices = 5
	coloringproblem = ColoringProblem(numofColors, graphMatrix)
	coloringproblem.solveColoringProblem()




	
