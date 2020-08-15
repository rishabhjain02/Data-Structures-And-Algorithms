"""

0-1 Knapsack II
Problem Description

Given two integer arrays A and B of size N each which represent values and weights associated with N items respectively.

Also given an integer C which represents knapsack capacity.

Find out the maximum value subset of A such that sum of the weights of this subset is smaller than or equal to C.

NOTE: You cannot break an item, either pick the complete item, or don’t pick it (0-1 property).



Problem Constraints
1 <= N <= 500

1 <= C, B[i] <= 10^6

1 <= A[i] <= 50



Input Format
First argument is an integer array A of size N denoting the values on N items.

Second argument is an integer array B of size N denoting the weights on N items.

Third argument is an integer C denoting the knapsack capacity.



Output Format
Return a single integer denoting the maximum value subset of A such that sum of the weights of this subset is smaller than or equal to C.



Example Input
Input 1:

 A = [6, 10, 12]
 B = [10, 20, 30]
 C = 50
Input 2:

 A = [1, 3, 2, 4]
 B = [12, 13, 15, 19]
 C = 10


Example Output
Output 1:

 22
Output 2:

 0


Example Explanation
Explanation 1:

 Taking items with weight 20 and 30 will give us the maximum value i.e 10 + 12 = 22
Explanation 2:

 Knapsack capacity is 10 but each item has weight greater than 10 so no items can be considered in the knapsack therefore answer is 0.


"""


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return an integer
    def solve(self, value, weight, capacity):
        n = len(value)
        sum_val = sum(value)
        max_val = 0
        
        dp = [[0 for j in range(sum_val + 1)] for i in range(n + 1)]
        
        # Initialising first cells in first row from second column to last column with infinite
        for j in range(1, sum_val+1):
            dp[0][j] = float("inf")
        
        for i in range(1, n+1):
            for j in range(1, sum_val+1):
                if value[i-1] <= j:
                    dp[i][j] = min(dp[i-1][j], weight[i-1] + dp[i-1][j-value[i-1]])
                    
                else:
                    dp[i][j] = dp[i-1][j]
                    
        for j in range(sum_val, -1, -1):
            if dp[n][j] <= capacity:
                return j
