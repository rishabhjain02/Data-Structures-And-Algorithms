"""

Longest Balanced Substring
Problem Description

Given a string A made up of multiple brackets of type "[]" , "()" and "{}" find the length of the longest substring which forms a balanced string .

Conditions for a string to be balanced :

Blank string is balanced ( However blank string will not be provided as a test case ).
If B is balanced : (B) , [B] and {B} are also balanced.
If B1 and B2 are balanced then B1B2 i.e the string formed by concatenating B1 and B2 is also balanced.


Problem Constraints
0 <= |A| <= 10^6



Input Format
First and only argument is an string A.



Output Format
Return an single integer denoting the lenght of the longest balanced substring.



Example Input
Input 1:

 A = "[()]"
Input 2:

 A = "[(])"


Example Output
Output 1:

 4
Output 2:

 0


Example Explanation
Explanation 1:

 Substring [1:4] i.e "[()]" is the longest balanced substring of length 4.
Explanation 2:

 None of the substring is balanced so answer is 0.


"""


class Solution:
    # @param A : string
    # @return an integer
    def LBSlength(self, A):
        
        stack = [-1]
	    opening = set('{([')
	    matches = set([('{','}'), ('(',')'), ('[',']')])
	    ans = 0
	    
	    for i in range(len(A)):
	        
	        if A[i] in opening:
	            stack.append(i)
	            
	        else:
	            val = stack.pop()
	            
	            if val != -1 and (A[val], A[i]) in matches:
	                ans = max(ans, i - stack[-1])
	                
	            else:
	                stack.append(i)
	                
	    return ans
	    
