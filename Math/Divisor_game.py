"""

Divisor game
Problem Description
Scooby has 3 three integers A, B and C. Scooby calls a positive integer special if it is divisible by B and it is divisible by C. You need to tell number of special integers less than or equal to A.   


Problem Constraints
1 <= A, B, C <= 1000000000


Input Format
A positive integer A
A positive integer B
A positive integer C


Output Format
One integer corresponding to the number of special integers less than or equal to A.


Example Input
 A=12, B=3, C=2


Example Output
 2


Example Explanation
 The two integers divisible by 2 and 3 and less than or equal to 12 are 6,12.

"""

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        def gcd(a,b):
            if b==0:
                return abs(a)
            return gcd(b,a%b)
        
        lcm = (B*C)//gcd(B,C)
        return A//lcm