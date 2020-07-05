"""

Flatten Binary Tree to Linked List
Problem Description

Given a binary tree A, flatten it to a linked list in-place.

The left child of all nodes should be NULL.



Problem Constraints
1 <= size of tree <= 100000



Input Format
First and only argument is the head of tree A.



Output Format
Return the linked-list after flattening.



Example Input
Input 1:

     1
    / \
   2   3
Input 2:

         1
        / \
       2   5
      / \   \
     3   4   6


Example Output
Output 1:

1
 \
  2
   \
    3
Output 2:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6


Example Explanation
Explanation 1:

 Tree flattening looks like this.
Explanation 2:

 Tree flattening looks like this.

"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def flattenTree(root):
    if root == None:
        return
    
    left_node = flattenTree(root.left)
    right_node = flattenTree(root.right)
    
    root.left = None
    
    if left_node != None:
        root.right = left_node
        
        while left_node.right != None:
            left_node = left_node.right
        
        left_node.right = right_node
    
    else:
        root.right = right_node
    
    return root
        

class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def flatten(self, A):
        return flattenTree(A)
        
        
