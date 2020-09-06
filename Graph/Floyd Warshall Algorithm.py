"""

Floyd Warshall Algorithm
Problem Description

Given a matrix of integers A of size N x N, where A[i][j] represents the weight of directed edge from i to j (i ---> j).

If i == j, A[i][j] = 0, and if there is no directed edge from vertex i to vertex j, A[i][j] = -1.

Return a matrix B of size N x N where B[i][j] = shortest path from vertex i to vertex j.

If there is no possible path from vertex i to vertex j , B[i][j] = -1

Note: Rows are numbered from top to bottom and columns are numbered from left to right.



Problem Constraints
1 <= N <= 200
-1 <= A[i][j] <= 1000000


Input Format
The first and only argument given is the integer matrix A.


Output Format
Return a matrix B of size N x N where B[i][j] = shortest path from vertex i to vertex j
If there is no possible path from vertex i to vertex j, B[i][j] = -1.


Example Input
A = [ [0 , 50 , 39]
          [-1 , 0 , 1]
          [-1 , 10 , 0] ]


Example Output
[ [0 , 49 , 39 ]
   [-1 , 0 , -1 ]
   [-1 , 10 , 0 ] ]


Example Explanation
Shortest Path from 1 to 2 would be 1 ---> 3 ---> 2 and not directly from 1 to 2,
All remaining distances remains same.


"""


class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):
        n = len(A)
        B = [[float("inf") for j in range(n)] for i in range(n)]
        
        for i in range(n):
			for j in range(n):
				if A[i][j] != -1:
                     B[i][j] = A[i][j]
                    
        for c in range(n):
            for i in range(n):
                for j in range(n):
                    if B[i][j] > B[i][c] + B[c][j]:
                        B[i][j] = B[i][c] + B[c][j]
                    
                        
        for i in range(n):
            for j in range(n):
                if B[i][j] == float("inf"):
                    B[i][j] = -1
                    
        return B
        
