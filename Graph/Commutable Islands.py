"""

Commutable Islands
Problem Description

There are A islands and there are M bridges connecting them. Each bridge has some cost attached to it.

We need to find bridges with minimal cost such that all islands are connected.

It is guaranteed that input data will contain at least one possible scenario in which all islands are connected with each other.



Problem Constraints
1 <= A, M <= 6*10^4

1 <= B[i][0], B[i][1] <= A

1 <= B[i][2] <= 10^3



Input Format
The first argument contains an integer, A, representing the number of islands.

The second argument contains an 2-d integer matrix, B, of size M x 3 where Island B[i][0] and B[i][1] are connected using a bridge of cost B[i][2].



Output Format
Return an integer representing the minimal cost required.



Example Input
Input 1:

 A = 4
 B = [  [1, 2, 1]
        [2, 3, 4]
        [1, 4, 3]
        [4, 3, 2]
        [1, 3, 10]  ]
Input 2:

 A = 4
 B = [  [1, 2, 1]
        [2, 3, 2]
        [3, 4, 4]
        [1, 4, 3]   ]


Example Output
Output 1:

 6
Output 2:

 6


Example Explanation
Explanation 1:

 We can choose bridges (1, 2, 1), (1, 4, 3) and (4, 3, 2), where the total cost incurred will be (1 + 3 + 2) = 6.
Explanation 2:

 We can choose bridges (1, 2, 1), (2, 3, 2) and (1, 4, 3), where the total cost incurred will be (1 + 2 + 3) = 6.


"""


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
	# @return an integer
	def solve(self, A, B):
	    min_cost = 0
	    
	    B.sort(key = lambda x : x[2])
	    dsu = DSU(A)
	    
	    for u, v, w in B:
	        if dsu.find(u) != dsu.find(v):
	            min_cost += w
	            dsu.union(u, v)
	            
	    return min_cost
	    
	    
