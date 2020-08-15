"""

Length of Longest Fibonacci Subsequence
Problem Description

Given a strictly increasing array A of positive integers forming a sequence.

A sequence X1, X2, X3, ..., XN is fibonacci like if


N > =3
Xi + Xi+1 = Xi+2 for all i+2 <= N
Find and return the length of the longest Fibonacci-like subsequence of A.

If one does not exist, return 0.

NOTE: A subsequence is derived from another sequence A by deleting any number of elements (including none) from A, without changing the order of the remaining elements.



Problem Constraints
3 <= length of the array <= 1000

1 <= A[i] <= 10^9



Input Format
The only argument given is the integer array A.



Output Format
Return the length of the longest Fibonacci-like subsequence of A.
If one does not exist, return 0.



Example Input
Input 1:

 A = [1, 2, 3, 4, 5, 6, 7, 8]
Input 2:

 A = [1, 3, 7, 11, 12, 14, 18]


Example Output
Output 1:

 5
Output 2:

 3


Example Explanation
Explanation 1:

 The longest subsequence that is fibonacci-like: [1, 2, 3, 5, 8].
Explanation 2:

 The longest subsequence that is fibonacci-like: [1, 11, 12], [3, 11, 14] or [7, 11, 18].
 The length will be 3.

"""


from collections import defaultdict

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        index = defaultdict(int)
        max_length = 2
        
        for i in range(n):
            index[A[i]] = i
            
        dp = [[2 for j in range(n)] for i in range(n)]
        
        for k in range(n):
            for j in range(k):
                required_val = A[k] - A[j]
                
                if required_val in index:
                    i = index[required_val]
                    
                    if i < j:
                        dp[j][k] = 1 + dp[i][j]
                        max_length = max(max_length, dp[j][k])
                        
        if max_length == 2:
            return 0
        return max_length
        
