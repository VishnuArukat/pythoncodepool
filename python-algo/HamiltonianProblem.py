class HamiltonianProblem(object):

	"""docstring for HadjacencymatrixltonianProblem"""

	def __init__(self, adjacencyMatrix):
		self.numOfVertexes = len(adjacencyMatrix)
		self.hamiltonianPath = [None] * self.numOfVertexes
		self.adjacencyMatrix = adjacencyMatrix

	def hamiltonianCycle(self):
		self.hamiltonianPath[0] = 0			#setting up that we are starting from the 0 index and assigning 0 to it and we can start from any node but we have to change the other function also

		if not self.findFeasibleSolution(1): #checking the path from position 1 bcoz we assign the 0 as the start node previous comment
			print "No feasible solution found"
			return
		else:
			self.showHamiltonianPath()


	def findFeasibleSolution(self,position):
		# to check whether we are done, so that we connect the last node to the first node to form a cycle.
		if position == self.numOfVertexes:
			x = self.hamiltonianPath[position -1]	#end node
			y = self.hamiltonianPath[0] #first node

			if self.adjacencyMatrix[x][y] == 1:  # checking whether these two are connected or not in the adjancency matrix
				return True
			else:
				return False

		# if the above if statement is false then evluvate the for statement

		for vertexIndex in xrange(1,self.numOfVertexes):
			if self.isFeasible(vertexIndex , position):
				self.hamiltonianPath[position] = vertexIndex

				if self.findFeasibleSolution(position+1): #checking for the next node calling the function again
					return True

		return False

	def isFeasible(self , vertex , actualPosition):
			# First criteria whether the two nodes are connected?

		if self.adjacencyMatrix[self.hamiltonianPath[actualPosition-1]] [vertex] == 0:
			return False

		# Second criteria whether we have already added this node

		for i in xrange(actualPosition):
			if self.hamiltonianPath[i] == vertex:
				return False
		return True


	def showHamiltonianPath(self):
		print "Hamiltonian cycle exist"

		for i in xrange(self.numOfVertexes):
			print self.hamiltonianPath[i],

		print self.hamiltonianPath[0] # printing the first element one more time so that it will form a cycle


if __name__ == '__main__':

	adjacencyMatrix = [ [0 , 1 , 1], [1 , 0 , 1], [1 , 1 , 0] ]
	hamiltonian = HamiltonianProblem(adjacencyMatrix)
	hamiltonian.hamiltonianCycle()