"""

Excel Column Number
Problem Description
Given a column title as appears in an Excel sheet, return its corresponding column number.


Problem Constraints
1 <= length of the column title <= 5


Input Format
Input a string which represents the column title in excel sheet.


Output Format
Return a single integer which represents the corresponding column number.


Example Input
Input 1:
 AB
Input 2:
 ABCD
      


Example Output
Output 1:
 28
Output 2:
 19010
       


Example Explanation
Explanation 1:
 A -> 1
 B -> 2
 C -> 3
 ...
 Z -> 26
 AA -> 27
 AB -> 28

"""

class Solution:
	# @param A : string
	# @return an integer
	def titleToNumber(self, A):
	    ans = 0
        n = len(A)
        for i in range(len(A)):
            ans += (26**(n-1))*(ord(A[i])-64)
            n -= 1
            
        return ans
