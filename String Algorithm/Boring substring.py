"""

Boring substring
Problem Description

Given a string A of lowercase English alphabets. Rearrange the characters of the given string A such that there is no boring substring in A.

A boring substring has the following properties:

Its length is 2.
Both the characters are consecutive, for example - "ab", "cd", "dc", "zy" etc.(If the first character is C then the next character can be either (C+1) or (C-1)).
Return 1 if it possible to rearrange the letters of A such that there are no boring substring in A, else return 0.



Problem Constraints
1 <= |A| <= 100



Input Format
The only argument given is string A.



Output Format
Return 1 if it possible to rearrange the letters of A such that there are no boring substring in A, else return 0.



Example Input
Input 1:

 A ="abcd"
Input 2:

 A = "aab"


Example Output
Output 1:

 1
Output 2:

 0


Example Explanation
Explanation 1:

 String A can be rearranged into "cadb" or "bdac" 
Explanation 2:

 No arrangement of string A can make it free of boring substrings.

"""

# Solution 1:

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        n = len(A)
        odd = []
        even = []
        freq = [0]*26
        even_min = 0
        even_max = 0
        odd_min = 0
        odd_max = 0
        
        for char in A:
            freq[ord(char) - ord('a')] += 1
            
        for i in range(26):
            if i%2 == 0 and freq[i] > 0:
                even_min = i
                break
            
        for i in range(26):
            if i%2 != 0 and freq[i] > 0:
                odd_min = i
                break
        
        for i in range(25, -1, -1):
            if i%2 == 0 and freq[i] > 0:
                even_max = i
                break
        
        for i in range(25, -1, -1):
            if i%2 != 0 and freq[i] > 0:
                odd_max = i
                break
            
        if abs(even_min - odd_max) == 1 and abs(even_max - odd_min) == 1:
            return 0
        return 1
        
  
  


# Solution 2:
        
# class Solution:
#     # @param A : string
#     # @return an integer
#     def solve(self, A):
#         n = len(A)
#         odd = []
#         even = []
#         freq = [0]*26
        
#         for char in A:
#             freq[ord(char) - ord('a')] += 1        
        
#         for i in range(26):
#             if i%2 == 0:
#                 while freq[i] > 0:
#                     even.append(i)
#                     freq[i] -= 1
#             else:
#                 while freq[i] > 0:
#                     odd.append(i)
#                     freq[i] -= 1
                
#         if abs(even[-1]-odd[0]) == 1 and abs(even[0]-odd[-1]) == 1:
#             return 0
#         return 1

                
        
