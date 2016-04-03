
#Introduction

All programs are written with some comments that will give you a slight idea about the code.If you want to know more about it you can read the following.

##Backtracking Problems

*Backtracking is a general algorithm for finding all (or some) solutions to some computational problems, notably constraint satisfaction problems, that incrementally builds candidates to the solutions, and abandons each partial candidate c ("backtracks") as soon as it determines that c cannot possibly be completed to a valid solution.
backtracking is faster than the brute force because it can eliminate large number of candidate with single test.*

* N QUEENS PROBLEM
* HAMILTONIAN CYCLE
* COLORING PROBLEM
* KNIGHT TOUR PROBLEM
* MAZE PROBLEM




###N QUEENS PROBLEM

&nbsp;&nbsp;&nbsp;&nbsp;Place N queens by no two queens not threatens each other.original one was designed for 8 queens but can be generalized for N queens-there are 92 possible solution for 8 queens problem including rotating the board.Gauss and dijikstra (Used this for explaining the power of the structral programming) worked on this.
#####&nbsp;&nbsp;Method
Queens can attack each other for following conditions.
if the chess is a two dimensional array then the indexes are i,j where th i- rowindex and j- is the coloumn indexe
* if the row index of the queens are match then they can attack each other
*	if the coloumn index are equal then they are in a same coloumn they can attack each other
* To check the diagonal we can use the formula that the absolute differance between the rowindex and the coloumnindex are same
&nbsp;&nbsp;a[i,j] and b[k,l]
&nbsp;&nbsp;	then |i-k| = |j-l|
* we are using a list to store the result as index as rowindex and the value as the coloumnindex.
* Here i am going row vise by incrimenting the rowindex and checking the possible position for the queen using the preceding position in the current row
* 

