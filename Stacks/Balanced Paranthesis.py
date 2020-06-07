"""

Balanced Paranthesis
Problem Description

Given an expression string A, examine whether the pairs and the orders of “{“,”}”, ”(“,”)”, ”[“,”]” are correct in A.

Refer to the examples for more clarity.



Problem Constraints
1 <= |A| <= 100



Input Format
The first and the only argument of input contains the string A having the paranthesis sequence.



Output Format
Return 0, if the paranthesis sequence is not balanced.

Return 1, if the paranthesis sequence is balanced.



Example Input
Input 1:

 A = {([])}
Input 2:

 A = (){
Input 3:

 A = ()[] 


Example Output
Output 1:

 1 
Output 2:

 0 
Output 3:

 1 


Example Explanation
You can clearly see that the first and third case contain valid paranthesis.

In the second case, there is no closing bracket for {, thus the paranthesis sequence is invalid.

"""

class Solution:
	# @param A : string
	# @return an integer
	def solve(self, A):
	    
	    stack = []
	    opening = set('{([')
	    matches = set([('{','}'), ('(',')'), ('[',']')])
	    
	    for par in A:
	        
	        if par in opening:
	            stack.append(par)
	        
	        else:
	            if stack == []:
	                return 0
	            last_open = stack.pop()
	            if (last_open, par) not in matches:
	                return 0
	    
	    if stack == []:
	        return 1
	    return 0
	            
	    