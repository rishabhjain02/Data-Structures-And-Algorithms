"""

Palindrome Partitioning II
Problem Description

Given a string A, partition A such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of A.



Problem Constraints
1 <= length(A) <= 501



Input Format
The first and the only argument contains the string A.



Output Format
Return an integer, representing the minimum cuts needed.



Example Input
Input 1:

 A = "aba"
Input 2:

 A = "aab"


Example Output
Output 1:

 0
Output 2:

 1


Example Explanation
Explanation 1:

 "aba" is already a palindrome, so no cuts are needed.
Explanation 2:

 Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.


"""


def palindrome(s, start, end):
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True

class Solution:
	# @param A : string
	# @return an integer
	def minCut(self, A):
	    n = len(A)
	    cuts = [n-1]*n
	    cuts[0] = 0
	    
	    if palindrome(A, 0, n-1):
	        return 0
	        
	    for i in range(1, n):
	        for j in range(i+1):
	            if palindrome(A, j, i):
	                if j == 0:
	                    cuts[i] = 0
	                else:
	                    cuts[i] = min(cuts[i], cuts[j-1] + 1)
	                    
	    return cuts[-1]
	    
