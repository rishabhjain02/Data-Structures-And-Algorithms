"""

Level Order
Problem Description

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).



Problem Constraints
1 <= number of nodes <= 10^5



Input Format
First and only argument is root node of the binary tree, A.



Output Format
Return a 2D integer array denoting the zigzag level order traversal of the given binary tree.



Example Input
Input 1:

    3
   / \
  9  20
    /  \
   15   7
Input 2:

   1
  / \
 6   2
    /
   3


Example Output
Output 1:

 [
   [3],
   [9, 20],
   [15, 7]
 ]
Output 2:

 [ 
   [1]
   [6, 2]
   [3]
 ]


Example Explanation
Explanation 1:

 Return the 2D array. Each row denotes the traversal of each level.

"""

# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

from collections import deque

class Solution:
	# @param A : root node of tree
	# @return a list of list of integers
	def levelOrder(self, root):
	    ans = []
	    
	    if root == None:
	        return
	    
	    queue = deque()
	    queue.append(root)
	    
	    while len(queue) > 0:
	        temp = []
	        
	        for i in range(len(queue)):
	            cur_node = queue.popleft()
	            temp.append(cur_node.val)
	            
	            if cur_node.left != None:
	                queue.append(cur_node.left)
	                
	            if cur_node.right != None:
	                queue.append(cur_node.right)
	   
	        ans.append(temp)
	        
	        
	    return ans
	    
