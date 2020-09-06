"""

Rotten Oranges
Problem Description

Given a matrix of integers A of size N x M consisting of 0, 1 or 2.

Each cell can have three values:

The value 0 representing an empty cell.

The value 1 representing a fresh orange.

The value 2 representing a rotten orange.

Every minute, any fresh orange that is adjacent (Left, Right, Top, or Bottom) to a rotten orange becomes rotten. Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1 instead.

Note: Your solution will run on multiple test cases. If you are using global variables, make sure to clear them.



Problem Constraints
1 <= N, M <= 1000

0 <= A[i][j] <= 2



Input Format
The first argument given is the integer matrix A.



Output Format
Return the minimum number of minutes that must elapse until no cell has a fresh orange.

If this is impossible, return -1 instead.



Example Input
Input 1:

A = [   [2, 1, 1]
        [1, 1, 0]
        [0, 1, 1]   ]
Input 2:

 
A = [   [2, 1, 1]
        [0, 1, 1]
        [1, 0, 1]   ]


Example Output
Output 1:

 4
Output 2:

 -1


Example Explanation
Explanation 1:

 Max of 4 using (0,0) , (0,1) , (1,1) , (1,2) , (2,2)
Explanation 2:

 Task is impossible

"""


from collections import deque

def valid(A, visited, i, j, rows, cols):
    if i>=0 and i<rows and j>=0 and j<cols and A[i][j] == 1 and visited[i][j] == False:
        return True
        
    return False
    

def bfs(A, visited, rows, cols, ans):
    queue = deque()
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    
    for i in range(rows):
        for j in range(cols):
            if A[i][j] == 2:
                queue.append((i, j, 0))
                
    while queue:
        i, j, time = queue.popleft()
        ans[0] = max(ans[0], time)
        
        for d1, d2 in directions:
            x = i + d1
            y = j + d2
            
            if valid(A, visited, x, y, rows, cols):
                queue.append((x, y, time+1))
                visited[x][y] = True
        

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        rows = len(A)
        cols = len(A[0])
        
        visited = [[False for j in range(cols)] for i in range(rows)]
        ans = [0]
        
        bfs(A, visited, rows, cols, ans)
        
        for i in range(rows):
            for j in range(cols):
                if A[i][j] == 1 and visited[i][j] == False:
                    return -1
        
        return ans[0]
        
