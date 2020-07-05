"""

Largest BST Subtree
Problem Description

Given a Binary Tree A with N nodes.

Write a function that returns the size of the largest subtree which is also a Binary Search Tree (BST).

If the complete Binary Tree is BST, then return the size of whole tree.

NOTE:

Largest subtree means subtree with most number of nodes.


Problem Constraints
1 <= N <= 10^5



Input Format
First and only argument is an pointer to root of the binary tree A.



Output Format
Return an single integer denoting the size of the largest subtree which is also a BST.



Example Input
Input 1:

     10
    / \
   5  15
  / \   \ 
 1   8   7
Input 2:

     5
    / \
   3   8
  / \ / \
 1  4 7  9


Example Output
Output 1:

 3
Output 2:

 7


Example Explanation
Explanation 1:

 Largest BST subtree is
                            5
                           / \
                          1   8
Explanation 2:

 Given binary tree itself is BST.

"""

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

def largestBSTSubtree(root, ans, flag):
    if root == None:
        # Third value in return is for size of the BST
        return float("-inf"), float("inf"), 0
        
    left_max, left_min, left_size = largestBSTSubtree(root.left, ans, flag)
    right_max, right_min, right_size = largestBSTSubtree(root.right, ans, flag)
    
    # Checking valid BST
    if root.val > left_max and root.val <= right_min and flag[0] == 1:
        ans[0] = max(ans[0], left_size+right_size+1)
    else:
        flag[0] = 0
        
    return max(root.val, right_max), min(root.val, left_min), left_size+right_size+1

class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):
        ans = [0]
        flag = [1]
        largestBSTSubtree(A, ans, flag)
        return ans[0]
        
