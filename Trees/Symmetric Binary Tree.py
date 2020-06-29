"""

Symmetric Binary Tree
Problem Description

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).



Problem Constraints
1 <= number of nodes <= 10^5



Input Format
First and only argument is the root node of the binary tree.



Output Format
Return 0 / 1 ( 0 for false, 1 for true ).



Example Input
Input 1:

    1
   / \
  2   2
 / \ / \
3  4 4  3
Input 2:

    1
   / \
  2   2
   \   \
   3    3


Example Output
Output 1:

 1
Output 2:

 0


Example Explanation
Explanation 1:

 The above binary tree is symmetric. 
Explanation 2:

The above binary tree is not symmetric.

"""

# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

def symmetric(root1, root2):
    
    if root1 == None and root2 == None:
        return 1
        
    if root1 == None or root2 == None:
        return 0
    
    if root1.val != root2.val:
        return 0
        
    return symmetric(root1.left, root2.right) and symmetric(root1.right, root2.left)


class Solution:
	# @param A : root node of tree
	# @return an integer
	def isSymmetric(self, A):
	    
	    return symmetric(A.left, A.right)
	    
