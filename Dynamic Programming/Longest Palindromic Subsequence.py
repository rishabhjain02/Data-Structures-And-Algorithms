"""

Longest Palindromic Subsequence
Problem Description

Given a string A. Find the longest palindromic subsequence (A subsequence which does not need to be contiguous and is a palindrome).

You need to return the length of longest palindromic subsequence.



Problem Constraints
1 <= length of(A) <= 10^3



Input Format
First and only integer is a string A.



Output Format
Return an integer denoting the length of longest palindromic subsequence.



Example Input
Input 1:

 A = "bebeeed"
Input 2:

 A = "aedsead"


Example Output
Output 1:

 4
Output 2:

 5


Example Explanation
Explanation 1:

 The longest palindromic subsequence is "eeee", which has a length of 4.
Explanation 2:

 The longest palindromic subsequence is "aedea", which has a length of 5.


"""


class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        len_a = len(A)
        
        lcs = [[0 for j in range(len_a+1)] for i in range(len_a+1)]
        
        for i in range(len_a + 1):
            for j in range(len_a + 1):
                
                if i == 0 or j == 0:
                    lcs[i][j] = 0
                
                elif A[i-1] == A[(len_a - 1) - (j - 1)]:
                    lcs[i][j] = 1 + lcs[i-1][j-1]
                    
                else:
                    lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
                    
        return lcs[-1][-1]
        
        

        
