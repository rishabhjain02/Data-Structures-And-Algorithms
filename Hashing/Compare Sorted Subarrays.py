"""

Compare Sorted Subarrays
Problem Description

Given an array A of length N. You have to answer Q queires.

Each query will contain 4 integers l1, r1, l2 and r2. If sorted segment from [l1, r1] is same as sorted segment from [l2 r2] then answer is 1 else 0.

NOTE The queries are 0-indexed.



Problem Constraints
0 <= A[i] <= 100000
1 <= N <= 100000
1 <= Q <= 100000



Input Format
First argument is an array A.
Second will be 2-D array B denoting queries with dimension Q * 4.
Consider ith query as l1 = B[i][0], r1 = B[i][1], l2 = A[i][2], r2 = B[i][3].



Output Format
Return an array of length Q with answer of the queries in the same order in input.



Example Input
Input 1:

 A = [1, 7, 11, 8, 11, 7, 1]
 B = [ 
       [0, 2, 4, 6]
     ]
Input 2:

 A = [1, 3, 2]
 B = [
       [0, 1, 1, 2]
     ] 


Example Output
Output 1:

 [1]
Output 2:

 [0]


Example Explanation
Explanation 1:

 (0, 2) -> [1, 7, 11]
 (4, 6) -> [11, 7, 1]
 Both are same when sorted hence 1.
Explanation 2:

 (0, 1) -> [1, 3]
 (1, 2) -> [3, 2] 
 Both are different when sorted hence -1.

"""

import random
from collections import defaultdict
class Solution:
	# @param A : list of integers
	# @param B : list of list of integers
	# @return a list of integers
	def solve(self, A, B):
	    n = len(A)
	    m = len(B)
	    hash = defaultdict(int)
	    prefix_sum = [0]*(n+1)
	    ans = []
	    
	    # Mapping each number to some random number in the range(1, 10^10)
	    # So, that probability of collison of sum become very very less
	    for num in A:
	        hash[num] = random.randint(1, 10**10)
	    
	    # Computing prefix sum, By this we can solve each query in O(1)    
	    prefix_sum[0] = 0 
	    for i in range(1, n+1):
	        prefix_sum[i] = prefix_sum[i-1] + hash[A[i-1]]
	        
	    for i in range(m):
	        l1, r1, l2, r2 = B[i][0], B[i][1], B[i][2], B[i][3]
	        
	        # Taking the sum of numbers A[l1:r1] i.e. from l1 to r1 index and store in sum1
	        # Taking the sum of numbers A[l2:r2] i.e. from l2 to r2 index and store in sum2
	        sum1 = prefix_sum[r1+1] - prefix_sum[l1]
	        sum2 = prefix_sum[r2+1] - prefix_sum[l2]
	        
	        # Checking if sum1 and sum2 are equal then both are same segment, if we sort them, so--> 1
	        if sum1 == sum2:
	            ans.append(1)
	            
	        # if sum1 and sum2 are not equal, so--> 0
	        else:
	            ans.append(0)
	    
	    return ans
        
	    
	    
