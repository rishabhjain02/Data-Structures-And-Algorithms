"""

Longest valid Parentheses
Problem Description

Given a string A containing just the characters '(' and ')'.

Find the length of the longest valid (well-formed) parentheses substring.



Problem Constraints
1 <= length(A) <= 750000



Input Format
The only argument given is string A.



Output Format
Return the length of the longest valid (well-formed) parentheses substring.



Example Input
Input 1:

 A = "(()"
Input 2:

 A = ")()())"


Example Output
Output 1:

 2
Output 2:

 4


Example Explanation
Explanation 1:

 The longest valid parentheses substring is "()", which has length = 2.
Explanation 2:

 The longest valid parentheses substring is "()()", which has length = 4.


"""


class Solution:
	# @param A : string
	# @return an integer
	def longestValidParentheses(self, A):
	    stack = [-1]
	    ans = 0
	    
	    for i in range(len(A)):
	        
	        if A[i] == '(':
	            stack.append(i)
	            
	        else:
	            val = stack.pop()
	            
	            if val != -1 and A[val] == '(':
	                ans = max(ans, i - stack[-1])
	                
	            else:
	                stack.append(i)
	                
	    return ans
