"""

Excel Column Title
Problem Description
Given a positive integer A, return its corresponding column title as appear in an Excel sheet. For example:
    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
   


Problem Constraints
1 <= A <= 10^9


Input Format
First and only argument of input contains single integer A


Output Format
Return a string denoting the corresponding title.


Example Input
 A = 27


Example Output
 "AA"


Example Explanation
    1 -> A,
    2 -> B,
    3 -> C,
    ...
    26 -> Z,
    27 -> AA,
    28 -> AB 


"""

	class Solution:
	# @param A : integer
	# @return a strings
	def convertToTitle(self, A):
	    ans = ""
        n = A
        while(n>0):
            rem = n%26
            if rem == 0:
                ans += "Z"
                n = (n//26) - 1
            
            else:
                ans += str(chr(rem+64))
                n = n // 26

        return ans[::-1]
