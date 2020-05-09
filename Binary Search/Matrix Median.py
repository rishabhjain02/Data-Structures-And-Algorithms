"""

Matrix Median
Problem Description
Given a matrix of integers A of size N x M in which each row is sorted. Find and return the overall median of the matrix A. NOTE: No extra memory is allowed. NOTE: Rows are numbered from top to bottom and columns are numbered from left to right. 


Problem Constraints
1 <= N, M <= 10^5 1 <= N*M <= 10^6 1 <= A[i] <= 10^9 N*M is odd 


Input Format
The first and only argument given is the integer matrix A.


Output Format
Return the overall median of the matrix A.


Example Input
Input 1:
A = [   [1, 3, 5],
        [2, 6, 9],
        [3, 6, 9]   ]
  Input 2:      
A = [   [5, 17, 100]    ]
    


Example Output
Output 1:
 5
  Output 2:      
 17
    


Example Explanation
Explanation 1:
 
A = [1, 2, 3, 3, 5, 6, 6, 9, 9]
Median is 5. So, we return 5.
  Explanation 2:      
 
Median is 17.

"""

import bisect
class Solution:
	# @param A : list of list of integers
	# @return an integer
	def findMedian(self, A):
	    n = len(A)
        m = len(A[0])
        min_no = A[0][0]
        max_no = A[0][0]
        for i in range(n):
            min_no = min(min_no,A[i][0])
            max_no = max(max_no,A[i][m-1])
            
        required_ans = (n*m)//2
        
        low = min_no
        high = max_no
        ans = 0
        while(low <= high):
            mid = low + (high-low)//2
            small_count = 0
            large_count = 0
            for i in range(n):
                small_count += bisect.bisect_right(A[i], mid, 0, m)
            for i in range(n):
                large_count += bisect.bisect_left(A[i], mid, 0, m)
            if small_count == n*m-large_count:
                return mid
            elif small_count > required_ans:
                high = mid-1
            elif small_count <= required_ans:
                low = mid+1
                
        return low
