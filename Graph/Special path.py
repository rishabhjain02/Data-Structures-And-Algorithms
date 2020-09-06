"""

Special path
Problem Description

Given a graph with N nodes numbered 1 to N and M weighted edges. Given a binary array A of size N. A[i] = 1 if the ith node is special else 0.

Find the minimum distance of the special path between the 1st and the Nth node. Distance between two nodes is defined as the sum of the weight of edges in the path.

A special path is a path which visits alteast C non-special nodes and atleast D special nodes.

NOTE: A node or edge can occur multiple times in a special path. If no such path exists return -1.



Problem Constraints
1 <= N, M <= 10000
0 <= A[i] <= 1
1 <= B[i][0], B[i][1] <= N
1 <= B[i][2] <= 100000
0 <= C, D <= 10



Input Format
First argument is an integer array A of size N
Second argument is a 2-D integer array B of size M*3 denoting edges. B[i][0] and B[i][1] are connected by ith edge with weight B[i][2]
Third argument is an integer C
Fourth argument is an integer D



Output Format
Return an integer denoting the minimum distance of the special path. Return -1 if no such path exists.



Example Input
Input 1:

A = [0, 1, 0]
B = [ [1, 2, 3], [2, 3, 5] ] 
C = 2
D = 3
Input 2:

A = [1, 1]
B = [ [1, 2, 1] ]
C = 1
D = 1


Example Output
Output 1:

 20
Output 2:

 -1


Example Explanation
Explanation 1:

 Minimum distance of the special path is 20 ( 1 -> 2 -> 1 -> 2 -> 1 -> 2 -> 3).
 Number of visits of non-special nodes = 4 (1, 1, 1, 3)
 Number of visits of special nodes = 3 (2, 2, 2)
Explanation 2:

 Cannot be achieved.

"""



from collections import defaultdict, deque

def make_adjacency_list(graph, B):
    for u, v, w in B:
        graph[u].append((v, w))
        graph[v].append((u, w))

    
def find_min_dist_path(A, graph, dist, C, D):
    queue = deque()
    
    if A[0] == 1:
        queue.append((1, 0, min(1, D)))
        dist[1][0][min(1, D)] = 0
        
    else:
        queue.append((1, min(1, C), 0))
        dist[1][min(1, C)][0] = 0
        
    while queue:
        node, non_sp, sp = queue.popleft()
        
        for neighbour, weight in graph[node]:
            
            if A[neighbour-1] == 1:
                new_sp = min(sp+1, D)
                if dist[neighbour][non_sp][new_sp] > dist[node][non_sp][sp] + weight:
                    dist[neighbour][non_sp][new_sp] = dist[node][non_sp][sp] + weight
                    queue.append((neighbour, non_sp, new_sp))
                    
            else:
                new_non_sp = min(non_sp+1, C)
                if dist[neighbour][new_non_sp][sp] > dist[node][non_sp][sp] + weight:
                    dist[neighbour][new_non_sp][sp] = dist[node][non_sp][sp] + weight
                    queue.append((neighbour, new_non_sp, sp))


class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @param C : integer
    # @param D : integer
    # @return an integer
    def solve(self, A, B, C, D):
        n = len(A)
        graph = defaultdict(list)
        
        make_adjacency_list(graph, B)
        
        dist = [[[float("inf") for k in range(D+1)] for j in range(C+1)] for i in range(n+1)]
        
        find_min_dist_path(A, graph, dist, C, D)
        
        if dist[n][C][D] == float("inf"):
            return -1
            
        return dist[n][C][D]
        
        
        
