"""

Max Rectangle in Binary Matrix
Problem Description

Given a 2-D binary matrix A of size N x M filled with 0's and 1's, find the largest rectangle containing all ones and return its area.



Problem Constraints
1 <= N, M <= 100



Input Format
First argument is an 2-D binary array A.



Output Format
Return an integer denoting the area of largest rectangle containing all ones.



Example Input
Input 1:

 A = [
       [1, 1, 1]
       [0, 1, 1]
       [1, 0, 0] 
     ]
Input 2:

 A = [
       [0, 1, 0]
       [1, 1, 1]
     ] 


Example Output
Output 1:

 4
Output 2:

 3


Example Explanation
Explanation 1:

 As the max area rectangle is created by the 2x2 rectangle created by (0,1), (0,2), (1,1) and (1,2).
Explanation 2:

 As the max area rectangle is created by the 1x3 rectangle created by (1,0), (1,1) and (1,2).


"""


# Function to find Largest Rectangle area for that row (Refer problem: Largest Rectangle in Histogram)
def solve_histogram(A):
    n = len(A)
    stack = [0]
	left = [-1]*n
	right = [n]*n
	
	# Finding the index of nearest smaller element in left side
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
	    
	# Finding the index of nearest smaller element in right side    
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


class Solution:
	# @param A : list of list of integers
	# @return an integer
	def maximalRectangle(self, A):
	    n = len(A)
        m = len(A[0])
        height = [[0 for i in range(m)] for j in range(n)]
        ans = float("-inf")
        
        # Compute height(continuous 1 above) for each element
        for i in range(n):
            for j in range(m):
                if A[i][j] != 0:
                    height[i][j] = height[i-1][j] + 1
                    
        # Now take each row of height and find max_area possible like histogram problem
        for row in height:
            area = solve_histogram(row)
            # ans will be the max(area possible for each row)
            ans = max(ans, area)
            
        return ans
	    
