"""

Ways to Decode
Problem Description

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message denoted by string A containing digits, determine the total number of ways to decode it modulo 109 + 7.

.



Problem Constraints
1 <= length(A) <= 10^5



Input Format
The first and the only argument is a string A.



Output Format
Return an integer, representing the number of ways to decode the string modulo 109 + 7..



Example Input
Input 1:

 A = "12"
Input 2:

 A = "8"


Example Output
Output 1:

 2
Output 2:

 1


Example Explanation
Explanation 1:

 Given encoded message "8", it could be decoded as only "H" (8).
 The number of ways decoding "8" is 1.
Explanation 2:

 Given encoded message "12", it could be decoded as "AB" (1, 2) or "L" (12).
 The number of ways decoding "12" is 2.


"""


class Solution:
	# @param A : string
	# @return an integer
	def numDecodings(self, A):
	    n = len(A)
	    dp = [0]*(n+1)
	    mod = 10**9+7
	    dp[0]= 1
	    dp[1] = 1 if A[0] != '0' else 0
	    
	    for i in range(2, n+1):
	        val1 = int(A[i-1])
	        val2 = int(A[i-2:i])
	        
	        if val1 != 0:
	            dp[i] = (dp[i] + dp[i-1])%mod
	            
	        if val2 >= 10 and val2 <= 26:
	            dp[i] = (dp[i] + dp[i-2])%mod
	            
	    return dp[-1]
	    
	    
