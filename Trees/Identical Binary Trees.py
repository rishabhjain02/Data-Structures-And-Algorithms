"""

Identical Binary Trees
Problem Description

Given two binary trees, check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.



Problem Constraints
1 <= number of nodes <= 10^5



Input Format
First argument is a root node of first tree, A.

Second argument is a root node of second tree, B.



Output Format
Return 0 / 1 ( 0 for false, 1 for true ) for this problem.



Example Input
Input 1:

   1       1
  / \     / \
 2   3   2   3
Input 2:

   1       1
  / \     / \
 2   3   3   3


Example Output
Output 1:

 1
Output 2:

 0


Example Explanation
Explanation 1:

 Both trees are structurally identical and the nodes have the same value.
Explanation 2:

 Value of left child of the tree is different.


"""

# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

def identical(root1, root2):
    
    if root1 == None and root2 == None:
        return 1
        
    if root1 == None or root2 == None:
        return 0
    
    if root1.val != root2.val:
        return 0
        
    return identical(root1.left, root2.left) and identical(root1.right, root2.right)

class Solution:
	# @param A : root node of tree
	# @param B : root node of tree
	# @return an integer
	def isSameTree(self, A, B):
	    return identical(A, B)
