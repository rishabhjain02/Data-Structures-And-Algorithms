"""

Next Pointer Binary Tree
Problem Description

Given a binary tree,

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Assume perfect binary tree and try to solve this in constant extra space.



Problem Constraints
1 <= Number of nodes in binary tree <= 100000

0 <= node values <= 10^9



Input Format
First and only argument is head of the binary tree A.



Output Format
Return the head of the binary tree after the changes are made.



Example Input
Input 1:

 
     1
    /  \
   2    3
Input 2:

 
        1
       /  \
      2    5
     / \  / \
    3  4  6  7


Example Output
Output 1:

 
        1 -> NULL
       /  \
      2 -> 3 -> NULL
Output 2:

 
         1 -> NULL
       /  \
      2 -> 5 -> NULL
     / \  / \
    3->4->6->7 -> NULL


Example Explanation
Explanation 1:

Next pointers are set as given in the output.
Explanation 2:

Next pointers are set as given in the output.

"""

# Definition for a  binary tree node
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

def findNextRightNode(pointer):
    
    while pointer.next != None:
        pointer = pointer.next
        
        if pointer.left != None:
            return pointer.left
        
        if pointer.right != None:
            return pointer.right
    
    return None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root == None:
            return root
        
        vertical_pointer = root
        
        while vertical_pointer != None:
            horizontal_pointer = vertical_pointer
            
            while horizontal_pointer != None:
                
                if horizontal_pointer.left != None:
                    if horizontal_pointer.right != None:
                        horizontal_pointer.left.next = horizontal_pointer.right
                    else:
                        horizontal_pointer.left.next = findNextRightNode(horizontal_pointer)
                
                if horizontal_pointer.right != None:
                    horizontal_pointer.right.next = findNextRightNode(horizontal_pointer)
                
                horizontal_pointer = horizontal_pointer.next
                
            if vertical_pointer.left != None:
                vertical_pointer = vertical_pointer.left
            
            elif vertical_pointer.right != None:
                vertical_pointer = vertical_pointer.right
        
            else:
                vertical_pointer = findNextRightNode(vertical_pointer)
                
        return root
        
        