"""

Count A
Problem Description

You are given a string A. Find the number of substrings that start and end with 'a'.



Problem Constraints
1 <= |A| <= 10^5

String will have only lowercase English letters.



Input Format
Given the only argument is a String A.



Output Format
Return number of substrings that start and end with 'a'.



Example Input
Input 1:

 A = "aab"
Input 2:

 A = "bcbc"


Example Output
Output 1:

 3
Output 2:

 0


Example Explanation
Explanation 1:

 Substrings that start and end with 'a' are:
    1. "a"
    2. "aa"
    3. "a"
Explanation 2:

 There are no substrings that start and end with 'a'.

"""

# Approach :
# if cur_char is a: it is already a valid substring and it can make 
# valid substrings with a's present in left of it.
# e.g. s = "xababad"
#           0123456
# First a (index:1)-> 1(self) + 0(a's present in left)   = 1
# Second a (index:3)-> 1(self) + 1(a's present in left)  = 2
# Third a (index:5)-> 1(self) + 2(a's present in left)   = 3
#                                                   ans  = 6 
# so, it is basically sum of A.P.
# Hence find count(n) of a's in s and find n*(n+1)/2.


class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        n = len(A)
        count = 0
        for c in A:
            if c == "a":
                count += 1
        ans = count*(count+1)//2
        return ans
