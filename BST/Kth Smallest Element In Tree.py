"""

Kth Smallest Element In Tree
Problem Description

Given a binary search tree represented by root A, write a function to find the Bth smallest element in the tree.



Problem Constraints
1 <= Number of nodes in binary tree <= 100000

0 <= node values <= 10^9



Input Format
First and only argument is head of the binary tree A.



Output Format
Return an integer, representing the Bth element.



Example Input
Input 1:

 
            2
          /   \
         1    3
B = 2
Input 2:

 
            3
             \
              2
               \
                1
B = 1



Example Output
Output 1:

 2
Output 2:

 1


Example Explanation
Explanation 1:

2nd element is 2.
Explanation 2:

1st element is 1.

"""

# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

def inorder(root, k, count, ans):
    if root == None:
        return
    
    inorder(root.left, k, count, ans)
    
    count[0] += 1
    if count[0] == k:
        ans[0] = root.val
        return
    
    inorder(root.right, k, count, ans)
    

class Solution:
	# @param A : root node of tree
	# @param B : integer
	# @return an integer
	def kthsmallest(self, A, B):
	    count = [0]
	    ans = [0]
	    inorder(A, B, count, ans)
	    return ans[0]
        
        
        