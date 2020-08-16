"""

Make Palindrome
Problem Description

Two players have got a string A, consisting of lowercase English letters. They play a game that is described by the following rules:

The players move in turns; In one move the player can remove an arbitrary letter from string A.
If the player before his turn can reorder the letters in string A so as to get a palindrome, this player wins.
NOTE:

A palindrome is a string that reads the same both ways (from left to right, and vice versa). For example, string "abba" is a palindrome and string "abc" isn't.



Problem Constraints
1 ≤ |A| ≤ 10^3



Input Format
The input contains a single line, containing string A.



Output Format
Return a single integer, 1 or 2, depending upon which player wins.



Example Input
Input 1:

 A = "aba"
Input 2:

 A = "abca"


Example Output
Output 1:

 1
Output 2:

 2


Example Explanation
Explanation 1:

 The string is already a palindrome. Hence player 1 wins.
Explanation 2:

 If player 1 erases characters 'b' or 'c', the string becomes a palindrome and player 2 wins.
 If player 1 erases character 'a', the string becoms "abc", since all characters are different now, any sequence of moves leads to winning of player 2.


"""


from collections import defaultdict

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        freq = defaultdict(int)
        count_odd = 0
        
        for c in A:
            freq[c] += 1
            
        for k in freq:
            if freq[k] % 2 == 1:
                count_odd += 1
                
        if count_odd != 0 and count_odd % 2 == 0:
            return 2
        return 1

