class QueensProblem(object):
	
	"""docstring for QueensProblem"""
	

	def __init__(self, numofqueens):
		self.queensArray = [None] * numofqueens  # creating a list using the numof queens
		self.numofqueens = numofqueens
		self.count = 0			#add self because it is a class


	def solveQueensProblem(self):
		self.arrangeQueens(0)    #calling the arrange queens and passing the value  index[0] as the starting position

	def arrangeQueens(self,rowIndex):
		
		for i in xrange(self.numofqueens):

			if self.isPlaceValid(rowIndex,i):
				self.queensArray[rowIndex] = i

				if rowIndex == (self.numofqueens - 1):   #To check whether we placed all the queens in the board
					self.printQueens()
					self.count+=1
				else:
					self.arrangeQueens(rowIndex + 1)

	def isPlaceValid(self,rowIndex,coloumnIndex):
		
		for i in xrange(rowIndex):
			
			if self.queensArray[i] == coloumnIndex: #same coloumn
				return False

			if (abs(i - rowIndex) == abs(self.queensArray[i] - coloumnIndex)):	#for asscending
			 	return False

			# if ((i - rowIndex) == (self.queensArray[i] - coloumnIndex)):	#for asscending
			# 	return False

			# if ((i - rowIndex) == (coloumnIndex - self.queensArray[i])):	#for diagonal
			# 	return False

		return True  #This return statement is part of the function not the loop

	def printQueens(self):
		
		for i in xrange(self.numofqueens):
			for j in xrange(self.numofqueens):
				
				if (self.queensArray[i] == j):
					print " Q ",
				else:
					print " - ",

			print "\n"
		
		print "\n"
		

if __name__ == '__main__':

	queenproblem = QueensProblem(8)

	result = queenproblem.solveQueensProblem()
		
	print "The no of posiible solution for the {0}  queens problem is {1}".format( queenproblem.numofqueens , queenproblem.count) 
