"""

Matrix and Absolute Difference
Problem Description

Given a matrix C of integers, of dimension A x B.

For any given K, you are not allowed to travel between cells that have an absolute difference greater than K.

Return the minimum value of K such that it is possible to travel between any pair of cells in the grid through a path of adjacent cells.

NOTE:

Adjacent cells are those cells that share a side with the current cell.


Problem Constraints
1 <= A, B <= 10^2

1 <= C[i][j] <= 10^9



Input Format
The first argument given is A.

The second argument give is B.

The third argument given is the integer matrix C.



Output Format
Return a single integer, the minimum value of K.



Example Input
Input 1:

 A = 3
 B = 3
 C = [  [1, 5, 6]
        [10, 7, 2]
        [3, 6, 9]   ]


Example Output
Output 1:

 4


Example Explanation
Explanation 1:

 
 It is possible to travel between any pair of cells through a path of adjacent cells that do not have an absolute
 difference in value greater than 4. e.g. : A path from (0, 0) to (2, 2) may look like this:
 => (0, 0) -> (0, 1) -> (1, 1) -> (2, 1) -> (2, 2)


"""


# Make a list of edges as for each cell one edge will be between it and horizontal right neighbour
# and second edge will be between it and vertical down neighbour and weight will be absolute diff
# between the values present in the cells in matrix C
# Apply Kruskal and find max weight edge in the Min spanning tree

class DSU:
    
    def __init__(self, vertices):
        self.parent = [i for i in range(vertices)]
        self.size = [0]*(vertices)
        
    def find(self, node):
        if self.parent[node] == node:
            return node
        
        root = self.find(self.parent[node])
        self.parent[node] = root
        return root
        
    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        
        if self.size[xroot] < self.size[yroot]: 
            self.parent[xroot] = yroot 
            
        elif self.size[xroot] > self.size[yroot]: 
            self.parent[yroot] = xroot 
            
        else : 
            self.parent[yroot] = xroot 
            self.size[xroot] += 1

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of list of integers
    # @return an integer
    def solve(self, A, B, C):
        dsu = DSU(A*B)
        graph = []
        ans = float("-inf")
                
        for i in range(A):
            for j in range(B):
                u = i*B + j
                
                if j < B-1:
                    v = i*B + (j+1)
                    w = abs(C[i][j+1] - C[i][j])
                    graph.append([u, v, w])
                    
                if i < A-1:
                    v = (i+1)*B + j
                    w = abs(C[i+1][j] - C[i][j])
                    graph.append([u, v, w])
                    
                    
        graph.sort(key = lambda x: x[2])
        
        for u, v, w in graph:
            if dsu.find(u) != dsu.find(v):
                ans = max(ans, w)
                dsu.union(u, v)
        
        return ans
        
