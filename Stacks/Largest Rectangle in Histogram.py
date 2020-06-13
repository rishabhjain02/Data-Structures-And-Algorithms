"""

Largest Rectangle in Histogram
Problem Description

Given an array of integers A .

A represents a histogram i.e A[i] denotes height of the ith histogram's bar. Width of each bar is 1.

Find the area of the largest rectangle formed by the histogram.



Problem Constraints
1 <= |A| <= 100000

1 <= A[i] <= 1000000000



Input Format
The only argument given is the integer array A.



Output Format
Return the area of largest rectangle in the histogram.



Example Input
Input 1:

 A = [2, 1, 5, 6, 2, 3]
Input 2:

 A = [2]


Example Output
Output 1:

 10
Output 2:

 2


Example Explanation
Explanation 1:

The largest rectangle has area = 10 unit. Formed by A[3] to A[4].
Explanation 2:

Largest rectangle has area 2.

"""

class Solution:
	# @param A : list of integers
	# @return an integer
	def largestRectangleArea(self, A):
	    n = len(A)
	    stack = [0]
	    left = [-1]*n
	    right = [n]*n
	    
	    for i in range(1,n):
	        if stack != [] and A[stack[-1]] < A[i]:
	            left[i] = stack[-1]
	            stack.append(i)
	            
	        else:
	            while stack != [] and A[stack[-1]] >= A[i]:
	                stack.pop()
	            if stack != []:
	                left[i] = stack[-1]
	                
	            stack.append(i)
	            
	            
	    stack = []
	    stack.append(n-1)
	    
	    for i in range(n-2, -1, -1):
	        if stack != [] and A[stack[-1]] < A[i]:
	            right[i] = stack[-1]
	            stack.append(i)
	            
	        else:
	            while stack != [] and A[stack[-1]] >= A[i]:
	                stack.pop()
	            if stack != []:
	                right[i] = stack[-1]
	                
	            stack.append(i)
	            
	    max_area = float("-inf")
	    
	    for i in range(n):
	        val = (right[i] - left[i] - 1)*A[i]
	        max_area = max(max_area, val)
	    
	    return max_area
	    
