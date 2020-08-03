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
        n = len(A)
        count = -1
        k = n
        
        lps = [[0 for i in range(n)] for j in range(n)]
        
        for c in range(n):
            count += 1
            
            for i in range(k):
                j = i + count
                
                if i == j:
                    lps[i][j] = 1
                
                elif A[i] == A[j]:
                    lps[i][j] = 2 + lps[i+1][j-1]
                    
                else:
                    lps[i][j] = max(lps[i+1][j], lps[i][j-1])
                    
            k -= 1        
                    
        return lps[0][n-1]
                    
                    