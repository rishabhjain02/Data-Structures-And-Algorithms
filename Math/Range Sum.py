"""

Range Sum
Problem Description
Given two integers A and B such that A <= B. A Function F is defined as follows:
F[0] = 0
F[1] = 1
F[n] = F[n-1] + F[n-2]; n > 1
Function S(A, B) = F[A] + F[A+1] + F[A+2] + ... + F[B]. Find and return S(A, B) modulo (10^9+7).  


Problem Constraints
0 <= A <= B <= 10^9


Input Format
The arguments given are two integers A and B.


Output Format
Return an integer denoting the value of S(A, B) modulo (109+7).


Example Input
Input 1:
 A = 0
 B = 3
Input 2:
 A = 3
 B = 4
 


Example Output
Output 1:
 4
Output 2:
 5
 


Example Explanation
Explanation 1:
 F(0) = 0, F(1) = 1, F(2) = 1, F(3) = 2.
 S(0, 3) = F(0) + F(1) + F(2) + F(3) = 0 + 1 + 1 + 2 = 4.
Explanation 2:
 F(3) = 2, F(4) = 3.
 S(3, 4) = F(3) + F(4) = 2 + 3 = 5.

"""

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        
        def fib(n):
            F = [[1,1], [1,0]]
            if n==0:
                return 0
            power(F, n-1)
            return F[0][0]
            
        def multiply(F, M):
            a = ((F[0][0] * M[0][0])%(10**9+7) + (F[0][1] * M[1][0])%(10**9+7))%(10**9+7)
            b = ((F[0][0] * M[0][1])%(10**9+7) + (F[0][1] * M[1][1])%(10**9+7))%(10**9+7)
            c = ((F[1][0] * M[0][0])%(10**9+7) + (F[1][1] * M[1][0])%(10**9+7))%(10**9+7)
            d = ((F[1][0] * M[0][1])%(10**9+7) + (F[1][1] * M[1][1])%(10**9+7))%(10**9+7)
            
            F[0][0] = a 
	        F[0][1] = b 
	        F[1][0] = c 
	        F[1][1] = d 
            
        def power(F,n):
            if n==0 or n==1:
                return 
            M = [[1,1], [1,0]]
            power(F, n//2)
            multiply(F, F)
            
            if (n % 2 != 0): 
                multiply(F, M) 
        
        sum_left_A = fib(A+1) - 1
        sum_upto_B = fib(B+2) - 1
        return (sum_upto_B - sum_left_A)%(10**9+7)
        
        