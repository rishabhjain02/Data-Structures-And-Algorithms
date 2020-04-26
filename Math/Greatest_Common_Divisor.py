"""

Greatest Common Divisor
Problem Description
Given 2 non negative integers A and B, find gcd(A, B) GCD of 2 integers A and B is defined as the greatest integer g such that g is a divisor of both A and B. Both A and B fit in a 32 bit signed integer. Note: DO NOT USE LIBRARY FUNCTIONS. 


Problem Constraints
0 <= A, B <= 10^9


Input Format
First argument is an integer A.
Second argument is an integer B.


Output Format
Return an integer denoting the gcd(A, B).


Example Input
Input 1:
A = 6
B = 3


Example Output
Output 1:
3


Example Explanation
Explanation 1:
GCD(3, 6) = 3 as 3 divides both 3 and 6.

"""

class Solution:
	# @param A : integer
	# @param B : integer
	# @return an integer
	def gcd(self, A, B):
	    if B == 0:
	        return abs(A)
	    return self.gcd(B,A%B)