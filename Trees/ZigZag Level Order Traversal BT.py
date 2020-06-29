"""

ZigZag Level Order Traversal BT
Problem Description

Given a binary tree, return the zigzag level order traversal of its nodes values. (ie, from left to right, then right to left for the next level and alternate between).



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
   [20, 9],
   [15, 7]
 ]
Output 2:

 [ 
   [1]
   [2, 6]
   [3]
 ]


Example Explanation
Explanation 1:

 Return the 2D array. Each row denotes the zigzag traversal of each level.

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
	def zigzagLevelOrder(self, root):
	    ans = []
	    
	    if root == None:
	        return
	    
	    queue = deque()
	    queue.append(root)
	    count = 1
	    flag = False
	    
	    while len(queue) > 0:
	        temp = deque()
	        
	        while count > 0:
	            cur_node = queue.popleft()
	            
	            if flag:
	                temp.appendleft(cur_node.val)
	            else:
	                temp.append(cur_node.val)
	            
	            if cur_node.left != None:
	                queue.append(cur_node.left)
	                
	            if cur_node.right != None:
	                queue.append(cur_node.right)
	            
	            count -= 1
	            
	        ans.append(temp)
	        count = len(queue)
	        flag = not flag
	        
	        
	    return ans
	    
