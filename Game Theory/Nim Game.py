"""

Nim Game
Problem Description

Nim is the most famous two-player algorithm game. The basic rules for this game are as follows:

The game starts with a number of piles of stones. The number of stones in each pile may not be equal.
The players alternately pick up 1 or more stones from 1 pile
The player to remove the last stone wins.
Given an integer array A of size N denoting the number of stones in each pile, determine the game's winner if both players play optimally.



Problem Constraints
1 <= N <= 100

0 <= A[i] <= 100

Player 1 always goes first.



Input Format
First and only argument is an integer array A of size N denoting the number of stones in each pile.



Output Format
Return an string denoting the name of the winner(i.e., either First or Second).



Example Input
Input 1:

 A = [1, 1]
Input 2:

 A = [3, 2, 4]


Example Output
Output 1:

 Second
Output 2:

 First


Example Explanation
Explanation 1:

 In the first case, there are N = 2 piles of pile = [1, 1]  stones. Player 1 has to remove one pile on the first move. 
 Player 2 removes the second for a win.
Explanation 2:

 Play may proceed as follows:
    Player  Takes           Leaving
                          pile=[3,2,4]
    1       2 from pile[1]  pile=[3,4]
    2       2 from pile[1]  pile=[3,2]
    1       1 from pile[0]  pile=[2,2]
    2       1 from pile[0]  pile=[1,2]
    1       1 from pile[1]  pile=[1,1]
    2       1 from pile[0]  pile=[0,1]
    1       1 from pile[1]  WIN

"""


class Solution:
    # @param A : list of integers
    # @return a strings
    def solve(self, A):
        xor = 0
        
        for num in A:
            xor = xor ^ num
            
        if xor == 0:
            return "Second"
        
        return "First"
