"""

Make Circle
Problem Description

Given an array of strings A of size N, find if the given strings can be chained to form a circle.

A string X can be put before another string Y in circle if the last character of X is same as first character of Y.

NOTE: All strings consist of lower case characters.



Problem Constraints
1 <= N <= 10^5

Sum of length of all strings <= 10^6



Input Format
First and only argument is a string array A of size N.



Output Format
Return an integer 1 if it is possible to chain the strings to form a circle else return 0.



Example Input
Input 1:

 A = ["aab", "bac", "aaa", "cda"]
Input 2:

 A = ["abc", "cbc"]


Example Output
Output 1:

 1
Output 2:

 0


Example Explanation
Explanation 1:

 We can chain the strings aab -> bac -> cda -> aaa -> aab. So this forms a circle. So, output will be 1. 
Explanation 2:

 There is no way to chain the given strings such that they forms a circle.

"""


from collections import defaultdict


def can_be_chained(A):
    graph = defaultdict(list)
    present = [False]*26
    indegree = [0]*26
    outdegree = [0]*26
    
    for s in A:
        u = ord(s[0]) - 97
        v = ord(s[-1]) - 97
        
        present[u] = True
        present[v] = True
        
        indegree[v] += 1
        outdegree[u] += 1
        
        graph[u].append(v)
        
    for i in range(26):
        if indegree[i] != outdegree[i]:
            return 0
            
    return fully_connected(graph, present, ord(A[0][0]) - 97)
    
    
def fully_connected(graph, present, s):
    visited = [False]*26
    
    dfs(graph, visited, s)
    
    for i in range(26):
        if present[i] == True and visited[i] == False:
            return 0
            
    return 1
    
    
def dfs(graph, visited, s):
    visited[s] = True
    
    for i in graph[s]:
        if visited[i] == False:
            dfs(graph, visited, i)

    

class Solution:
    # @param A : list of strings
    # @return an integer
    def solve(self, A):
        
        return can_be_chained(A)
        

