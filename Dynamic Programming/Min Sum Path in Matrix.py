"""

Min Sum Path in Matrix
Problem Description

Given a M x N grid A of integers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Return the minimum sum of the path.

NOTE: You can only move either down or right at any point in time.



Problem Constraints
1 <= M, N <= 2000

-1000 <= A[i][j] <= 1000



Input Format
First and only argument is a 2-D grid A.



Output Format
Return an integer denoting the minimum sum of the path.



Example Input
Input 1:

 A = [
       [1, 3, 2]
       [4, 3, 1]
       [5, 6, 1]
     ]
Input 2:

 A = [
       [1, -3, 2]
       [2, 5, 10]
       [5, -5, 1]
     ]


Example Output
Output 1:

 8
Output 2:

 -1


Example Explanation
Explanation 1:

 The path will be: 1 -> 3 -> 2 -> 1 -> 1.
Input 2:

 The path will be: 1 -> -3 -> 5 -> -5 -> 1.


"""


class Solution:
	# @param A : list of list of integers
	# @return an integer
	def minPathSum(self, A):
	    rows = len(A)
	    cols = len(A[0])
	    
	    cost = [[0 for j in range(cols)] for i in range(rows)]
	    
	    for i in range(rows):
	        for j in range(cols):
	            
	            if i == 0 and j == 0:
	                cost[i][j] = A[i][j]
	                
	            elif i == 0:
	                cost[i][j] = A[i][j] + cost[i][j-1]
	                
	            elif j == 0:
	                cost[i][j] = A[i][j] + cost[i-1][j]
	                
	            else:
	                cost[i][j] = A[i][j] + min(cost[i-1][j], cost[i][j-1])
	                
	    return cost[rows-1][cols-1]
	                
	                
