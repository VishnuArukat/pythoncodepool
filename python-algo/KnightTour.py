class KnightTour:
	def __init__(self,boardSize):
		
		self.boardSize = boardSize
# these possible moves have been calculated using the knight at the origin or the start position (0,0) consider the chess as a  x-y coordinate then 
# we can mark the possible final points where the knight will end up using the x-y coordinate and here the -1 will means that it is
# an arbitary position which is outside the chess and ( importantly consider the x-y have -ve terms also)

		self.xMoves = [2,1,-1,-2,-2,-1,1,2]   #these are the possible moves in x 
		self.yMoves = [1,2,2,1,-1,-2,-2,-1]
		# we creating 2D array and initializing with the -1 and the size of the 2D array is boardsize

		# this format is same as b= [-1] * boardsize
		# the syntax is like this a= [value for loop] it will create list of size of the for loop input
		# here the second value is the list that is created using the first for loop
		# ex:   a= [[-1 for x in xrange(2)] for x in xrange(2)]   fist arg will be replaced by the list
		#  	ie a = [[-1,-1] for x in xrange(2)]
		# the result will become [[-1,-1],[-1,-1]]


		self.solutionMatrix = [[-1 for x in xrange(boardSize)] for x in xrange(boardSize)]


	def solveKnightTourProblem(self):
		# starting position as the stepcount =0
		self.solutionMatrix[0][0]=0
		# start the stepcount from 1
		if not self.solveProblem(1,0,0):
			print "no feaasible solution found"
			return

		self.showSolution()

	def solveProblem(self,stepCount,x,y):
		
		if stepCount == (self.boardSize *self.boardSize):
			#checking whether we have consider all the possiblities 
			return True

		for i in xrange(self.boardSize):
			# this is for finding out the next possible 8 positions
			nextX = x+self.xMoves[i]
			nextY = y+self.yMoves[i]

			if self.isValidMove(nextX,nextY):
				self.solutionMatrix[nextX][nextY] = stepCount

				stepCount+=1

				# checking for the valid move at the current position with the recursive call and if not set the current position as the -1 and backtrack

				if self.solveProblem(stepCount, nextX,nextY):
					return True  # return here means it will exit the function
				# below line only execute if the above if fails ---> no valid move
				self.solutionMatrix[nextX][nextY] = -1

 		return False

 	def isValidMove(self,x,y):
 		# this function checks whether the moves are inside the chess or not and if it outside then return false
 		
 		if x < 0 or x >= self.boardSize:
 			return False
 		if y < 0 or y >= self.boardSize:
 			return False
 		# greater than -1 means that we already visited the index so return false
 		if self.solutionMatrix[x][y] > -1:
 			return False

 		return True


 	def showSolution(self):
 		for i in xrange(self.boardSize):
 			for j in xrange(self.boardSize):
 				print self.solutionMatrix[i][j],

 			print "\n"


if __name__=='__main__':
	knightTour =  KnightTour(6)
	knightTour.solveKnightTourProblem()


 





