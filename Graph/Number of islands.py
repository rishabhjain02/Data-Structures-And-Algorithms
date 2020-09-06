"""

Number of islands
Problem Description

Given a matrix of integers A of size N x M consisting of 0 and 1. A group of connected 1's forms an island. From a cell (i, j) such that A[i][j] = 1 you can visit any cell that shares a corner with (i, j) and value in that cell is 1.

More formally, from any cell (i, j) if A[i][j] = 1 you can visit:

(i-1, j) if (i-1, j) is inside the matrix and A[i-1][j] = 1.
(i, j-1) if (i, j-1) is inside the matrix and A[i][j-1] = 1.
(i+1, j) if (i+1, j) is inside the matrix and A[i+1][j] = 1.
(i, j+1) if (i, j+1) is inside the matrix and A[i][j+1] = 1.
(i-1, j-1) if (i-1, j-1) is inside the matrix and A[i-1][j-1] = 1.
(i+1, j+1) if (i+1, j+1) is inside the matrix and A[i+1][j+1] = 1.
(i-1, j+1) if (i-1, j+1) is inside the matrix and A[i-1][j+1] = 1.
(i+1, j-1) if (i+1, j-1) is inside the matrix and A[i+1][j-1] = 1.
Return the number of islands.

NOTE: Rows are numbered from top to bottom and columns are numbered from left to right.



Problem Constraints
1 <= N, M <= 100

0 <= A[i] <= 1



Input Format
The only argument given is the integer matrix A.



Output Format
Return the number of islands.



Example Input
Input 1:

 A = [ 
       [0, 1, 0]
       [0, 0, 1]
       [1, 0, 0]
     ]
Input 2:

 A = [   
       [1, 1, 0, 0, 0]
       [0, 1, 0, 0, 0]
       [1, 0, 0, 1, 1]
       [0, 0, 0, 0, 0]
       [1, 0, 1, 0, 1]    
     ]


Example Output
Output 1:

 2
Output 2:

 5


Example Explanation
Explanation 1:

 The 1's at position A[0][1] and A[1][2] forms one island.
 Other is formed by A[2][0].
Explanation 2:

 There 5 island in total.


"""


from collections import deque


def isValid(A, i, j, visited):
    rows = len(A)
    cols = len(A[0])
    
    if i>=0 and i<rows and j>=0 and j<cols and A[i][j] == 1 and visited[i][j] == False:
        return True
        
    return False


def bfs(A, i, j, visited):
    
    directions = [(-1,0), (0,-1), (1,0), (0,1), (-1,-1), (1,1), (-1,1), (1,-1)]
    queue = deque()
    
    queue.append((i, j))
    visited[i][j] = True
    
    while queue:
        x, y = queue.popleft()
        
        for d1, d2 in directions:
            row = x + d1
            col = y + d2
            
            if isValid(A, row, col, visited):
                visited[row][col] = True
                queue.append((row, col))
    
    

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        rows = len(A)
        cols = len(A[0])
        count = 0
        
        visited = [[False for j in range(cols)] for i in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
                if A[i][j] == 1 and visited[i][j] == False:
                    bfs(A, i, j, visited)
                    count += 1
                    
        return count
        
        