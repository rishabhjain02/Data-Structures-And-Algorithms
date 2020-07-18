"""

Minimum largest element
Problem Description

Given an array A of N numbers, you have to perform B operations. In each operation, you have to pick any one of the N elements and add original value(value stored at index before we did any operations) to it's current value. You can choose any of the N elements in each operation.

Perform B operations in such a way that the largest element of the modified array(after B operations) is minimised. Find the minimum possible largest element after B operations.



Problem Constraints
1 <= N <= 10^6
0 <= B <= 10^5
-10^5 <= A[i] <= 10^5



Input Format
First argument is an integer array A.
Second argument is an integer B.



Output Format
Return an integer denoting the minimum possible largest element after B operations.



Example Input
Input 1:

 A = [1, 2, 3, 4] 
 B = 3
Input 2:

 A = [5, 1, 4, 2] 
 B = 5


Example Output
Output 1:

 4
Output 2:

 5


Example Explanation
Explanation 1:

 Apply operation on element at index 0, the array would change to [2, 2, 3, 4]
 Apply operation on element at index 0, the array would change to [3, 2, 3, 4]
 Apply operation on element at index 0, the array would change to [4, 2, 3, 4]
 Minimum possible largest element after 3 operations is 4.
Explanation 2:

 Apply operation on element at index 1, the array would change to [5, 2, 4, 2]
 Apply operation on element at index 1, the array would change to [5, 3, 4, 2]
 Apply operation on element at index 1, the array would change to [5, 4, 4, 2]
 Apply operation on element at index 1, the array would change to [5, 5, 4, 2]
 Apply operation on element at index 3, the array would change to [5, 5, 4, 4]
 Minimum possible largest element after 5 operations is 5.

"""


import heapq

class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer
	def solve(self, A, B):
	    new = A[:]
	    n = len(A)
	    
	    min_heap = []
	    
	    for i in range(n):
	        heapq.heappush(min_heap, (A[i] + A[i], i))
	        
	    for _ in range(B):
	        val, index = heapq.heappop(min_heap)
	        new[index] = val
	        heapq.heappush(min_heap, (new[index] + A[index], index))
	        
	    return max(new)
	    
