"""

Redundant Braces
Problem Description

Given a string A denoting an expression. It contains the following operators '+', '-', '*', '/'.

Chech whether A has redundant braces or not.

NOTE: A will be always a valid expression.



Problem Constraints
1 <= |A| <= 1000



Input Format
The only argument given is string A.



Output Format
Return 1 if A has redundant braces, else return 0.



Example Input
Input 1:

 A = "((a+b))"
Input 2:

 A = "(a+(a+b))"


Example Output
Output 1:

 1
Output 2:

 0


Example Explanation
Explanation 1:

 ((a+b)) has redundant braces so answer will be 1.
Explanation 2:

 (a+(a+b)) doesn't have have any redundant braces so answer will be 0.

"""

class Solution:
	# @param A : string
	# @return an integer
	def braces(self, A):
	    count_braces = 0
	    count_operators = 0
	    operators = set(['+', '-', '*', '/'])
	    
	    for i in range(len(A)):
	        if A[i] == '(' and A[i+2] == ')':
	            return 1
	            
	        if A[i] == '(':
	            count_braces += 1
	        
	        if A[i] in operators:
	            count_operators += 1
	    
	    if count_braces > count_operators:
	        return 1
	    return 0
