"""

TOP VIEW
Problem Description

Given a binary tree of integers denoted by root A. Return an array of integers representing the top view of the Binary tree.

Right view of a Binary Tree is a set of nodes visible when the tree is visited from top.

Return the nodes in any order.



Problem Constraints
1 <= Number of nodes in binary tree <= 100000

0 <= node values <= 10^9



Input Format
First and only argument is head of the binary tree A.



Output Format
Return an array, representing the top view of the binary tree.



Example Input
Input 1:

 
            1
          /   \
         2    3
        / \  / \
       4   5 6  7
      /
     8 
Input 2:

 
            1
           /  \
          2    3
           \
            4
             \
              5


Example Output
Output 1:

 [1, 2, 4, 8, 3, 7]
Output 2:

 [1, 2, 3]


Example Explanation
Explanation 1:

Top view is described.
Explanation 2:

Top view is described.

"""

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

from collections import defaultdict, deque

def vertical_order(root, hash_map):
    hd_map = defaultdict(int)
    queue = deque()
        
    hd_map[root] = 0
    hash_map[0] = root.val
    queue.append(root)
        
    while len(queue) > 0:
        node = queue.popleft()
        
        if node.left != None:
            left_child = node.left
            queue.append(left_child)
            hd_map[left_child] = hd_map[node] - 1
            hr_dist = hd_map[left_child]
            if hr_dist not in hash_map:
                hash_map[hr_dist] = left_child.val
                
        if node.right != None:
            right_child = node.right
            queue.append(right_child)
            hd_map[right_child] = hd_map[node] + 1
            hr_dist = hd_map[right_child]
            if hr_dist not in hash_map:
                hash_map[hr_dist] = right_child.val

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def solve(self, A):
        if A == None:
            return None
        
        hash_map = defaultdict(int)
        
        vertical_order(A, hash_map)
        
        return list(hash_map.values())
            
        
