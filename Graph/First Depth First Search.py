"""

First Depth First Search
Problem Description

You are given n towns (1 to n). All towns are connected via unique directed path as mentioned in the input.

Given 2 towns find whether you can reach the first town from the second without repeating any edge.

x y : query to find whether x is reachable from y.

Input contains an integer array A of size n and 2 integers x and y ( 1 <= x, y <= n ).

There exist a directed edge from A[i] to i+1 for every 1 <= i < n. Also, it's guaranteed that A[i] <= i.

NOTE: Array A is 0-indexed.



Problem Constraints
1 <= n <= 100000



Input Format
First argument is vector A

Second argument is integer B

Third argument is integer C



Output Format
Return 1 if reachable, 0 otherwise.



Example Input
Input 1:

 A = [1, 1, 2]
 B = 1
 C = 2
Input 2:

 A = [1, 1, 2]
 B = 2
 C = 1


Example Output
Output 1:

 0
Output 2:

 1


Example Explanation
Explanation 1:

 Tree is 1--> 2--> 3 and hence 1 is not reachable from 2.
Explanation 2:

 Tree is 1--> 2--> 3 and hence 2 is reachable from 1.


"""


from collections import defaultdict, deque


def make_adjacency_list(graph, A):
    for i in range(1, len(A)):
        graph[A[i]].append(i+1)


def path_exists(graph, visited, s, d):
    if s == d:
        return 1
        
    visited[s] = True
    
    for i in graph[s]:
        if visited[i] == False:
            if path_exists(graph, visited, i, d):
                return 1
                
    return 0


class Solution:
	# @param A : list of integers
	# @param B : integer
	# @param C : integer
	# @return an integer
	def solve(self, A, B, C):
	    n = len(A)
	    graph = defaultdict(list)
	    visited = [False]*(n+1)
	    
	    make_adjacency_list(graph, A)
	    
	    return path_exists(graph, visited, C, B)
	    
