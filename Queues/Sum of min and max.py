"""

Sum of min and max
Problem Description

Given an array A of both positive and negative integers.

Your task is to compute sum of minimum and maximum elements of all sub-array of size B.

NOTE: Since the answer can be very large, you are required to return the sum modulo 10^9 + 7.



Problem Constraints
1 <= size of array A <= 10^5

-10^9 <= A[i] <= 10^9

1 <= B <= size of array



Input Format
The first argument denotes the integer array A.
The second argument denotes the value B



Output Format
Return an integer that denotes the required value.



Example Input
Input 1:

 A = [2, 5, -1, 7, -3, -1, -2]
 B = 4
Input 2:

 A = [2, -1, 3]
 B = 2


Example Output
Output 1:

 18
Output 2:

 3


Example Explanation
Explanation 1:

 Subarrays of size 4 are : 
    [2, 5, -1, 7],   min + max = -1 + 7 = 6
    [5, -1, 7, -3],  min + max = -3 + 7 = 4      
    [-1, 7, -3, -1], min + max = -3 + 7 = 4
    [7, -3, -1, -2], min + max = -3 + 7 = 4   
    Sum of all min & max = 6 + 4 + 4 + 4 = 18 
Explanation 2:

 Subarrays of size 2 are : 
    [2, -1],   min + max = -1 + 2 = 1
    [-1, 3],   min + max = -1 + 3 = 2
    Sum of all min & max = 1 + 2 = 3 

"""

from collections import deque

def find_max(A, B):
    n = len(A)
	queue = deque()
	window_start = 0
	max_sum = 0
	    
	queue.append(0)
	for i in range(1, B):
	    while len(queue) != 0 and A[i] >= A[queue[len(queue)-1]]:
	        queue.pop()
	    queue.append(i)
	max_sum = (max_sum + A[queue[0]])%(10**9+7)
	    
	for i in range(B, n):
	    window_start += 1
	    while len(queue) != 0 and A[i] >= A[queue[len(queue)-1]]:
	        queue.pop()
	    queue.append(i)
	    if queue[0] < window_start:
	        queue.popleft()
	    max_sum = (max_sum + A[queue[0]])%(10**9+7)
	    
	return max_sum 
	    
	    
def find_min(A, B):
    n = len(A)
	queue = deque()
	window_start = 0
	min_sum = 0
	    
	queue.append(0)
	for i in range(1, B):
	    while len(queue) != 0 and A[i] <= A[queue[len(queue)-1]]:
	        queue.pop()
	    queue.append(i)
	min_sum = (min_sum + A[queue[0]])%(10**9+7)
	    
	for i in range(B, n):
	    window_start += 1
	    while len(queue) != 0 and A[i] <= A[queue[len(queue)-1]]:
	        queue.pop()
	    queue.append(i)
	    if queue[0] < window_start:
	        queue.popleft()
	    min_sum = (min_sum + A[queue[0]])%(10**9+7)
	    
	return min_sum    
    

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        
        max_sum = find_max(A, B)
        min_sum = find_min(A, B)
        return (max_sum + min_sum)%(10**9+7)
        
