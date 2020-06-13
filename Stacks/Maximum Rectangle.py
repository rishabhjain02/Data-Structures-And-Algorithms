"""

Maximum Rectangle
Given a 2D binary matrix of integers A containing 0's and 1's of size N x M.

Find the largest rectangle containing only 1's and return its area.

Note: Rows are numbered from top to bottom and columns are numbered from left to right.


Input Format

The only argument given is the integer matrix A.
Output Format

Return the area of the largest rectangle containing only 1's.
Constraints

1 <= N, M <= 1000
0 <= A[i] <= 1
For Example

Input 1:
    A = [   [0, 0, 1]
            [0, 1, 1]
            [1, 1, 1]   ]
Output 1:
    4

Input 2:
    A = [   [0, 1, 0, 1]
            [1, 0, 1, 0]    ]
Output 2:
    1

"""

# Function to find Largest Rectangle area for that row (Refer problem: Largest Rectangle in Histogram)
def solve_histogram(A):
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


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
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
                    
        
        
