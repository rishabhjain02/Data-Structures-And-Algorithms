"""

Regular Expression II
Problem Description

Implement wildcard pattern matching with support for ' ? ' and ' * ' for strings A and B.

' . ' : Matches any single character.
' * ' : Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).



Problem Constraints
1 <= length(A), length(B) <= 10^4



Input Format
The first argument of input contains a string A.
The second argument of input contains a string B denoting the pattern.



Output Format
Return 1 if the patterns match else return 0.



Example Input
Input 1:

 A = "aab"
 B = "c*a*b"
Input 2:

 A = "acz"
 B = "a.a"


Example Output
Output 1:

 1
Output 2:

 0


Example Explanation
Explanation 1:

 'c' can be repeated 0 times, 'a' can be repeated 1 time. Therefore, it matches "aab".
 So, return 1.
Explanation 2:

 '.' matches any single character. First two character in string A will be match. 
 But the last character i.e 'z' != 'a'. Return 0.


"""


class Solution:
	# @param A : string
	# @param B : string
	# @return an integer
	def isMatch(self, A, B):
	    len_a = len(A)
	    len_b = len(B)
	    
	    match = [[0 for j in range(len_b + 1)] for i in range(len_a + 1)]
	    
	    for i in range(len_a + 1):
	        for j in range(len_b + 1):
	            
	            if i == 0 and j == 0:
	                match[i][j] = 1
	                
	            elif j == 0:
	                match[i][j] = 0
	                
	            elif i == 0:
	                if B[j-1] == '*':
	                    match[i][j] = match[i][j-2]
	                    
	            elif B[j-1] == '*':
	                match[i][j] = match[i][j-2]
	                
	                if B[j-2] == '.' or A[i-1] == B[j-2]:
                        match[i][j] = match[i][j] or match[i-1][j]
                        
                elif A[i-1] == B[j-1] or B[j-1] == '.':
                    match[i][j] = match[i-1][j-1]
                    
        return match[-1][-1]
	       
