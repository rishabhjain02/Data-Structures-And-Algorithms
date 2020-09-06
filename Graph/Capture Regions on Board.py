"""

Capture Regions on Board
Problem Description

Given a 2-D board A of size N x M containing 'X' and 'O', capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.



Problem Constraints
1 <= N, M <= 1000



Input Format
First and only argument is a N x M character matrix A.



Output Format
Make changes to the the input only as matrix is passed by reference.



Example Input
Input 1:

 A = [ 
       [X, X, X, X],
       [X, O, O, X],
       [X, X, O, X],
       [X, O, X, X] 
     ]
Input 2:

 A = [
       [X, O, O],
       [X, O, X],
       [O, O, O]
     ]


Example Output
Output 1:

 After running your function, the board should be:
 A = [
       [X, X, X, X],
       [X, X, X, X],
       [X, X, X, X],
       [X, O, X, X]
     ]
Output 2:

 After running your function, the board should be:
 A = [
       [X, O, O],
       [X, O, X],
       [O, O, O]
     ]


Example Explanation
Explanation 1:

 O in (4,2) is not surrounded by X from below.
Explanation 2:

 No O's are surrounded.


"""


from collections import deque

def valid(A, i, j, visited):
    rows = len(A)
    cols = len(A[0])
    
    if i>=0 and i<rows and j>=0 and j<cols and A[i][j] == 'O':
        return True
        
    return False
    

def bfs(A, visited, i, j):
    queue = deque()
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    
    queue.append((i, j))
    A[i][j] = 'Y'
    
    while queue:
        x, y = queue.popleft()
        A[x][y] = 'Y'
        
        for d1, d2 in directions:
            row = x + d1
            col = y + d2
            
            if valid(A, row, col, visited):
                queue.append((row, col))
    

# We are traversing First column, Last column, First row and Last row and if 'O' if found:
# We do bfs starting from thatin the four directions for adjacent 'O' and mark them 'Y'
# These 'Y' marked cells can not be captured by 'X'
class Solution:
    # @param A : list of list of chars
    def solve(self, A):
        rows = len(A)
        cols = len(A[0])
        
        visited = [[False for j in range(cols)] for i in range(rows)]
        
        for j in range(cols):
            if A[0][j] == 'O':
                bfs(A, visited, 0, j)
                
        for j in range(cols):
            if A[rows-1][j] == 'O':
                bfs(A, visited, rows-1, j)
                
        for i in range(rows):
            if A[i][0] == 'O':
                bfs(A, visited, i, 0)
                
        for i in range(rows):
            if A[i][cols-1] == 'O':
                bfs(A, visited, i, cols-1)

                
        for i in range(rows):
            for j in range(cols):
                if A[i][j] == 'Y':
                    A[i][j] = 'O'
                    
                elif A[i][j] == 'O':
                    A[i][j] = 'X'
                
        return A


