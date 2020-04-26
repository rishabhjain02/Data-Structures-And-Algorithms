"""

Consecutive Number Sum
Problem Description
Given an integer A. Return number of ways we can write A as a sum of consecutive positive integers.


Problem Constraints
1 <= A <= 10^9


Input Format
The first argument given is the integer A.


Output Format
Return number of ways we can write A as a sum of consecutive positive integers.


Example Input
A = 9


Example Output
3


Example Explanation
A = 9
A = 2 + 3 + 4
A = 5 + 4

"""

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        m = 1
        ans = 0
        while((2*A - m*(m-1))>0):
            exp = (2*A - m*(m-1))%(2*m) 
            if exp == 0:
                ans += 1
            m+=1
        return ans
