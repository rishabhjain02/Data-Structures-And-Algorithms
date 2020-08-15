"""

Tushar's Birthday Party
Problem Description

As it is Tushar's Birthday on March 1st, he decided to throw a party to all his friends at TGI Fridays in Pune. Given are the eating capacity of each friend, filling capacity of each dish and cost of each dish. A friend is satisfied if the sum of the filling capacity of dishes he ate is equal to his capacity. Find the minimum cost such that all of Tushar's friends are satisfied (reached their eating capacity).

NOTE:

Each dish is supposed to be eaten by only one person. Sharing is not allowed.

Each friend can take any dish unlimited number of times.

There always exists a dish with filling capacity 1 so that a solution always exists.



Problem Constraints
|A| <= 1000

|B| <= 1000

|C| <= 1000



Input Format
First Argument is vector A, denoting eating capacities

Second Argument is vector B, denoting filling capacities

Third Argument is vector C, denoting cost



Output Format
Return a single integer, the answer to the problem



Example Input
Input 1:

A = [2, 4, 6]
B = [2, 1, 3]
C = [2, 5, 3]
Input 2:

A = [2]
B = [1]
C = [2]


Example Output
Output 1:

12
Output 2:

4


Example Explanation
Explanation 1:

First friend takes dish 1, Second friend takes dish 1 twice and third friend takes dish 3 twice.
So 2 + 2*2 + 3*2 = 12.
Explanation 2:

Only way is to take 2 dishes of cost 2, hence 4.

"""


# Similar to 0/N Knapsack

class Solution:
	# @param A : tuple of integers
	# @param B : tuple of integers
	# @param C : tuple of integers
	# @return an integer
	def solve(self, capacity, filling, cost):
	    max_capacity = max(capacity)
	    n = len(filling)
        min_cost = 0
        
        dp = [[0 for j in range(max_capacity + 1)] for i in range(n + 1)]
        
        for j in range(1, max_capacity+1):
            dp[0][j] = float("inf")
            
        for i in range(1, n+1):
            for j in range(1, max_capacity+1):
                if filling[i-1] <= j:
                    dp[i][j] = min(dp[i-1][j], cost[i-1] + dp[i][j-filling[i-1]])
                    
                else:
                    dp[i][j] = dp[i-1][j]
                    
        for capacity in capacity:
            min_cost += dp[n][capacity]
            
        return min_cost
            
	    
