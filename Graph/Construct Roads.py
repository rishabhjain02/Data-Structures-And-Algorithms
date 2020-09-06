"""

Construct Roads
Problem Description

A country consist of N cities connected by N - 1 roads. King of that country want to construct maximum number of roads such that the new country formed remains bipartite country.

Bipartite country is a country, whose cities can be partitioned into 2 sets in such a way, that for each road (u, v) that belongs to the country, u and v belong to different sets. Also, there should be no multiple roads between two cities and no self loops.

Return the maximum number of roads king can construct. Since the answer could be large return answer % 109 + 7.

NOTE: All cities can be visited from any city.



Problem Constraints
1 <= A <= 10^5

1 <= B[i][0], B[i][1] <= N



Input Format
First argument is an integer A denoting the number of cities, N.

Second argument is a 2D array B of size (N-1) x 2 denoting the initial roads i.e. there is a road between cities B[i][0] and B[1][1] .



Output Format
Return an integer denoting the maximum number of roads king can construct.



Example Input
Input 1:

 A = 3
 B = [
       [1, 2]
       [1, 3]
     ]
Input 2:

 A = 5
 B = [
       [1, 3]
       [1, 4]
       [3, 2]
       [3, 5]
     ]


Example Output
Output 1:

 0
Output 2:

 2


Example Explanation
Explanation 1:

 We can't construct any new roads such that the country remains bipartite.
Explanation 2:

 We can add two roads between cities (1, 2) and (1, 5).

"""


# Color the graph with two colors c1, c2
# Count nodes with c1 color and c2 color
# total edges = count_c1 * count*c2
# Edges that can be added = total edges - given n-1 edges

from collections import defaultdict, deque


def make_adjacency_list(graph, B):
    for u, v in B:
        graph[u].append(v)
        graph[v].append(u)


def bfs(graph, visited, color, source):
    queue = deque()
    queue.append(source)
    visited[source-1] = True
    color[source-1] = 0
    
    while queue:
        parent = queue.popleft()
        
        for neighbour in graph[parent]:
            if visited[neighbour-1] == False:
                queue.append(neighbour)
                color[neighbour-1] = color[parent-1] ^ 1
                visited[neighbour-1] = True


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        graph = defaultdict(list)
        visited = [False]*A
        color = [0]*A
        color1_count = 0
        color2_count = 0
        mod = 10**9+7
        
        make_adjacency_list(graph, B)
        
        bfs(graph, visited, color, 1)
        
        for c in color:
            if c == 0:
                color1_count += 1
            else:
                color2_count += 1
                
        return (color1_count%mod * color2_count%mod) % mod - (A - 1)
        
        
