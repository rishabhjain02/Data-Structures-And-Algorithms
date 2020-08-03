"""

Length of LIS
Problem Description

You are given an array A. You need to find the length of the Longest Increasing Subsequence in the array.

In other words, you need to find a subsequence of array A in which the elements are in sorted order, (strictly increasing) and as long as possible.



Problem Constraints
1 ≤ length(A), A[i] ≤ 10^5



Input Format
The first and only argument of the input is the array A.



Output Format
Output a single integer, the length of the longest increasing subsequence in array A.



Example Input
Input 1:

A: [2, 1, 4, 3]
Input 2:

A: [5, 6, 3, 7, 9]


Example Output
Output 1:

2
Output 2:

4


Example Explanation
Explanation 1:

 [2, 4] and [1, 3] are the longest increasing sequences of size 2. 
Explanation 2:

The longest increasing subsequence we can get is [5, 6, 7, 9] of size 4.


"""


# Finding the index of equal or next greater element than key using Binary Search.
def search(arr, low, high, key):
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] >= key:
            ans = mid
            high = mid - 1
            
        else:
            low = mid + 1
    
    return ans

class Solution:
    # @param A : list of integers
    # @return an integer
    def findLIS(self, A):
        n = len(A)
	    lis = [0]*n
	    
	    lis[0] = A[0]
	    last_idx = 0
	    
	    for i in range(1, n):
	        
	        if A[i] < lis[0]:
	            lis[0] = A[i]
	            
	        elif A[i] > lis[last_idx]:
	            last_idx += 1
	            lis[last_idx] = A[i]
	            
	        else:
	            index = search(lis, 0, last_idx, A[i])
	            lis[index] = A[i]
	            
	    return last_idx + 1
	            
