"""

Gym Trainer
Problem Description

You are the trainer of a gym and there are A people who come to your gym.

Some of them are friends because they walk together, and some of them are friends because they talk together.
But people become possessive about each other, so a person cannot walk with one friend and talk with another. Although he can walk with two or more people or talk with two or more people.

You being the trainer, decided to suggest each one of the 2 possible diets. But friends, being friends will always have the same diet as all the other friends are having.

Find and return the number of ways you can suggest each of them a diet.

As the number of ways can be huge, return the answer modulo 109+7.

NOTE: If there is any person who walks with one person and talks with the another person, then you may return 0.



Problem Constraints
1 <= A, N, M <= 10^5

1 <= B[i][0], B[i][1], C[i][0], C[i][1] <= A



Input Format
The first argument contains an integer A, representing the number of people.
The second argument contains a 2-D integer array B of size N x 2, where B[i][0] and B[i][1] are friends because they walk together.
The third argument contains a 2-D integer array C of size M x 2, where C[i][0] and C[i][1] are friends because they talk together.



Output Format
Return an integer representing the number of ways to suggest one of the two diets to the people.



Example Input
Input 1:

 A = 4
 B = [
       [1, 2]
     ]
 C = [
       [3, 4]
     ]
Input 2:

 A = 3
 B = [
       [1, 2]
     ]
 C = [
       [1, 3] 
     ]


Example Output
Output 1:

 4
Output 2:

 0


Example Explanation
Explanation 1:

 There are four ways to suggest the diet:
 Diet-1 to (1, 2) and Diet-2 to (3, 4).
 Diet-1 to (1, 2) and Diet-1 to (3, 4).
 Diet-2 to (1, 2) and Diet-1 to (3, 4).
 Diet-2 to (1, 2) and Diet-2 to (3, 4).
 
Explanation 2:

 Person 1 walks with person 2 and talks with person 3. So, we will return 0.

"""


# Count number of groups formed in list A as well as in list B
# If some person is present in both the lists, return 0
# Ans = 2 ^ (count of groups + count of persons having no friend)

import sys
sys.setrecursionlimit(10**6)

from collections import defaultdict

def make_adjacency_list(graph, arr):
    for u, v in arr:
        graph[u].append(v)
        graph[v].append(u)
        

def dfs(graph, source, visited):
    visited[source] = 1
    
    for i in graph[source]:
        if i not in visited:
            dfs(graph, i, visited)


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @param C : list of list of integers
    # @return an integer
    def solve(self, A, B, C):
        graph = defaultdict(list)
        visited1 = defaultdict(int)
        count = 0
        
        make_adjacency_list(graph, B)
        
        # Appying DFS on First list B
        for i in graph:
            if i not in visited1:
                dfs(graph, i, visited1)
                count += 1
                
        # Checking for common person in both the lists        
        for u, v in C:
            if u in visited1 or v in visited1:
                return 0
                
        graph = defaultdict(list)        
        visited2 = defaultdict(int)
        
        make_adjacency_list(graph, C)
        
        # Applying DFS on Second list C
        for i in graph:
            if i not in visited2:
                dfs(graph, i, visited2)
                count += 1
                
        # Checking for person having no friend        
        for i in range(1, A+1):
            if i not in visited1 and i not in visited2:
                count += 1
                
        # Calculating ans        
        return pow(2, count, 10**9+7)
            
        
        
