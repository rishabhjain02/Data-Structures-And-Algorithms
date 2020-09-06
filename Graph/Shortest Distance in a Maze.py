"""

Shortest Distance in a Maze
Problem Description

Given a matrix of integers A of size N x M describing a maze. The maze consists of empty locations and walls.

1 represents a wall in a matrix and 0 represents an empty location in a wall.

There is a ball trapped in a maze. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall (maze boundary is also considered as a wall). When the ball stops, it could choose the next direction.

Given two array of integers of size B and C of size 2 denoting the starting and destination position of the ball.

Find the shortest distance for the ball to stop at the destination. The distance is defined by the number of empty spaces traveled by the ball from the starting position (excluded) to the destination (included). If the ball cannot stop at the destination, return -1.



Problem Constraints
2 <= N, M <= 100

0 <= A[i] <= 1

0 <= B[i][0], C[i][0] < N

0 <= B[i][1], C[i][1] < M



Input Format
The first argument given is the integer matrix A.

The second argument given is an array of integer B.

The third argument if an array of integer C.



Output Format
Return a single integer, the minimum distance required to reach destination



Example Input
Input 1:

A = [ [0, 0], [0, 0] ]
B = [0, 0]
C = [0, 1]
Input 2:

A = [ [0, 0], [0, 1] ]
B = [0, 0]
C = [0, 1]


Example Output
Output 1:

 1
Output 2:

 1


Example Explanation
Explanation 1:

 Go directly from start to destination in distance 1.
Explanation 2:

 Go directly from start to destination in distance 1.

"""


from collections import deque


def valid(A, i, j):
    rows = len(A)
    cols = len(A[0])
    
    if i>=0 and i<rows and j>=0 and j<cols and A[i][j] == 0:
        return True
        
    return False


def bfs(distance, A, s, d):
    queue = deque()
    directions = [(0,1), (0,-1), (1,0), (-1,0)]
    
    distance[s[0]][s[1]] = 0
    queue.append((s[0], s[1]))
    
    while queue:
        i, j = queue.popleft()
        
        for d1, d2 in directions:
            x = i
            y = j
            count = 0
            
            while valid(A, x+d1, y+d2):
                x += d1
                y += d2
                count += 1
            
            if distance[i][j] + count < distance[x][y]:
                distance[x][y] = distance[i][j] + count
                queue.append((x, y))


class Solution:
    # @param A : list of list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        if A[C[0]][C[1]] == 1:
            return -1
            
        rows = len(A)
        cols = len(A[0])
        distance = [[float("inf") for j in range(cols)] for i in range(rows)]
        
        bfs(distance, A, B, C)
        
        if distance[C[0]][C[1]] == float("inf"):
            return -1
            
        return distance[C[0]][C[1]]
        
