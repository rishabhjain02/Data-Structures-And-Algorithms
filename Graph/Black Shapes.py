"""

Black Shapes
Problem Description

Given character matrix A of O's and X's, where O = white, X = black.

Return the number of black shapes. A black shape consists of one or more adjacent X's (diagonals not included)



Problem Constraints
1 <= |A|,|A[0]| <= 1000

A[i][j] = 'X' or 'O'



Input Format
The First and only argument is character matrix A.



Output Format
Return a single integer denoting number of black shapes.



Example Input
Input 1:

 A = [ [X, X, X], [X, X, X], [X, X, X] ]
Input 2:

 A = [ [X, O], [O, X] ]


Example Output
Output 1:

 1
Output 2:

 2


Example Explanation
Explanation 1:

 All X's belong to single shapes
Explanation 2:

 Both X's belong to different shapes


"""


from collections import deque


def isValid(A, i, j, visited):
    rows = len(A)
    cols = len(A[0])
    
    if i>=0 and i<rows and j>=0 and j<cols and A[i][j] == 'X' and visited[i][j] == False:
        return True
        
    return False


def bfs(A, i, j, visited):
    
    directions = [(-1,0), (0,-1), (1,0), (0,1)]
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
	# @param A : list of strings
	# @return an integer
	def black(self, A):
	    rows = len(A)
        cols = len(A[0])
        count = 0
        
        visited = [[False for j in range(cols)] for i in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
                if A[i][j] == 'X' and visited[i][j] == False:
                    bfs(A, i, j, visited)
                    count += 1
                    
        return count
	    
