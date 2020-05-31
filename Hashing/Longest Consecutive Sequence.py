"""

Longest Consecutive Sequence
Problem Description

Given an unsorted integer array A of size N.

Find the length of the longest set of consecutive elements from the array A.



Problem Constraints
1 <= N <= 10^6

-10^6 <= A[i] <= 10^6



Input Format
First argument is an integer array A of size N.



Output Format
Return an integer denoting the length of the longest set of consecutive elements from the array A.



Example Input
Input 1:

A = [100, 4, 200, 1, 3, 2]
Input 2:

A = [2, 1]


Example Output
Output 1:

 4
Output 2:

 2


Example Explanation
Explanation 1:

 The set of consecutive elements will be [1, 2, 3, 4].
Explanation 2:

 The set of consecutive elements will be [1, 2].

"""

class Solution:
	# @param A : tuple of integers
	# @return an integer
	def longestConsecutive(self, A):
	    n = len(A)
	    s = set()
	    ans = 0
	    
	    for num in A:
	        s.add(num)
	        
	    for i in range(n):
	        if A[i]-1 not in s:
	            num = A[i]
	            while(num in s):
	                num += 1
	            ans = max(ans, num-A[i])
	    return ans
	    
