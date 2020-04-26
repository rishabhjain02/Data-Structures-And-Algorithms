"""

Delete one
Problem Description
Given an integer array A of size N. You have to delete one element such that the GCD(Greatest common divisor) of the remaining array is maximum.

Find the maximum value of GCD.


Problem Constraints
2 <= N <= 10^5
1 <= A[i] <= 10^9


Input Format
First argument is an integer array A.


Output Format
Return an integer denoting the maximum value of GCD.


Example Input
Input 1:
 A = [12, 15, 18]
Input 2:
 A = [5, 15, 30]
 


Example Output
Output 1:
 6
Output 2:
 15
 


Example Explanation
Explanation 1:
 
 If you delete 12, gcd will be 3.
 If you delete 15, gcd will be 6.
 If you delete 18, gcd will 3.
 Maximum vallue of gcd is 6.
Explanation 2:
 If you delete 5, gcd will be 15.
 If you delete 15, gcd will be 5.
 If you delete 30, gcd will be 5.

"""

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        if n==2:
            return max(A)
        def gcd(a,b):
            if b==0:
                return abs(a)
            return gcd(b,a%b)
        
        left_gcd = [0] * n
        right_gcd = [0] * n
        
        right_gcd[n-1] = A[n-1]
        for i in range(n-2,-1,-1):
            right_gcd[i] = gcd(A[i],right_gcd[i+1])
        
        left_gcd[0] = A[0]
        ans = 0
        for i in range(1,n-1):
            left_gcd[i] = gcd(left_gcd[i-1],A[i])
            ans = max(ans,gcd(left_gcd[i-1],right_gcd[i+1]))
            
        return ans
            
            
