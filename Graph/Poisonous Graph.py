"""

Poisonous Graph
Problem Description

You are given an undirected unweighted graph consisting of A vertices and M edges given in a form of 2D Matrix B of size M x 2 where (B[i][0], B][i][1]) denotes two nodes connected by an edge.

You have to write a number on each vertex of the graph. Each number should be 1, 2 or 3. The graph becomes Poisonous if for each edge the sum of numbers on vertices connected by this edge is odd.

Calculate the number of possible ways to write numbers 1, 2 or 3 on vertices so the graph becomes poisonous. Since this number may be large, return it modulo 998244353.

NOTE:

Note that you have to write exactly one number on each vertex.
The graph does not have any self-loops or multiple edges.
Nodes are labelled from 1 to A.


Problem Constraints
1 <= A <= 3*10^5

0 <= M <= 3*10^5

1 <= B[i][0], B[i][1] <= A

B[i][0] != B[i][1]



Input Format
First argument is an integer A denoting the number of nodes.

Second argument is an 2D Matrix B of size M x 2 denoting the M edges.



Output Format
Return one integer denoting the number of possible ways to write numbers 1, 2 or 3 on the vertices of given graph so it becomes Poisonous . Since answer may be large, print it modulo 998244353.



Example Input
Input 1:

 A = 2
 B = [  [1, 2]
     ]
Input 2:

 A = 4
 B = [  [1, 2]
        [1, 3]
        [1, 4]
        [2, 3]
        [2, 4]
        [3, 4]
    ]


Example Output
Output 1:

 4
Output 2:

 0


Example Explanation
Explanation 1:

 There are 4 ways to make the graph poisonous. i.e, writing number on node 1 and 2 as,
    [1, 2] , [3, 2], [2, 1] or [2, 3] repsectively.
Explanation 2:

 There is no way to make the graph poisonous.

"""


from collections import defaultdict, deque


def power(x, y, p) : 
    res = 1     
      
    while (y > 0) : 
          
        if (y%2 == 1) : 
            res = (res * x) % p 
  
        y = y//2 
        x = (x * x) % p 
          
    return res


def make_adjacency_list(graph, B):
    for u, v in B:
        graph[u].append(v)
        graph[v].append(u)
        
        
def bipartite(graph, visited, source, color1_count, color2_count, color):
    queue = deque()
    queue.append(source)
    color[source] = 0
    visited[source] = True
    
    while queue:
        parent = queue.popleft()
        
        if color[parent] == 0:
            color1_count += 1
            
        elif color[parent] == 1:
            color2_count += 1
        
        for neighbour in graph[parent]:
            if visited[neighbour] == False:
                queue.append(neighbour)
                color[neighbour] = color[parent] ^ 1
                visited[neighbour] = True
                
            elif color[neighbour] == color[parent]:
                return False, color1_count, color2_count
                
    return True, color1_count, color2_count


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        graph = defaultdict(list)
        visited = [False]*(A+1)
        color = [-1]*(A+1)
        ans = 1
        count = 0
        mod = 998244353
        
        if len(B) == 0:
            return power(3, A, mod)
        
        make_adjacency_list(graph, B)
        
        for i in range(1, A+1):
            color1_count = 0
            color2_count = 0
            
            
            if visited[i] == False:
                flag, color1_count, color2_count = bipartite(graph, visited, i, color1_count, color2_count, color)
                
                if not flag:
                    return 0
                
                else:
                    if color2_count == 0:
                        ans = (ans * power(3, color1_count, mod))%mod
                    else:
                        ans = ( ans * (power(2, color1_count, mod) + power(2, color2_count, mod))%mod )%mod
            
        return ans
        
