"""

Find a peak element
Problem Description
Given an array of integers A, find and return the peak element in it. An array element is peak if it is NOT smaller than its neighbors. For corner elements, we need to consider only one neighbor. We ensure that answer will be unique.   


Problem Constraints
1 <= |A| <= 100000 1 <= A[i] <= 10^9   


Input Format
The only argument given is the integer array A.


Output Format
Return the peak element.


Example Input
Input 1:
A = [1, 2, 3, 4, 5]
  Input 2:          
A = [5, 17, 100, 11]
      


Example Output
Output 1:
 5
  Output 2:          
 100
      


Example Explanation
Explanation 1:
 5 is the peak.
  Explanation 2:          
 100 is the peak.

"""

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        low = 0
        high = n-1
        while(low <= high):
            mid = low + (high-low)//2
            if mid == 0 and A[mid] >= A[mid+1]:
                return A[mid]
            elif mid == n-1 and A[mid] >= A[mid-1]:
                return A[mid]
            elif A[mid]>=A[mid-1] and A[mid]>=A[mid+1]:
                return A[mid]
            elif A[mid-1]>A[mid]:
                high = mid-1
            else:
                low = mid+1
                    
            
