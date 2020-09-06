"""

Construction Cost
Problem Description

Given a graph with A nodes and C weighted edges. Cost of constructing the graph is the sum of weights of all the edges in the graph.

Find the minimum cost of constructing the graph by selecting some given edges such that we can reach every other node from the 1st node.

NOTE: Return the answer modulo 10^9+7 as the answer can be large.



Problem Constraints
1 <= A <= 100000
0 <= C <= 100000
1 <= B[i][0], B[i][1] <= N
1 <= B[i][2] <= 10^9



Input Format
First argument is an integer A.
Second argument is a 2-D integer array B of size C*3 denoting edges. B[i][0] and B[i][1] are connected by ith edge with weight B[i][2]



Output Format
Return an integer denoting the minimum construction cost.



Example Input
Input 1:

A = 3
B = [   [1, 2, 14]
        [2, 3, 7]
        [3, 1, 2]   ]
Input 2:

A = 3
B = [   [1, 2, 20]
        [2, 3, 17]  ]


Example Output
Output 1:

9
Output 2:

37


Example Explanation
Explanation 1:

We can take only two edges (2 -> 3 and 3 -> 1) to construct the graph. we can reach the 1st node from 2nd and 3rd node using only these two edges.
So, the total cost of costruction is 9.
Explanation 2:

We have to take both the given edges so that we can reach the 1st node from 2nd and 3rd node.


"""


from collections import defaultdict
import heapq

def make_adjacency_list(graph, B):
    for u, v, w in B:
        graph[u].append((v, w))
        graph[v].append((u, w))
        
def prims(graph, visited, ans):
    minheap = []
    heapq.heappush(minheap, (0, 1))
    
    while minheap:
        cost, node = heapq.heappop(minheap)
        
        if visited[node] == False:
            visited[node] = True
            ans[0] = (ans[0] + cost) % (10**9+7)
            
            for neighbour, weight in graph[node]:
                if visited[neighbour] == False:
                    heapq.heappush(minheap, (weight, neighbour))
        

class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        graph = defaultdict(list)
        visited = [False]*(A+1)
        ans = [0]
        
        make_adjacency_list(graph, B)
        
        prims(graph, visited, ans)
        
        return ans[0]
        
