"""

Max Product Subarray
Problem Description

Given an integer array A of size N. Find the contiguous subarray within the given array (containing at least one number) which has the largest product.

Return an integer corresponding to the maximum product possible.

NOTE: Answer will fit in 32-bit integer value.



Problem Constraints
1 <= N <= 5 * 10^5

-100 <= A[i] <= 100



Input Format
First and only argument is an integer array A.



Output Format
Return an integer corresponding to the maximum product possible.



Example Input
Input 1:

 A = [4, 2, -5, 1]
Input 2:

 A = [-3, 0, -5, 0]


Example Output
Output 1:

 8
Output 2:

 0


Example Explanation
Explanation 1:

 We can choose the subarray [4, 2] such that the maximum product is 8.
Explanation 2:

 0 will be the maximum product possible.


"""


class Solution:
	# @param A : tuple of integers
	# @return an integer
	def maxProduct(self, A):
	    n = len(A)
	        
	    local_min = A[0]
	    local_max = A[0]
	    global_max = A[0]
	    
	    for i in range(1, n):
	        if A[i] < 0:
	            local_max, local_min = local_min, local_max
	            
	        local_max = max(A[i], A[i]*local_max)
	        local_min = min(A[i], A[i]*local_min)
	        
	        global_max = max(global_max, local_max)
	    
	    return global_max