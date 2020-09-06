"""

Another BFS
Problem Description

Given a weighted undirected graph having A nodes, a source node C and destination node D.

Find the shortest distance from C to D and if it is impossible to reach node D from C then return -1.

You are expected to do it in Time Complexity of O(A + M).

Note:

There are no self-loops in the graph.

No multiple edges between two pair of vertices.

The graph may or may not be connected.

Nodes are Numbered from 0 to A-1.

Your solution will run on multiple testcases. If you are using global variables make sure to clear them.



Problem Constraints
1 <= A <= 10^5

0 <= B[i][0], B[i][1] < A

1 <= B[i][2] <= 2

0 <= C < A

0 <= D < A



Input Format
The first argument given is an integer A, representing the number of nodes.

The second argument given is the matrix B, where B[i][0] and B[i][1] are connected through an edge of weight B[i][2].

The third argument given is an integer C, representing the source node.

The fourth argument is an integer D, representing the destination node.

Note: B[i][2] will be either 1 or 2.



Output Format
Return the shortest distance from C to D. If it is impossible to reach node D from C then return -1.



Example Input
Input 1:

 
A = 6
B = [   [2, 5, 1]
        [1, 3, 1] 
        [0, 5, 2] 
        [0, 2, 2] 
        [1, 4, 1] 
        [0, 1, 1] ] 
C = 3
D = 2
Input 2:

A = 2
B = [   [0, 1, 1]
    ] 
C = 0
D = 1


Example Output
Output 1:

 4
Output 2:

 1


Example Explanation
Explanation 1:

The path to be followed will be:
    3 -> 1 (Edge weight : 1)
    1 -> 0 (Edge weight : 1)
    0 -> 2 (Edge weight : 2)
Total length of path = 1 + 1 + 2 = 4.
Explanation 2:

 Path will be 0-> 1.

"""


from collections import defaultdict, deque

def make_adjacency_list(graph, B, x):
    for u, v, w in B:
        
        # As this is undirected graph, add nodes in each other's adjacency list
        if w == 1:
            graph[u].append(v)
            graph[v].append(u)
            
        # In case of Weight = 2, add one temp node and make two edges of 1 weight each    
        else:
            graph[u].append(x)
            graph[x].append(u)
            graph[x].append(v)
            graph[v].append(x)
            x += 1
    
    return x

# Finding min cost from the parent array
def find_min_cost(parent, dst, ans):
    while dst >= 0:
        ans[0] += 1
        dst = parent[dst]
    

def bfs(graph, src, dst, visited, parent, ans):
    queue = deque()
    
    queue.append(src)
    visited[src] = True
    
    while queue:
        v = queue.popleft()
        
        if v == dst:
            
            # If we reach destination then, find the min cost
            find_min_cost(parent, dst, ans)
            return
            
        for i in graph[v]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
                
                # Adding parent of i node
                parent[i] = v
                
    

class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @param C : integer
    # @param D : integer
    # @return an integer
    def solve(self, A, B, C, D):
        ans = [-1]
        graph = defaultdict(list)
        
        n = make_adjacency_list(graph, B, A)
        
        visited = [False]*n

        parent = [-1]*n

        bfs(graph, C, D, visited, parent, ans)
        
        return ans[0]
        
        
