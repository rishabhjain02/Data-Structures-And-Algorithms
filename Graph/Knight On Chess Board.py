"""

Knight On Chess Board
Problem Description

Given any source point, (C, D) and destination point, (E, F) on a chess board of size A x B, we need to find whether Knight can move to the destination or not.

Figure: https://i.imgur.com/c2ptefU.jpeg

The above figure details the movements for a knight ( 8 possibilities ).

If yes, then what would be the minimum number of steps for the knight to move to the said point. If knight can not move from the source point to the destination point, then return -1.

NOTE: A knight cannot go out of the board.



Problem Constraints
1 <= A, B <= 500



Input Format
The first argument of input contains an integer A.
The second argument of input contains an integer B.
The third argument of input contains an integer C.
The fourth argument of input contains an integer D.
The fifth argument of input contains an integer E.
The sixth argument of input contains an integer F.



Output Format
If it is possible to reach the destination point, return the minimum number of moves.
Else return -1.



Example Input
Input 1:

 A = 8
 B = 8
 C = 1
 D = 1
 E = 8
 F = 8
Input 2:

 A = 2
 B = 4
 C = 2
 D = 1
 E = 4
 F = 4


Example Output
Output 1:

 6
Output 2:

 -1


Example Explanation
Explanation 1:

 The size of the chessboard is 8x8, the knight is initially at (1, 1) and the knight wants to reach position (8, 8).
 The minimum number of moves required for this is 6.
Explanation 2:

 It is not possible to move knight to position (4, 4) from (2, 1)


"""


from collections import deque


def valid(rows, cols, i, j, visited):
    if i>=0 and i<rows and j>=0 and j<cols and visited[i][j] == False:
        return True
        
    return False
    

def bfs(rows, cols, C, D, E, F, steps, visited):
    queue = deque()
    directions = [(-2,-1), (-2,1), (-1,-2), (-1,2), (2,-1), (2,1), (1,-2), (1,2)]
    
    queue.append((C-1, D-1, 0))
    visited[C-1][D-1] = True
    
    while queue:
        i, j, dist = queue.popleft()
        
        if i == E-1 and j == F-1:
            steps[0] = dist
            return True
        
        for d1, d2 in directions:
            x = i + d1
            y = j + d2
            
            if valid(rows, cols, x, y, visited):
                queue.append((x, y, dist + 1))
                visited[x][y] = True
    

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @param E : integer
    # @param F : integer
    # @return an integer
    def knight(self, A, B, C, D, E, F):
        rows = A
        cols = B
        steps = [0]
        
        visited = [[False for j in range(cols)] for i in range(rows)]
        
        if bfs(rows, cols, C, D, E, F, steps, visited):
            return steps[0]
            
        return -1

