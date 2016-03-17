class Mazeproblem:

	def __init__(self , mazeTable):

		self.mazeTable = mazeTable
		self.mazeSize = len(mazeTable)
		self.solutionTable = [[0]*self.mazeSize for i in xrange(self.mazeSize)]

	def solveMaze(self):
		
		if not self.solve(0,0):
			print "no feasile solution has found"
		else:
			self.showResult()


	def solve(self,x,y):
		
		if  self.isFinished(x,y):
			return True

		if self.isValid(x,y):
			self.solutionTable[x][y] = 1 #if it is valid it is part of the soltion

		# recursion
			# go downward
			if self.solve(x+1,y):
				return True
			# going right
			if self.solve(x,y+1):
				return True

			self.solutionTable[x][y] = 0   #no feasible solution backtrack

		return False

	def isFinished(self,x,y):
		# you can change the finish point by changing the index for the finish point
		if x == self.mazeSize-1 and y == self.mazeSize-1:
			self.solutionTable[x][y] =1
			return True
		return False
		
	def isValid(self,x,y):

		if x < 0  or x >= self.mazeSize:return False
		if y < 0  or y >= self.mazeSize:return False

		if self.mazeTable[x][y] != 1:
			return False

		return True

	def showResult(self):

		for i in xrange(self.mazeSize):
			for j in xrange(self.mazeSize):
				if self.solutionTable[i][j] ==1:
					print "S",
				else:
					print"x",

			print "\n"


if __name__ =='__main__':

# the o in themaze table marks the greyed boxes and 1 marks the possible path
	mazeTable = [[1,1,1,1,1],
				 [1,0,0,0,0],		
				 [1,0,0,1,0],			
				 [1,1,1,1,1],
				 [1,1,1,0,1]
				]

	mazeProblem =  Mazeproblem(mazeTable)
	mazeProblem.solveMaze()









