"""

Binary Tree From Inorder And Postorder
Problem Description

Given inorder and postorder traversal of a tree, construct the binary tree.

NOTE: You may assume that duplicates do not exist in the tree.



Problem Constraints
1 <= number of nodes <= 10^5



Input Format
First argument is an integer array A denoting the inorder traversal of the tree.

Second argument is an integer array B denoting the postorder traversal of the tree.



Output Format
Return the root node of the binary tree.



Example Input
Input 1:

 A = [2, 1, 3]
 B = [2, 3, 1]
Input 2:

 A = [6, 1, 3, 2]
 B = [6, 3, 2, 1]


Example Output
Output 1:

   1
  / \
 2   3
Output 2:

   1  
  / \
 6   2
    /
   3


Example Explanation
Explanation 1:

 Create the binary tree and return the root node of the tree.

"""

# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

def helper(inorder, postorder):
    if not inorder:
        return None
	
	root_val = postorder[-1]
	root_idx = inorder.index(root_val)
	    
	left_nodes = inorder[:root_idx]
	right_nodes = inorder[root_idx+1:]

    m = len(left_nodes)
    n = len(right_nodes)
        
    root = TreeNode(root_val)
    root.left = helper(left_nodes, postorder[:m])
	root.right = helper(right_nodes, postorder[m:-1])
	    
    return root

class Solution:
	# @param A : list of integers
	# @param B : list of integers
	# @return the root node in the tree
	def buildTree(self, inorder, postorder):
	    
	    return helper(inorder, postorder)
	    
	    
        