"""

Trailing Zeros in Factorial
Problem Description
Given an integer A, return the number of trailing zeroes in A! i.e. factorial of A. Note: Your solution should run in logarithmic time complexity.    


Problem Constraints
1 <= A <= 10^9


Input Format
First and only argument is a single integer A.


Output Format
Return a single integer denoting number of zeroes.


Example Input
Input 1
 A = 5
Input 2:
 A = 6
 


Example Output
Output 1:
 1
Output 2:
 1
 


Example Explanation
Explanation 1:
 A! = 120.
 Number of trailing zeros = 1. So, return 1.
Explanation 2:
 A! = 720 
 Number of trailing zeros = 1. So, return 1.

"""

class Solution:
	# @param A : integer
	# @return an integer
	def trailingZeroes(self, A):
	    count = 0
        i=5
        while (A/i>=1): 
            count += A//i 
            i *= 5
      
        return count 
