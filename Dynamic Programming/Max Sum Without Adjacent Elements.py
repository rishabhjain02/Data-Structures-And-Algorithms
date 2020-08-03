"""

Max Sum Without Adjacent Elements
Problem Description

Given a 2 x N grid of integer, A, choose numbers such that the sum of the numbers is maximum and no two chosen numbers are adjacent horizontally, vertically or diagonally, and return it.

Note: You can choose more than 2 numbers.



Problem Constraints
1 <= N <= 20000
1 <= A[i] <= 2000



Input Format
The first and the only argument of input contains a 2d matrix, A.



Output Format
Return an integer, representing the maximum possible sum.



Example Input
Input 1:

 A = [   
        [1]
        [2]    
     ]
Input 2:

 A = [   
        [1, 2, 3, 4]
        [2, 3, 4, 5]    
     ]


Example Output
Output 1:

 2
Output 2:

 8


Example Explanation
Explanation 1:

 We will choose 2.
Explanation 2:

 We will choose 3 and 5.

"""


class Solution:
	# @param A : list of list of integers
	# @return an integer
	def adjacent(self, A):
	    n = len(A[0])
	    if n == 0:
	        return 0
	    
	    B = [0]*n
	    
	    for i in range(n):
	        B[i] = max(A[0][i], A[1][i])
	        
	    val1 = B[0]
	    
	    if n == 1:
	        return val1
	        
	    val2 = max(B[0], B[1])
	         
	    if n == 2:
	        return val2
	        
	    max_sum = None
	    
	    for i in range(2, n):
	        max_sum = max(B[i]+val1, val2)
	        val1 = val2
	        val2 = max_sum
	        
	    return max_sum
