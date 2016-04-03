
#Introduction

All programs are written with some comments that will give you a slight idea about the code.If you want to know more about it you can read the following.

##Backtracking Problems

*Backtracking is a general algorithm for finding all (or some) solutions to some computational problems, notably constraint satisfaction problems, that incrementally builds candidates to the solutions, and abandons each partial candidate c ("backtracks") as soon as it determines that c cannot possibly be completed to a valid solution.
backtracking is faster than the brute force because it can eliminate large number of candidate with single test.*

* [N QUEENS PROBLEM](###N QUEENS PROBLEM)
* [HAMILTONIAN CYCLE](###HAMILTONIAN CYCLE)
* (###COLORING PROBLEM)
* [KNIGHT TOUR PROBLEM](###KNIGHT TOUR PROBLEM)
* [MAZE PROBLEM](###MAZE PROBLEM)




###N QUEENS PROBLEM

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Place N queens by no two queens not threatens each other.original one was designed for 8 queens but can be generalized for N queens-there are 92 possible solution for 8 queens problem including rotating the board.Gauss and dijikstra (Used this for explaining the power of the structral programming) worked on this.
#####&nbsp;&nbsp;&nbsp;&nbsp;Method
Queens can attack each other for following conditions.
if the chess is a two dimensional array then the indexes are i,j where th i- rowindex and j- is the coloumn indexe
* if the row index of the queens are match then they can attack each other
*	if the coloumn index are equal then they are in a same coloumn they can attack each other
* To check the diagonal we can use the formula that the absolute differance between the rowindex and the coloumnindex are same
&nbsp;&nbsp;a[i,j] and b[k,l]
&nbsp;&nbsp;	then |i-k| = |j-l|
* we are using a list to store the result as index as rowindex and the value as the coloumnindex.
* Here i am going row vise by incrimenting the rowindex and checking the possible position for the queen using the preceding position in the current row
* To know more you can check this [link](https://developers.google.com/optimization/puzzles/queens#propagation-and-backtracking) 

###HAMILTONIAN CYCLE

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Hamiltonian Path is the undirectional path that visit every node exactly once.And Hamiltonian cycle is that the start node and the end node of the path are same.there may be several hamiltonian paths in a graph.And it is NP-complete problem.
#####&nbsp;&nbsp;&nbsp;&nbsp;Method
* we use recusrion to solve the problem.create an empty path array and add vertex 0 to its as the starting vertex.
* we also pass the adjacency matrix of the graph.
* Add other vertice starting from the vertex 1.Before adding the vertex check whether it is  adjacent to the previously added vertex and not added already.
&nbsp;&nbsp;&nbsp;&nbsp;If find such a  vertex -> we add to the possible solution 
&nbsp;&nbsp;&nbsp;&nbsp;if we donot find any such vertex then we return false.
* This is same as the traveling salesman problem
* Here position is used to refer the  previous node of the hamiltonian path and vertex is used to check the next node.
* For more information check [here](http://www.geeksforgeeks.org/backtracking-set-7-hamiltonian-cycle/)

###COLORING PROBLEM

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Hamiltonian Path is the undirectional path that visit every node exactly once.And 
