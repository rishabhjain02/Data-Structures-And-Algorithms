"""

Square Root of Integer
Problem Description
Given an integer A. Compute and return the square root of A. If A is not a perfect square, return floor(sqrt(A)). DO NOT USE SQRT FUNCTION FROM STANDARD LIBRARY.       


Problem Constraints
0 <= A <= 10^10


Input Format
The first and only argument given is the integer A.


Output Format
Return floor(sqrt(A))


Example Input
Input 1:
 11
Input 2:
 9
        


Example Output
Output 1:
 3
Output 2:
 3
        


Example Explanation
Explanation:
 When A = 11 , square root of A = 3.316. It is not a perfect square so we return the floor which is 3.
 When A = 9 which is a perfect square of 3, so we return 3.

"""

class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        def isPossible(n):
            if n*n<=A:
                return True
            else:
                return False
                
        low = 1
        high = A
        ans = 0
        while(low<=high):
            mid = low+(high-low)//2
            if isPossible(mid):
                ans = mid
                low = mid+1
            else:
                high = mid-1
        return ans
