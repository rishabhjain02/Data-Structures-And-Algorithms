"""

Minimum Number of Squares
Problem Description

Given an integer A. Return minimum count of numbers, sum of whose squares is equal to A.



Problem Constraints
1 <= A <= 10^5



Input Format
First and only argument is an inetegr A.



Output Format
Return an integer denoting the minimum count.



Example Input
Input 1:

 A = 6
Input 2:

 A = 5


Example Output
Output 1:

 3
Output 2:

 2


Example Explanation
Explanation 1:

 Possible combinations are : (12 + 12 + 12 + 12 + 12 + 12) and (12 + 12 + 22).
 Minimum count of numbers, sum of whose squares is 6 is 3. 
Explanation 2:

 We can represent 5 using only 2 numbers i.e. 12 + 22 = 5

"""


class Solution:
	# @param A : integer
	# @return an integer
	def countMinSquares(self, n):
	    
        dp = [0]*(n+1)
        squares = []
        i = 1
    
        dp[1] = 1
    
        while i*i <= n:
	        squares.append(i*i)
	        i += 1

        for i in range(2, n+1):
            dp[i] = i
            
            for x in squares:
                if x > i:
                    break
                
                dp[i] = min(dp[i], 1 + dp[i-x])
    
        return dp[n]