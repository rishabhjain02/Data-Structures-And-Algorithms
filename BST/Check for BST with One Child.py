"""

Check for BST with One Child
Problem Description

Given preorder traversal of a binary tree, check if it is possible that it is also a preorder traversal of a Binary Search Tree (BST), where each internal node (non-leaf nodes) have exactly one child.



Problem Constraints
1 <= number of nodes <= 100000



Input Format
First and only argument is an integer array denoting the preorder traversal of binary tree.



Output Format
Return a string "YES" if true else "NO".



Example Input
Input 1:

 A : [4, 10, 5, 8]
Input 2:

 A : [1, 5, 6, 4]


Example Output
Output 1:

 "YES"
Output 2:

 "NO"


Example Explanation
Explanation 1:

 The possible BST is:
            4
             \
             10
             /
             5
              \
              8
Explanation 2:

 There is no possible BST which have the above preorder traversal.

"""

class Solution:
    # @param A : list of integers
    # @return a strings
    def solve(self, A):
        n = len(A)
        if n <= 2:
            return "YES"
            
        min_val = min(A[n-1], A[n-2])
        max_val = max(A[n-1], A[n-2])
        
        for i in range(n-3, -1, -1):
            if A[i] < max_val and A[i] > min_val:
                return "NO"
            min_val = min(min_val, A[i])
            max_val = max(max_val, A[i])
            
        return "YES"
        
