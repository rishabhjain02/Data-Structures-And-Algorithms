"""

Minimum Weighted Cycle
Problem Description

Given an integer A, representing number of vertices in a graph.

Also you are given a matrix of integers B of size N x 3 where N represents number of Edges in a Graph and Triplet (B[i][0], B[i][1], B[i][2]) implies there is an undirected edge between B[i][0] and B[i][1] and weight of that edge is

B[i][2].

Find and return the weight of minimum weighted cycle and if there is no cycle return -1 instead.

NOTE: Graph may contain multiple edges and self loops.



Problem Constraints
1 <= A <= 1000

1 <= B[i][0], B[i][1] <= A

1 <= B[i][2] <= 100000



Input Format
The first argument given is the integer A.

The second argument given is the integer matrix B.



Output Format
Return the weight of minimum weighted cycle and if there is no cycle return -1 instead.



Example Input
Input 1:

 A = 4
 B = [  [1 ,2 ,2]
        [2 ,3 ,3]
        [3 ,4 ,1]
        [4 ,1 ,4]
        [1 ,3 ,15]  ]
Input 2:

 A = 3
 B = [  [1 ,2 ,2]
        [2 ,3 ,3]  ]


Example Output
Output 1:

 10 
Output 2:

 -1


Example Explanation
Explanation 1:

 Given graph forms 3 cycles
 1. 1 ---> 2 ---> 3 ---> 4 ---> 1 weight = 10
 2. 1 ---> 2 ---> 3 ---> 1 weight = 20
 3. 1 ---> 3---> 4 ---> 1 weight = 20
 so answer would be 10.
Explanation 2:

 Given graph forms 0 cycles so return -1.

"""


from collections import defaultdict
import heapq

def make_adjacency_list(graph, B):
    for u, v, w in B:
        graph[u].append((v, w))
        graph[v].append((u, w))
     
# Finding shortest path bw source and dest        
def Dijsktra(A, graph, source, dest):
    visited = [False]*(A+1)
    distance = [float("inf")]*(A+1)
    minheap = []
    
    distance[source] = 0
    heapq.heappush(minheap, (0, source))
    
    while minheap:
        parent_dist, parent_node = heapq.heappop(minheap)
        
        if parent_node == dest:
            return distance[dest]
            
        visited[parent_node] = True
            
        for neighbour, weight in graph[parent_node]:
            if visited[neighbour] == False:
                cur_dist = parent_dist + weight
                    
                if cur_dist < distance[neighbour]:
                    distance[neighbour] = cur_dist
                    heapq.heappush(minheap, (cur_dist, neighbour))
    
    # If destination is not reachable from source, return inf 
    return float("inf")
    
class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        graph = defaultdict(list)
        min_weight_cycle = float("inf")
        
        make_adjacency_list(graph, B)
        
        for u, v, w in B:
            
            # Removing the edge from graph
            graph[u].remove((v, w))
            graph[v].remove((u, w))
            
            # Finding shortest distance bw u and v after removal of that edge
            dist = Dijsktra(A, graph, u, v)
            
            # Updating min_weight_cycle as shortest dist + weight of removed edge
            min_weight_cycle = min(min_weight_cycle, dist + w)
            
            # Adding back that in the graph
            graph[u].append((v, w))
            graph[v].append((u, w))
            
        # If finally min_weight_cycle is inf, so no cycle is found    
        if min_weight_cycle == float("inf"):
            return -1
            
        return min_weight_cycle
        
        
