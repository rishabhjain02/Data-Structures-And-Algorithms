"""

Longest Increasing Subsequence
Problem Description

Find the longest increasing subsequence of a given array of integers, A.

In other words, find a subsequence of array in which the subsequence's elements are in strictly increasing order, and in which the subsequence is as long as possible.

In this case, return the length of the longest increasing subsequence.



Problem Constraints
0 <= length(A) <= 2500
1 <= A[i] <= 2500



Input Format
The first and the only argument is an integer array A.



Output Format
Return an integer representing the length of the longest increasing subsequence.



Example Input
Input 1:

 A = [1, 2, 1, 5]
Input 2:

 A = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]


Example Output
Output 1:

 3
Output 2:

 6


Example Explanation
Explanation 1:

 The longest increasing subsequence: [1, 2, 5]
Explanation 2:

 The possible longest increasing subsequences: [0, 2, 6, 9, 13, 15] or [0, 4, 6, 9, 11, 15] or [0, 4, 6, 9, 13, 15]


"""


class Solution:
	# @param A : tuple of integers
	# @return an integer
	def lis(self, A):
	    n = len(A)
	    lis = [1]*n
	    
	    for i in range(1, n):
	        
	        max_val = 0
	        for j in range(i):
	            
	            if A[j] < A[i]:
	                max_val = max(max_val, lis[j])
	        
	        if max_val != 0:        
	            lis[i] = max_val + 1
	        
	    return max(lis)
