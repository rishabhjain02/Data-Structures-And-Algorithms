"""

Coin Game
Problem Description

Two people are playing the Coin Game! The rules of the game are:

The game is played on a line of N squares. The i-th square contains A[i] coins.
The players move in alternate turns. During each move, the current player must remove exactly 1 coin from i-th square and move it to j-th square if and only if 1 <= j < i.
The game ends when all coins are in square 1 and nobody can make a move. The first player to have no available move loses the game.
Determine whether the person who wins the game is the first or second person to move. Assume both players move optimally.



Problem Constraints
1 <= N <= 2^15
0 <= A[i] <= 10^9 (for i in [1 ... N])


Input Format
The first and only argument of the input is the array A.



Output Format
Your function should return the string "First" if the first player wins or "Second" otherwise.



Example Input
Input 1:

 A = [0, 2, 3, 0, 6]
Input 2:

 A = [0, 0, 0, 0]


Example Output
Output 1:

 "First"
Output 2:

 "Second"


Example Explanation
Explanation 1:

 The first player will shift one coin from squre 3 to square 1. 
 Hence, the second player is left with the squares [1,2,2,0,6]. 
 Now whatever be his/her move is, the first player can always nullify the change by shifting a coin to the same square where he/she shifted it. 
 Hence the last move is always played by the first player, so he wins.
Explanation 2:

 There are no coins in any of the squares so the first player cannot make any move, hence second player wins.


"""


class Solution:
    # @param A : list of integers
    # @return a strings
    def solve(self, A):
        n = len(A)
        xor = 0
        
        for i in range(n):
            if A[i] % 2 != 0:
                xor = xor ^ i
                
        if xor == 0:
            return "Second"
        
        return "First"
        
