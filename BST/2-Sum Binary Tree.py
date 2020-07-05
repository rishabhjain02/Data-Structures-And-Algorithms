"""

2-Sum Binary Tree
Problem Description

Given a binary search tree A, where each node contains a positive integer, and an integer B, you have to find whether or not there exist two different nodes X and Y such that X.value + Y.value = B.

Return 1 to denote that two such nodes exist. Return 0, otherwise.



Problem Constraints
1 <= size of tree <= 100000

1 <= B <= 10^9



Input Format
First argument is the head of the tree A.

Second argument is the integer B.



Output Format
Return 1 if such a pair can be found, 0 otherwise.



Example Input
Input 1:

         10
         / \
        9   20

B = 19
Input 2:

 
          10
         / \
        9   20

B = 40


Example Output
Output 1:

 1
Output 2:

 0


Example Explanation
Explanation 1:

 10 + 9 = 19. Hence 1 is returned.
Explanation 2:

 No such pair exists.

"""

# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

def preorder(root, values, B, ans):
    if root == None:
        return

    if B - root.val in values:
        ans[0] = 1
        return
    
    values.add(root.val)
    
    preorder(root.left, values, B, ans)
    preorder(root.right, values, B, ans)
    

class Solution:
	# @param A : root node of tree
	# @param B : integer
	# @return an integer
	def t2Sum(self, A, B):
	    ans = [0]
	    values = set()
	    preorder(A, values, B, ans)
	    return ans[0]

