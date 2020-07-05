"""

Recover Binary Search Tree
Problem Description

Two elements of a binary search tree (BST),represented by root A are swapped by mistake. Tell us the 2 values swapping which the tree will be restored.

A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?



Problem Constraints
1 <= size of tree <= 100000



Input Format
First and only argument is the head of the tree,A



Output Format
Return the 2 elements which need to be swapped.



Example Input
Input 1:

 
         1
        / \
       2   3
Input 2:

 
         2
        / \
       3   1



Example Output
Output 1:

 [2, 1]
Output 2:

 [3, 1]


Example Explanation
Explanation 1:

Swapping 1 and 2 will change the BST to be 
         2
        / \
       1   3
which is a valid BST 
Explanation 2:

Swapping 1 and 3 will change the BST to be 
         2
        / \
       1   3
which is a valid BST 

"""

# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

def inorder(root, arr):
    if root == None:
        return
    
    inorder(root.left, arr)
    
    arr.append(root.val)
    
    inorder(root.right, arr)
        

class Solution:
	# @param A : root node of tree
	# @return a list of integers
	def recoverTree(self, A):
	    ans = [0,0]
	    arr = []
	    flag = False
	    inorder(A, arr)
	    
	    for i in range(1, len(arr)):
	        if arr[i] < arr[i-1] and flag == False:
	            ans[1] = arr[i-1]
	            flag = True
	        
	        if arr[i] > ans[1] and flag == True:
	            ans[0] = arr[i-1]
	            flag = False
	    
	    if ans[0] == 0:
	        ans[0] = arr[-1]
	    
	    return ans
	        
