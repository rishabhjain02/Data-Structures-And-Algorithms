"""

Maximum Sum
Problem Description

You are given an array A of N integers and three integers B, C, and D.

You have to find the maximum value of A[i]*B + A[j]*C + A[k]*D, where 1 <= i <= j <= k <= N.



Problem Constraints
1 <= N <= 10^5

-10000 <= A[i], B, C, D <= 10000



Input Format
First argument is an array A
Second argument is an integer B
Third argument is an integer C
Fourth argument is an integer D



Output Format
Return an Integer S, i.e maximum value of (A[i] * B + A[j] * C + A[k] * D), where 1 <= i <= j <= k <= N.



Example Input
Input 1:

 A = [1, 5, -3, 4, -2]
 B = 2
 C = 1
 D = -1
Input 2:

 A = [3, 2, 1]
 B = 1
 C = -10
 D = 3


Example Output
Output 1:

 18
Output 2:

 -4


Example Explanation
Explanation 1:

 If you choose i = 2, j = 2, and k = 3 then we will get
 A[2]*B + A[2]*C + A[3]*D = 5*2 + 5*1 + (-3)*(-1) = 10 + 5 + 3 = 18
Explanation 2:

 If you choose i = 1, j = 3, and k = 3 then we will get
 A[1]*B + A[3]*C + A[3]*D = (3*1) + (-10*1) + (3*1) = 3 - 10 + 3 = -4


"""


# DP Approach

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @return an integer
    def solve(self, A, B, C, D):
        n = len(A)
        dp = [[float("-inf") for i in range(3)] for j in range(n+1)]
        
        for i in range(1, n+1):
            dp[i][0] = max(dp[i-1][0], A[i-1]*B)
            dp[i][1] = max(dp[i-1][1], dp[i][0] + A[i-1]*C)
            dp[i][2] = max(dp[i-1][2], dp[i][1] + A[i-1]*D)
            
        return dp[n][2]
            

# Second Approach: Using prefix and suffix

# def compute_prefix(A, B, prefix):
#     n = len(A)
#     prefix[0] = A[0]*B
    
#     for i in range(1, n):
#         prefix[i] = max(A[i]*B, prefix[i-1])
        
        
# def compute_suffix(A, D, suffix):
#     n = len(A)
#     suffix[n-1] = A[n-1]*D
    
#     for i in range(n-2, -1, -1):
#         suffix[i] = max(A[i]*D, suffix[i+1])


# class Solution:
#     # @param A : list of integers
#     # @param B : integer
#     # @param C : integer
#     # @param D : integer
#     # @return an integer
#     def solve(self, A, B, C, D):
#         n = len(A)
#         prefix = [0]*n
#         suffix = [0]*n
#         max_val = float("-inf")
        
#         compute_prefix(A, B, prefix)
        
#         compute_suffix(A, D, suffix)
        
#         for i in range(n):
#             max_val = max(max_val, prefix[i] + A[i]*C + suffix[i])
            
#         return max_val
        
        
