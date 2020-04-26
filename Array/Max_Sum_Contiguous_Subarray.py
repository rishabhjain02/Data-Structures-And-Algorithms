"""

Max Sum Contiguous Subarray
Problem Description
Find the contiguous subarray within an array, A of length N which has the largest sum.


Problem Constraints
1 <= N <= 1e6
-1000 <= A[i] <= 1000


Input Format
The first and the only argument contains an integer array, A.


Output Format
Return an integer representing the maximum possible sum of the contiguous subarray.


Example Input
Input 1:
 A = [1, 2, 3, 4, -10] 
 Input 2:
 A = [-2, 1, -3, 4, -1, 2, 1, -5, 4] 
 


Example Output
Output 1:
 10 
 Output 2:
 6 
 


Example Explanation
Explanation 1:
 The subarray [1, 2, 3, 4] has the maximum possible sum of 10. 
 Explanation 2:
 The subarray [4,-1,2,1] has the maximum possible sum of 6. 

"""

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        max_so_far = A[0]
        max_ending_here = 0
        
        for i in range(0, len(A)): 
            max_ending_here = max_ending_here + A[i] 
            
            max_so_far = max(max_so_far, max_ending_here) 
  
            if max_ending_here < 0: 
                max_ending_here = 0  
                
        return max_so_far
