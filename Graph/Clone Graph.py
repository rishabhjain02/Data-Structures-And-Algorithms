"""

Clone Graph
Problem Description

Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.



Problem Constraints
1 <= Number of nodes <= 10^5



Input Format
First and only argument is a node A denoting the root of the undirected graph.



Output Format
Return the node denoting the root of the new clone graph.



Example Input
Input 1:

      1
    / | \
   3  2  4
        / \
       5   6
Input 2:

      1
     / \
    3   4
   /   /|\
  2   5 7 6


Example Output
Output 1:

 Output will the same graph but with new pointers:
      1
    / | \
   3  2  4
        / \
       5   6
Output 2:

      1
     / \
    3   4
   /   /|\
  2   5 7 6


Example Explanation
Explanation 1:

 We need to return the same graph, but the pointers to the node should be different.


"""


# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

from collections import deque, defaultdict

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, root):
        
        queue = deque()
        queue.append(root)
        
        hashmap = defaultdict(int)
        hashmap[root] = UndirectedGraphNode(root.label)
    
        while queue:
            node = queue.popleft()
            
            for child in node.neighbors:
                if child not in hashmap:
                    hashmap[child] = UndirectedGraphNode(child.label)
                    queue.append(child)
                    
                hashmap[node].neighbors.append(hashmap[child])
                
        return hashmap[root]
            
        
        
