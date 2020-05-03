"""

Spiral Order Matrix II
Given an integer A, generate a square matrix filled with elements from 1 to A^2 in spiral order. 
 Input Format:
The first and the only argument contains an integer, A.
Output Format:
Return a 2-d matrix of size A x A satisfying the spiral order.
Constraints:
1 <= A <= 1000
Examples:
Input 1:
    A = 3

Output 1:
    [   [ 1, 2, 3 ],
        [ 8, 9, 4 ],
        [ 7, 6, 5 ]   ]

Input 2:
    4

Output 2:
    [   [1, 2, 3, 4],
        [12, 13, 14, 5],
        [11, 16, 15, 6],
        [10, 9, 8, 7]   ]

"""

class Solution:
	# @param A : integer
	# @return a list of list of integers
	def generateMatrix(self, A):
	    n = A
	    spiral_matrix = [[0 for i in range(n)] for j in range(n)]
	    row_start = 0
	    row_end = n-1
	    col_start = 0
	    col_end = n-1
	    num = 1
	    while(num <= n*n):
	        for c in range(col_start, col_end+1):
	            spiral_matrix[row_start][c] = num
	            num += 1
	        row_start += 1
	        
	        for r in range(row_start, row_end+1):
	            spiral_matrix[r][col_end] = num
	            num += 1
	        col_end -= 1
	        
	        for c in range(col_end, col_start-1, -1):
	            spiral_matrix[row_end][c] = num
	            num += 1
	        row_end -= 1
	        
	        for r in range(row_end, row_start-1, -1):
	            spiral_matrix[r][col_start] = num
	            num += 1
	        col_start += 1
	        
	    return spiral_matrix
	        
	    
