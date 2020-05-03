"""

SUMMATION
Problem Description
Given an integer A. Calculate the sum = (ACr) * (r) * (r - 1) * (2r-2) for all r from 0 to A. Return sum % 10^9 + 7.  


Problem Constraints
2 <= A <= 10^6


Input Format
The first and only argument given is the integer A.


Output Format
Return a single integer denoting sum % 10^9 + 7.


Example Input
Input 1:
 A = 3
Input 2:
 A = 4
 


Example Output
Output 1:
 18
Output 2:
 108
 


Example Explanation
Explaination 1:
 (ACr) * (r) * (r - 1) * (2r-2)
 r = 0, (1) * (0) * (1) * (1/4) = 0
 r = 1, (3) * (1) * (0) * (1/2) = 0
 r = 2, (3) * (2) * (1) * (1) = 6
 r = 3, (1) * (3) * (2) * (2) = 12
 sum = 18

"""

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        n = A
        def findPower(n,e):
            if e == 0:
                return 1
            result = (findPower(n*n%(10**9+7),e//2))%(10**9+7)
            if e%2 == 0:
                return result
            return result*n%(10**9+7)
            
        ans = (n * (n-1) * findPower(3,(n-2)))%(10**9+7)
        
        return ans
        
        
