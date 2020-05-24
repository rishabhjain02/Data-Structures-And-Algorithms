"""

Generate all Parentheses II
Problem Description
Given an integer A pairs of parentheses, write a function to generate all combinations of well-formed parentheses of length 2*A.


Problem Constraints
1 <= A <= 20


Input Format
First and only argument is integer A.


Output Format
Return a sorted list of all possible paranthesis.


Example Input
Input 1:
A = 3
  Input 2:          
A = 1
      


Example Output
Output 1:
[ "((()))", "(()())", "(())()", "()(())", "()()()" ]
  Output 2:          
[ "()" ]
      


Example Explanation
Explanation 1:
 All paranthesis are given in the output list.
  Explanation 2:          
 All paranthesis are given in the output list.

"""

class Solution:
	# @param A : integer
	# @return a list of strings
	
	def generate(self, A, cur_idx, open, close, cur_set, ans):
	    if cur_idx == 2*A:
	        ans.append("".join(cur_set))
	        
	    if open > 0:
	        cur_set.append('(')
	        self.generate(A, cur_idx+1, open-1, close, cur_set, ans)
	        cur_set.pop()
	        
	    if close > open:
	        cur_set.append(')')
	        self.generate(A, cur_idx+1, open, close-1, cur_set, ans)
	        cur_set.pop()
	        
	def generateParenthesis(self, A):
	    open = A
	    close = A
	    ans = []
	    cur_set = []
	    self.generate(A, 0, open, close, cur_set, ans)
	    return ans
