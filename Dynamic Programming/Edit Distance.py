"""

Edit Distance
Problem Description

Given two strings A and B, find the minimum number of steps required to convert A to B. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character


Problem Constraints
1 <= length(A), length(B) <= 450



Input Format
The first argument of input contains a string, A.
The second argument of input contains a string, B.



Output Format
Return an integer, representing the minimum number of steps required.



Example Input
Input 1:

 A = "abad"
 B = "abac"
Input 2:

 A = "Anshuman"
 B = "Antihuman


Example Output
Output 1:

 1
Output 2:

 2


Example Explanation
Exlanation 1:

 A = "abad" and B = "abac"
 After applying operation: Replace d with c. We get A = B.
 
Explanation 2:

 A = "Anshuman" and B = "Antihuman"
 After applying operations: Replace s with t and insert i before h. We get A = B.


"""


class Solution:
	# @param A : string
	# @param B : string
	# @return an integer
	def minDistance(self, A, B):
	    len_a = len(A)
	    len_b = len(B)
	    
	    steps = [[0 for i in range(len_b + 1)] for j in range(len_a + 1)]
	    
	    for i in range(len_a + 1):
	        for j in range(len_b + 1):
	            
	            if i == 0:
	                steps[i][j] = j
	                
	            elif j == 0:
	                steps[i][j] = i
	                
	            elif A[i-1] == B[j-1]:
	                steps[i][j] = steps[i-1][j-1]
	                
	            else:
	                steps[i][j] = 1 + min(steps[i][j-1], steps[i-1][j], steps[i-1][j-1])
	                
	    return steps[-1][-1]
	                
	                
