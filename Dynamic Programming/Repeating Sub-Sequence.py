"""

Repeating Sub-Sequence
Problem Description

Given a string A, find if there is any subsequence that repeats itself.

A subsequence of a string is defined as a sequence of characters generated by deleting some characters in the string without changing the order of the remaining characters.

NOTE: Sub-sequence length should be greater than or equal to 2.



Problem Constraints
1 <= length(A) <= 100



Input Format
The first and the only argument of input contains a string A.



Output Format
Return an integer, 1 if there is any subsequence which repeat itself else return 0.



Example Input
Input 1:

 A = "abab"
Input 2:

 A = "abba"


Example Output
Output 1:

 1
Output 2:

 0


Example Explanation
Explanation 1:

 "ab" is repeated.
Explanation 2:

 There is no repeating subsequence.


"""


# Just same as LCS but take second string same as first and do for different indices i.e. i != j

class Solution:
	# @param A : string
	# @return an integer
	def anytwo(self, A):
	    len_a = len(A)
        
        lcs = [[0 for j in range(len_a + 1)] for i in range(len_a + 1)]
        
        for i in range(len_a + 1):
            for j in range(len_a + 1):
                
                if i == 0 or j == 0:
                    lcs[i][j] = 0
                
                elif A[i-1] == A[j-1] and i != j:
                    lcs[i][j] = 1 + lcs[i-1][j-1]
                    
                else:
                    lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
                    
        return 1 if lcs[-1][-1] >= 2 else 0
	    
