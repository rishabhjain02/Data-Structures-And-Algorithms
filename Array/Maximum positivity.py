"""

Maximum positivity
Problem Description
Given an array of integers A of size N. Return maximum size subarray of A having only non-negative elements. If there are more than one such subarrays, return the one having earliest starting index in A.    


Problem Constraints
1 <= N <= 10^5 -109 <= A[i] <= 10^9 


Input Format
The first and only argument given is the integer array A.


Output Format
Return maximum size subarray of A having only non-negative elements. If there are more than one such subarrays, return the one having earliest starting index in A.


Example Input
Input 1:
 A = [5, 6, -1, 7, 8]
  Input 2:
 A = [1, 2, 3, 4, 5, 6]
  


Example Output
Output 1:
 [5, 6]
  Output 2:
 A = [1, 2, 3, 4, 5, 6]
  


Example Explanation
Explanation 1:
 There are two subarrays of size 2 having only non-negative elements.
 1. [5, 6]  starting point  = 0
 2. [7, 8]  starting point  = 3
 As starting point of 1 is smaller, return [5, 6]
  Explanation 2:
 There is only one subarray of size 6 having only non-negative elements:
 [1, 2, 3, 4, 5, 6]

"""

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        n = len(A)
        cur_max, max_so_far, start, end = 0, 0, 0, 0
        res_left, res_right = -1, -1
        while(end<n):
            if A[end] >= 0:
                cur_max += 1
                if cur_max > max_so_far:
                    max_so_far = cur_max
                    res_left = start
                    res_right = end
                end += 1
            
            else:
                cur_max = 0
                end += 1
                start = end
                
        return A[res_left:res_right+1]
                    
                
