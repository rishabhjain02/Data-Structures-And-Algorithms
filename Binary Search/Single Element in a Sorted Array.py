"""

Single Element in a Sorted Array
Problem Description
Given a sorted array of integers A where every element appears twice except for one element which appears once, find and return this single element that appears only once.


Problem Constraints
1 <= |A| <= 100000 1 <= A[i] <= 10^9 


Input Format
The only argument given is the integer array A.


Output Format
Return the single element that appears only once.


Example Input
Input 1:
A = [1, 1, 7]
  Input 2:      
A = [2, 3, 3]
    


Example Output
Output 1:
 7
  Output 2:      
 2
    


Example Explanation
Explanation 1:
 7 appears once
  Explanation 2:      
 2 appears once

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
            if mid == 0 and A[mid] != A[mid+1]:
                return A[mid]
            elif mid == n-1 and A[mid] != A[mid-1]:
                return A[mid]
            elif A[mid] != A[mid-1] and A[mid] != A[mid+1]:
                return A[mid]
            elif A[mid] == A[mid-1] and mid%2 != 0:
                low = mid+1
            elif A[mid] == A[mid-1] and mid%2 == 0:
                high = mid-2
            elif A[mid] == A[mid+1] and mid%2 == 0:
                low = mid+2
            else:
                high = mid-1
                
