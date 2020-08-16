"""

Scaler Nim!
Problem Description

Two people are playing game of Scaler Nim. The basic rules for this game are as follows:

The game starts with N piles of stones indexed from 0 to (N - 1). Each pile i (where 0 <= i <= N ) has Ai stones.
The players move in alternating turns. During each move, the current player must remove one or more stones from a single pile.
The player who removes the last stone loses the game.
Given an integer array A of size N denoting the number of stones in each pile, determine whether the person who wins the game is the first or second person to move. If the first player to move wins, return "First"; otherwise, return "Second". Assume both players move optimally.



Problem Constraints
1 <= N <= 100

1 <= A[i] <= 10^9

Player 1 always goes first.



Input Format
First and only argument is an integer array A of size N denoting the number of stones in each pile.



Output Format
Return an string denoting the name of the winner(i.e., either First or Second).



Example Input
Input 1:

 A = [1, 1]
Input 2:

 A = [2, 1, 3]


Example Output
Output 1:

 First
Output 2:

 Second


Example Explanation
Explanation 1:

 In the first testcase, the first player removes 1 stone from the first pile and then the second player has no moves other than removing 
 the only stone in the second pile. So first wins.
Explanation 2:

 In the second testcase, the series of moves can be depicted as:
 
 In every possible move of first player we see that the last stone is picked by him, so second player wins.

"""


# 1) If all are 1: if no. of piles odd: P2 win else: P1 win
# 2) Only one pile having value > 1: P1 win
# 3) [1, X] where X > 1, P1 win (as P1 remove X and P2 remain with 1)
# 4) From above three we conclude that if Xor sum is 0: P2 win except all are 1 and count is even 

class Solution:
    # @param A : list of integers
    # @return a strings
    def solve(self, A):
        n = len(A)
        xor = 0
        oneCount = A.count(1)
        
        if oneCount == n:
            if oneCount % 2 == 0:
                return "First"
            else:
                return "Second"
        
        for num in A:
            xor = xor ^ num
            
        if xor == 0:
            return "Second"
                
        return "First"
            
        
        
        
        
