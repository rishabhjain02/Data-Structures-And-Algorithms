"""

Unique Binary Search Trees II
Problem Description

Given an integer A, how many structurally unique BST's (binary search trees) exist that can store values 1...A?



Problem Constraints
1 <= A <=18



Input Format
First and only argument is the integer A



Output Format
Return a single integer, the answer to the problem



Example Input
Input 1:

 1
Input 2:

 2


Example Output
Output 1:

 1
Output 2:

 2


Example Explanation
Explanation 1:

 Only single node tree is possible.
Explanation 2:

 2 trees are possible, one rooted at 1 and other rooted at 2.


"""


class Solution:
	# @param A : integer
	# @return an integer
	def numTrees(self, A):
	        
	    dp = [0]*(A+1)
	    dp[0] = 1
	        
	    for i in range(1, A+1):
	        for j in range(1, i+1):
	            dp[i] += dp[j-1] * dp[i-j]
	            
	    return dp[A]
