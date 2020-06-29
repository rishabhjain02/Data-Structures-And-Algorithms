"""

Balanced Binary Tree
Problem Description

Given a root of binary tree A, determine if it is height-balanced.

A height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.



Problem Constraints
1 <= size of tree <= 100000



Input Format
First and only argument is the root of the tree A.



Output Format
Return 0 / 1 ( 0 for false, 1 for true ) for this problem.



Example Input
Input 1:

    1
   / \
  2   3
Input 2:

 
       1
      /
     2
    /
   3


Example Output
Output 1:

1
Output 2:

0


Example Explanation
Explanation 1:

It is a complete binary tree.
Explanation 2:

Because for the root node, left subtree has depth 2 and right subtree has depth 0. 
Difference = 2 > 1. 

"""


# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

def balance(root):
    if root == None:
        return -1, True
        
    height_left, left_balanced = balance(root.left)
    
    if left_balanced:
        height_right, right_balanced = balance(root.right)
        
        if right_balanced and abs(height_right - height_left) <= 1:
            return (max(height_left, height_right) + 1), True
            
        else:
            return height_left, False
    
    else:
        return height_left, False

class Solution:
	# @param A : root node of tree
	# @return an integer
	def isBalanced(self, A):
	    height, ans = balance(A)
	    if ans:
	        return 1
	    return 0
