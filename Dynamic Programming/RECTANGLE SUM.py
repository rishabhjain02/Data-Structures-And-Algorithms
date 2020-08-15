"""

RECTANGLE SUM
Problem Description

Given a matrix of integers A of size N x M.

Calculate the sum of all submatrices and return the maximum among all those sums.

NOTE: Empty submatrix also need to be considered.



Problem Constraints
1 <= N, M <= 100
-10000 <= A[i] <= 10000



Input Format
The first and only argument given is the integer matrix A.



Output Format
Return the maximum sum among all those sums of all possible submatrices.



Example Input
Input 1:

 A = [
       [1, 3, -2]
       [1, 4, 6]
       [-4, -2, 1] 
     ]
Input 2:

 
A = [  
      [-1, -1]
      [-1, -1] 
    ]


Example Output
Output 1:

 13
Output 2:

 0


Example Explanation
Explanation 1:

 Submatrix giving maximum sum is : 
    [ 
       [1, 3, -2]
       [1, 4, 6]
    ]
Explanation 2:

 Sum of empty submatrix will be 0.

"""


def kadane(arr):
    n = len(arr)
    max_so_far = float("-inf")
    max_ending_here = 0
    
    for i in range(n):
        max_ending_here = max_ending_here + arr[i]
        max_so_far = max(max_so_far, max_ending_here)
        max_ending_here = max(0, max_ending_here)
        
    return max_so_far
        

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        rows = len(A)
        cols = len(A[0])
        ans = float("-inf")
        
        pre_sum = [[0 for j in range(cols)] for i in range(rows+1)]
                
        for i in range(rows):
            for j in range(cols):
                pre_sum[i+1][j] = pre_sum[i][j] + A[i][j]
                
        for i in range(rows):
            for j in range(i, rows):
                temp = [0]*cols
                for k in range(cols):
                    if i == j:
                        temp[k] = A[i][k]
                    else:
                        temp[k] = pre_sum[j+1][k] - pre_sum[i][k]
                        
                ans = max(ans, kadane(temp))
        
                
        return max(0, ans)        
        
        
        
