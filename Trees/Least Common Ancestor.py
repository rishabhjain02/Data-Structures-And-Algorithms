"""

Least Common Ancestor
Problem Description

Find the lowest common ancestor in an unordered binary tree A given two values B and C in the tree.

Lowest common ancestor : the lowest common ancestor (LCA) of two nodes and w in a tree or directed acyclic graph (DAG) is the lowest (i.e. deepest) node that has both v and w as descendants.



Problem Constraints
1 <= size of tree <= 100000

1 <= B, C <= 10^9



Input Format
First argument is head of tree A.

Second argument is integer B.

Third argument is integer C.



Output Format
Return the LCA.



Example Input
Input 1:

 
      1
     /  \
    2    3
B = 2
C = 3
Input 2:

      1
     /  \
    2    3
   / \
  4   5
B = 4
C = 5


Example Output
Output 1:

 1
Output 2:

 2


Example Explanation
Explanation 1:

 LCA is 1.
Explanation 2:

 LCA is 2.

"""

# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

from collections import defaultdict


def find_path(root, path, num):
    if root == None:
        return False
        
    path.append(root.val)
    
    if root.val == num:
        return True
        
    if find_path(root.left, path, num) or find_path(root.right, path, num):
        return True
        
    path.pop()
    return False


def find_lca(root, num1, num2):
    path1 = []
    path2 = []
    
    val1 = find_path(root, path1, num1)
    val2 = find_path(root, path2, num2)
    
    if val1 == False or val2 == False:
        return -1
        
    i = 0
    while i < len(path1) and i < len(path2):
        if path1[i] != path2[i]:
            break
        i += 1
    return path1[i-1]


class Solution:
	# @param A : root node of tree
	# @param B : integer
	# @param C : integer
	# @return an integer
	def lca(self, A, B, C):
	    return find_lca(A, B, C)

	    
