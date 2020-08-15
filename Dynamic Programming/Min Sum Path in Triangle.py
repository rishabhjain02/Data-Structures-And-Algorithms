"""

Min Sum Path in Triangle
Problem Description

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

Adjacent numbers for jth number of row i is jth and (j+1)th numbers of row i+1 is



Problem Constraints
|A| <= 1000

A[i] <= 1000



Input Format
First and only argument is the vector of vector A defining the given triangle



Output Format
Return the minimum sum



Example Input
Input 1:

 
A = [ 
         [2],
        [3, 4],
       [6, 5, 7],
      [4, 1, 8, 3]
    ]
Input 2:

 A = [ [1] ]


Example Output
Output 1:

 11
Output 2:

 1


Example Explanation
Explanation 1:

 The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
Explanation 2:

 Only 2 can be collected.


"""


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def minimumTotal(self, A):
        n = len(A)
        m = len(A[-1])
        
        dp = [[float("inf") for j in range(m)] for i in range(n)]
        dp[0][0] = A[0][0]
        
        for i in range(1, n):
            for j in range(i+1):
                if j >= 1:
                    dp[i][j] = A[i][j] + min(dp[i-1][j], dp[i-1][j-1])
                else:
                    dp[i][j] = A[i][j] + dp[i-1][j]
                
        return min(dp[-1])
