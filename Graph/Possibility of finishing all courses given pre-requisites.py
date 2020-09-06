"""

Possibility of finishing all courses given pre-requisites
Problem Description

There are a total of A courses you have to take, labeled from 1 to A.

Some courses may have prerequisites, for example to take course 2 you have to first take course 1, which is expressed as a pair: [1,2].

So you are given two integer array B and C of same size where for each i (B[i], C[i]) denotes a pair.

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Return 1 if it is possible to finish all the courses, or 0 if it is not possible to finish all the courses.



Problem Constraints
1 <= A <= 6*10^4

1 <= length(B) = length(C) <= 10^5

1 <= B[i], C[i] <= A



Input Format
The first argument of input contains an integer A, representing the number of courses.

The second argument of input contains an integer array, B.

The third argument of input contains an integer array, C.



Output Format
Return 1 if it is possible to finish all the courses, or 0 if it is not possible to finish all the courses.



Example Input
Input 1:

 A = 3
 B = [1, 2]
 C = [2, 3]
Input 2:

 A = 2
 B = [1, 2]
 C = [2, 1]


Example Output
Output 1:

 1
Output 2:

 0


Example Explanation
Explanation 1:

 It is possible to complete the courses in the following order:
    1 -> 2 -> 3
Explanation 2:

 It is not possible to complete all the courses.


"""


# Do Topological Sort, if all elements are covered in sort then ans is 1 else 0

from collections import defaultdict, deque


def make_adjacency_list(graph, B, C):
    n = len(B)
    
    for i in range(n):
        graph[B[i]].append(C[i])


def isPossible(A, graph, indegree, count):
    for u in graph:
        for v in graph[u]:
            indegree[v] += 1
            
    queue = deque()
    
    for i in range(1, A+1):
        if indegree[i] == 0:
            queue.append(i)
            
    while queue:
        node = queue.popleft()
        count += 1
        
        for neighbour in graph[node]:
            indegree[neighbour] -= 1
            if indegree[neighbour] == 0:
                queue.append(neighbour)
                
    if count == A:
        return 1
    
    return 0
    

class Solution:
	# @param A : integer
	# @param B : list of integers
	# @param C : list of integers
	# @return an integer
	def solve(self, A, B, C):
	    graph = defaultdict(list)
	    indegree = [0]*(A+1)
	    count = 0
	    
	    make_adjacency_list(graph, B, C)
	    
	    return isPossible(A, graph, indegree, count)
	    
	    
