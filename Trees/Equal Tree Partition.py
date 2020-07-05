"""

Equal Tree Partition
Problem Description

Given a binary tree A. Check whether it is possible to partition the tree to two trees which have equal sum of values after removing exactly one edge on the original tree.



Problem Constraints
1 <= size of tree <= 100000

-10^9 <= value of node <= 10^9



Input Format
First and only argument is head of tree A.



Output Format
Return 1 if the tree can be partitioned into two trees of equal sum else return 0.



Example Input
Input 1:

 
                5
               /  \
              3    7
             / \  / \
            4  6  5  6
Input 2:

 
                1
               / \
              2   10
                  / \
                 20  2


Example Output
Output 1:

 1
Output 2:

 0


Example Explanation
Explanation 1:

 Remove edge between 5(root node) and 7: 
        Tree 1 =                                               Tree 2 =
                        5                                                     7
                       /                                                     / \
                      3                                                     5   6    
                     / \
                    4   6
        Sum of Tree 1 = Sum of Tree 2 = 18
Explanation 2:

 The given Tree cannot be partitioned.

"""

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

def find_sum(root, nodeSum):
    if root == None:
        return 0
    
    left_sum = find_sum(root.left, nodeSum)
    
    right_sum = find_sum(root.right, nodeSum)
    
    nodeSum.append(left_sum + right_sum + root.val)
    
    return nodeSum[-1]
    

class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):
        nodeSum = []
        total_sum = find_sum(A, nodeSum)
        nodeSum.pop()
        
        if total_sum//2 in nodeSum:
            return 1
        return 0
