"""

Valid Path
Problem Description

There is a rectangle with left bottom as (0, 0) and right up as (x, y).

There are N circles such that their centers are inside the rectangle.

Radius of each circle is R. Now we need to find out if it is possible that we can move from (0, 0) to (x, y) without touching any circle.

Note : We can move from any cell to any of its 8 adjecent neighbours and we cannot move outside the boundary of the rectangle at any point of time.



Problem Constraints
0 <= x , y, R <= 100

1 <= N <= 1000

Center of each circle would lie within the grid



Input Format
1st argument given is an Integer x , denoted by A in input.

2nd argument given is an Integer y, denoted by B in input.

3rd argument given is an Integer N, number of circles, denoted by C in input.

4th argument given is an Integer R, radius of each circle, denoted by D in input.

5th argument given is an Array A of size N, denoted by E in input, where A[i] = x cordinate of ith circle

6th argument given is an Array B of size N, denoted by F in input, where B[i] = y cordinate of ith circle



Output Format
Return YES or NO depending on weather it is possible to reach cell (x,y) or not starting from (0,0).



Example Input
Input 1:

 x = 2
 y = 3
 N = 1
 R = 1
 A = [2]
 B = [3]
Input 2:

 x = 1
 y = 1
 N = 1
 R = 1
 A = [1]
 B = [1]


Example Output
Output 1:

 NO
Output 2:

 NO


Example Explanation
Explanation 1:

 There is NO valid path in this case
Explanation 2:

 There is NO valid path in this case


"""


import math
from collections import deque


def valid(grid, rows, cols, i, j):
    if i>= 0 and i<rows and j>=0 and j<cols and grid[i][j] == 0:
        return True
    
    return False


def mark_cells_inside_circle(grid, rows, cols, C, D, E, F):
    
    for i in range(rows):
        for j in range(cols):
            for n in range(C):
                if math.sqrt((E[n]-i)**2 + (F[n]-j)**2) <= D:
                    grid[i][j] = -1
    

def bfs(grid, rows, cols):
    
    queue = deque()
    directions = [(-1,0), (0,-1), (1,0), (0,1), (-1,-1), (1,1), (-1,1), (1,-1)]
    
    queue.append((0, 0))
    grid[0][0] = 1
    
    while queue:
        i, j = queue.popleft()
        
        for d1, d2 in directions:
            x = i + d1
            y = j + d2
            
            if valid(grid, rows, cols, x, y):
                queue.append((x, y))
                grid[x][y] = 1


class Solution:
	# @param A : integer
	# @param B : integer
	# @param C : integer
	# @param D : integer
	# @param E : list of integers
	# @param F : list of integers
	# @return a strings
	def solve(self, A, B, C, D, E, F):
	    rows = A + 1
	    cols = B + 1
	    
	    grid = [[0 for j in range(cols)] for i in range(rows)]
	    
	    mark_cells_inside_circle(grid, rows, cols, C, D, E, F)
	    
	    if grid[0][0] == -1 or grid[-1][-1] == -1:
	        return "NO"
	    
	    bfs(grid, rows, cols)
	    
	    if grid[-1][-1] == 1:
	        return "YES"
	        
	    return "NO"
	    
	    
