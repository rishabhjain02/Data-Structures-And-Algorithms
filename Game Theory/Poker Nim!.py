"""

Poker Nim!
Problem Description

Poker Nim is another 2 -player game that's a simple variation on a Nim game. The rules of the games are as follows:

The game starts with N piles of chips indexed from 0 to N - 1. Each pile i (where 0 <= i < N) has Ai chips.
The players move in alternating turns. During each move, the current player must perform either of the following actions:
Remove one or more chips from a single pile.
Add one or more chips to a single pile.
At least 1 chip must be added or removed during each turn.

To ensure that the game ends in finite time, a player cannot add chips to any pile i more than B times.
The player who removes the last chip wins the game.
Given the values of N, B and the numbers of chips in each of the N piles, determine whether the person who wins the game is the first or second person to move. Assume both players move optimally.



Problem Constraints
1 <= N <= 100

0 <= B <= 100

1 <= A[i] <= 10^9

Player 1 always goes first.



Input Format
First argument is an integer array A of size N denoting the number of chips in each pile.

Second argument is an integer B



Output Format
Return an string denoting the name of the winner(i.e., either First or Second).



Example Input
Input 1:

 A = [1, 2]
 B = 5
Input 2:

 A = [2, 1, 3]
 B = 5


Example Output
Output 1:

 First
Output 2:

 Second

"""


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a strings
    def solve(self, A, B):
        xor = 0
        
        for num in A:
            xor = xor ^ num
            
        if xor == 0:
            return "Second"
        
        return "First"
