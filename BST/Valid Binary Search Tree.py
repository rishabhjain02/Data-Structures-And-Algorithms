"""

Valid Binary Search Tree
Problem Description

Given a binary tree represented by root A.

Assume a BST is defined as follows:

1) The left subtree of a node contains only nodes with keys less than the node's key.

2) The right subtree of a node contains only nodes with keys greater than the node's key.

3) Both the left and right subtrees must also be binary search trees.



Problem Constraints
1 <= Number of nodes in binary tree <= 100000

0 <= node values <= 10^9



Input Format
First and only argument is head of the binary tree A.



Output Format
Return 0 if false and 1 if true.



Example Input
Input 1:

 
   1
  /  \
 2    3
Input 2:

 
  2
 / \
1   3


Example Output
Output 1:

 0
Output 2:

 1


Example Explanation
Explanation 1:

 2 is not less than 1 but is in left subtree of 1.
Explanation 2:

Satisfies all conditions.

"""

# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

def checkValidBST(root, flag):
    if root == None:
        return float("-inf"), float("inf")
        
    left_max, left_min = checkValidBST(root.left, flag)
    right_max, right_min = checkValidBST(root.right, flag)
    
    if root.val <= left_max or root.val > right_min:
        flag[0] = 0
        
    return max(root.val, right_max), min(root.val, left_min)

class Solution:
	# @param A : root node of tree
	# @return an integer
	def isValidBST(self, A):
	    flag = [1]
	    checkValidBST(A, flag)
	    return flag[0]
	    
	    
