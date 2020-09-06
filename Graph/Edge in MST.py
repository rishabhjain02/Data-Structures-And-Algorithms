"""

Edge in MST
Problem Description

Given a undirected weighted graph with A nodes labelled from 1 to A with M edges given in a form of 2D-matrix B of size M * 3 where B[i][0] and B[i][1] denotes the two nodes connected by an edge of weight B[i][2].

For each edge check whether it belongs to any of the possible minimum spanning tree or not , return 1 if it belongs else return 0.

Return an one-dimensional binary array of size M denoting answer for each edge.

NOTE:

The graph may be disconnected in that case consider mst for each component.
No self-loops and no multiple edges present.
Answers in output array must be in order with the input array B output[i] must denote the answer of edge B[i][0] to B[i][1].


Problem Constraints
1 <= A, M <= 3*10^5

1 <= B[i][0], B[i][1] <= A

1 <= B[i][1] <= 10^3



Input Format
The first argument given is an integer A representing the number of nodes in the graph.

The second argument given is an matrix B of size M x 3 which represents the M edges such that there is a edge between node B[i][0] and node B[i][1] with weight B[i][2].



Output Format
Return an one-dimensional binary array of size M denoting answer for each edge.



Example Input
Input 1:

 A = 3
 B = [ [1, 2, 2]
       [1, 3, 2]
       [2, 3, 3]
     ]


Example Output
Output 1:

 [1, 1, 0]


Example Explanation
Explanation 1:

 Edge (1, 2) with weight 2 is included in the MST           1
                                                          /   \
                                                         2     3
 Edge (1, 3) with weight 2 is included in the same MST mentioned above.
 Edge (2,3) with weight 3 cannot be included in any of the mst possible.
 So we will return [1, 1, 0]


"""


from collections import defaultdict

class DSU:
    
    def __init__(self, vertices):
        self.parent = [i for i in range(vertices+1)]
        self.size = [0]*(vertices+1)
        
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
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        n = len(B)
        ans = [0]*(n)
        hashmap = defaultdict(int)
        
        for i in range(n):
            u = B[i][0]
            v = B[i][1]
            hashmap[(u, v)] = i
        
        B.sort(key = lambda x : x[2])
	    dsu = DSU(A)
	    
	    i = 0
	    
	    while i < n:
	        j = i
	        
	        # Finding count of edges with same weight
	        while j < n and B[j][2] == B[i][2]:
	            j += 1
	            
	        # For same weight edges, first check whether they can be added to MST or not
	        # We are not adding the edge to MST here, we are only finding the ans for that edge
	        for k in range(i, j):
	            u = B[k][0]
	            v = B[k][1]
	            
	            if dsu.find(u) != dsu.find(v):
	                index = hashmap[(u, v)]
	                ans[index] = 1
	        
	        # Now adding the same weight edges to the MST
	        for k in range(i, j):
	            u = B[k][0]
	            v = B[k][1]
	            
	            if dsu.find(u) != dsu.find(v):
	                dsu.union(u, v)       
	        
	        i = j
	            
	    return ans
        
        
