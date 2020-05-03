"""

First Missing Integer
Problem Description
Given an unsorted integer array A of size N. Find the first missing positive integer. Note: Your algorithm should run in O(n) time and use constant space.    


Problem Constraints
1 <= N <= 1000000 -10^9 <= A[i] <= 10^9    


Input Format
First argument is an integer array A.


Output Format
Return an integer denoting the first missing positive integer.


Example Input
Input 1:
[1, 2, 0]
Input 2:
[3, 4, -1, 1]
Input 3:
[-8, -7, -6]
   


Example Output
Output 1:
3
Output 2:
2
Output 3:
1
   


Example Explanation
Explanation 1:
A = [1, 2, 0]
First positive integer missing from the array is 3.

"""

class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        n = len(A)
        i = 0
        while(i<n):
            val = A[i]
            if val <= n and val >= 1 and val != A[val-1]:
                A[i], A[val-1] = A[val-1], A[i]
            else:
                i += 1
        
        for i in range(0,n):
            if A[i] != i+1:
                return i+1
        
        return n+1
            
            
