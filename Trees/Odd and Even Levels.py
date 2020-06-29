"""

Odd and Even Levels
Problem Description

Given a binary tree of integers. Find the difference between the sum of nodes at odd level and sum of nodes at even level.

NOTE: Consider the level of root node as 1.



Problem Constraints
1 <= Number of nodes in binary tree <= 100000

0 <= node values <= 10^9



Input Format
First and only argument is a root node of the binary tree, A



Output Format
Return an integer denoting the difference between the sum of nodes at odd level and sum of nodes at even level.



Example Input
Input 1:

        1
      /   \
     2     3
    / \   / \
   4   5 6   7
  /
 8 
Input 2:

        1
       / \
      2   10
       \
        4


Example Output
Output 1:

 10
Output 2:

 -7


Example Explanation
Explanation 1:

 Sum of nodes at odd level = 23
 Sum of ndoes at even level = 13
Explanation 2:

 Sum of nodes at odd level = 5
 Sum of ndoes at even level = 12

"""

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

from collections import deque

class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, root):
        if root == None:
            return None
            
        sum = 0
        queue = deque()
        queue.append(root)
        size = 1
        flag = True
        
        while len(queue) > 0:
            for i in range(size):
                node = queue.popleft()
                
                if flag:
                    # For odd level
                    sum += node.val
                else:
                    # For even level
                    sum -= node.val
                    
                if node.left != None:
                    queue.append(node.left)
                    
                if node.right != None:
                    queue.append(node.right)
            
            size = len(queue)
            flag = not flag
        
        return sum
                
                
        
        
        
        
