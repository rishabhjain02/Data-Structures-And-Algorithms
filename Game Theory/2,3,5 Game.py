"""

2,3,5 Game
Problem Description

Two players called Alice and Bob are playing T independent games, each game starting with A[i] number of stones. In each game, Alice always plays first, and the two players move in alternating turns.

The game's rules are as follows:

In a single move, a player can remove either 2, 3, or 5 stones from the game board.
If a player is unable to make a move, that player loses the game.
Given the starting number of stones, find and print the name of the winner.

Each player plays optimally, meaning they will not make a move that causes them to lose the game if a winning move exists.



Problem Constraints
1 <= T <= 10^5

1 <= A[i] <= 10^5 (for all i in [ 1....T ])



Input Format
The first and only input argument is the array A



Output Format
You have to return an array of strings denoting the winner of the i-th game. The i-th string should be "Alice" if Alice wins the i-th game, otherwise it should be "Bob".



Example Input
Input 1:

A: [1, 6, 4]
Input 2:

A: [2, 3, 5]


Example Output
Output 1:

["Bob", "Alice", "Alice"]
Output 2:

["Alice", "Alice", "Alice"]


Example Explanation
Explanation 1:

If Alice starts with 1 stone, she can't make any move, so she loses.
If Alice starts with 6 stones, she removes 5 stones and Bob can't remove any stone. So Bob loses.
If Alice starts with 4 stone, she removes 3 stones and Bob can't remove any stone. So Bob loses.
Explanation 2:

If Alice starts with 2 stones, she removes 2 stones and Bob can't remove any stone. So Bob loses.
If Alice starts with 3 stones, she removes 3 stones and Bob can't remove any stone. So Bob loses.
If Alice starts with 5 stones, she removes 5 stones and Bob can't remove any stone. So Bob loses.


"""


class Solution:
    # @param A : list of integers
    # @return a list of strings
    def solve(self, A):
        n = len(A)
        max_num = max(A)
        dp = [0]*(max_num + 1)
        ans = []
        
        for i in range(2, min(5, max_num)):
            dp[i] = 1
            
        for i in range(5, max_num+1):
            dp[i] = not (dp[i-2] and dp[i-3] and dp[i-5])
            
        for num in A:
            if dp[num] == 1:
                ans.append("Alice")
            else:
                ans.append("Bob")
                
        return ans
