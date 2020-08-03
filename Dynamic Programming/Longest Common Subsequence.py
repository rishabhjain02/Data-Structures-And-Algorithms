"""

Longest Common Subsequence
Problem Description

Given two strings A and B. Find the longest common subsequence ( A sequence which does not need to be contiguous), which is common in both the strings.

You need to return the length of such longest common subsequence.



Problem Constraints
1 <= Length of A, B <= 1005



Input Format
First argument is a string A.
Second argument is a string B.



Output Format
Return an integer denoting the length of the longest common subsequence.



Example Input
Input 1:

 A = "abbcdgf"
 B = "bbadcgf"
Input 2:

 A = "aaaaaa"
 B = "ababab"


Example Output
Output 1:

 5
Output 2:

 3


Example Explanation
Explanation 1:

 The longest common subsequence is "bbcgf", which has a length of 5.
Explanation 2:

 The longest common subsequence is "aaa", which has a length of 3.

"""


class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        len_a = len(A)
        len_b = len(B)
        
        lcs = [[0 for j in range(len_b+1)] for i in range(len_a+1)]
        
        for i in range(len_a + 1):
            for j in range(len_b + 1):
                
                if i == 0 or j == 0:
                    lcs[i][j] = 0
                
                elif A[i-1] == B[j-1]:
                    lcs[i][j] = 1 + lcs[i-1][j-1]
                    
                else:
                    lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
                    
        return lcs[-1][-1]
                    
